#!/usr/bin/env python3
"""Semantic Scholar daily paper fetcher.
Searches for recent Open Access papers by keyword,
outputs YAML-frontmatter Markdown files into papers/.
"""

import json
import os
import re
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from urllib.parse import quote

REPO_ROOT = Path(__file__).resolve().parent.parent
PAPERS_DIR = REPO_ROOT / "papers"
STATE_FILE = REPO_ROOT / ".fetch-state.json"

KEYWORDS = ["AI agent", "ESG", "NILM", "energy management"]
YEAR_RANGE = "2025-2026"
PER_KEYWORD = 10
API_BASE = "https://api.semanticscholar.org/graph/v1/paper/search"
FIELDS = "title,authors,year,abstract,externalIds,citationCount,isOpenAccess,openAccessPdf,url"

# API key: even with key, rate limit is 1 req/sec
# Key may take hours to propagate after approval; works fine without key if delays are respected
API_KEY = os.environ.get("SEMANTIC_SCHOLAR_API_KEY", "")
REQ_INTERVAL = 3  # seconds between API calls (1 req/sec limit + safety buffer)


def api_get(url, retries=3):
    """GET with retry on 429."""
    headers = {"Accept": "application/json"}
    if API_KEY:
        headers["x-api-key"] = API_KEY
    for attempt in range(retries):
        try:
            req = Request(url, headers=headers)
            with urlopen(req, timeout=30) as resp:
                return json.loads(resp.read())
        except HTTPError as e:
            if e.code in (429, 403):
                wait = 15 * (attempt + 1)
                print(f"  Rate limited ({e.code}), waiting {wait}s...")
                time.sleep(wait)
            else:
                raise
    return None


def fetch_arxiv_abstract_and_fulltext(arxiv_id: str) -> str:
    """Try to get extended content from ArXiv HTML."""
    if not arxiv_id:
        return ""
    url = f"https://export.arxiv.org/api/query?id_list={arxiv_id}"
    try:
        req = Request(url, headers={"Accept": "application/xml"})
        with urlopen(req, timeout=15) as resp:
            import xml.etree.ElementTree as ET
            root = ET.fromstring(resp.read())
            ns = {"atom": "http://www.w3.org/2005/Atom"}
            entry = root.find("atom:entry", ns)
            if entry is not None:
                summary = entry.find("atom:summary", ns)
                if summary is not None and summary.text:
                    return summary.text.strip()
    except Exception:
        pass
    return ""


def download_oa_pdf_text(pdf_url: str) -> str:
    """Download Open Access PDF and extract text. Returns empty if unavailable."""
    if not pdf_url:
        return ""
    try:
        req = Request(pdf_url, headers={"User-Agent": "ScholarPipeline/1.0"})
        with urlopen(req, timeout=30) as resp:
            pdf_bytes = resp.read()
            if len(pdf_bytes) > 10_000_000:  # skip >10MB PDFs
                return ""
        # Try pdfminer if available
        try:
            from io import BytesIO
            from pdfminer.high_level import extract_text
            text = extract_text(BytesIO(pdf_bytes))
            if text and len(text) > 200:
                # Truncate to ~50K chars for reasonable file size
                return text[:50000]
        except ImportError:
            pass
    except Exception:
        pass
    return ""


def slug(title):
    """Title -> filename-safe slug."""
    s = re.sub(r'[^\w\s-]', '', title.lower().strip())
    s = re.sub(r'[\s_]+', '-', s)
    return s[:80]


def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"fetched_ids": [], "last_run": None}


def save_state(state):
    state["last_run"] = datetime.now().isoformat()
    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False))


def fetch_keyword(keyword, state):
    """Fetch papers for one keyword, return list of new papers."""
    print(f"\n🔍 Searching: {keyword}")
    time.sleep(REQ_INTERVAL)  # pre-request delay to respect rate limit
    url = f"{API_BASE}?query={quote(keyword)}&year={YEAR_RANGE}&limit={PER_KEYWORD}&fields={FIELDS}"
    data = api_get(url)
    if not data:
        print(f"  ❌ Failed to fetch")
        return []

    total = data.get("total", 0)
    papers = data.get("data", [])
    print(f"  Found {total} total, got {len(papers)} results")

    new_papers = []
    for p in papers:
        pid = p.get("paperId", "")
        if pid in state["fetched_ids"]:
            continue

        title = p.get("title", "Untitled")
        year = p.get("year", "")
        abstract = p.get("abstract", "") or ""
        authors = [a.get("name", "") for a in (p.get("authors") or [])]
        citations = p.get("citationCount", 0)
        is_oa = p.get("isOpenAccess", False)
        oa_pdf = (p.get("openAccessPdf") or {}).get("url", "")
        ext_ids = p.get("externalIds") or {}
        doi = ext_ids.get("DOI", "")
        arxiv = ext_ids.get("ArXiv", "")
        s2_url = p.get("url", "")

        # Build tags from keyword
        tag = keyword.lower().replace(" ", "-")

        # Try to get full text
        fulltext = ""
        has_fulltext = False
        if oa_pdf:
            print(f"    📄 Trying PDF full text...")
            fulltext = download_oa_pdf_text(oa_pdf)
            if fulltext:
                has_fulltext = True
                print(f"    ✅ PDF text: {len(fulltext)} chars")

        # Write markdown
        filename = f"{year}-{slug(title)}.md"
        filepath = PAPERS_DIR / filename

        fulltext_section = ""
        if has_fulltext:
            fulltext_section = f"\n## Full Text (extracted from PDF)\n\n{fulltext}\n"

        content = f"""---
title: "{title}"
source: semantic-scholar
keyword: "{keyword}"
year: {year}
authors: [{', '.join(f'"{a}"' for a in authors[:5])}]
doi: "{doi}"
arxiv: "{arxiv}"
citations: {citations}
is_open_access: {str(is_oa).lower()}
pdf_url: "{oa_pdf}"
has_fulltext: {str(has_fulltext).lower()}
tags: [{tag}]
content_layer: L1
fetched: "{datetime.now().strftime('%Y-%m-%d')}"
---

## Abstract

{abstract if abstract else '_No abstract available._'}
{fulltext_section}
## Metadata

- **DOI**: {f'https://doi.org/{doi}' if doi else 'N/A'}
- **ArXiv**: {f'https://arxiv.org/abs/{arxiv}' if arxiv else 'N/A'}
- **Semantic Scholar**: {s2_url}
- **Open Access PDF**: {oa_pdf if oa_pdf else 'N/A'}
- **Citations**: {citations}
- **Authors**: {', '.join(authors)}
- **Full Text**: {'✅ Included' if has_fulltext else '❌ Abstract only (PDF unavailable or not Open Access)'}
"""
        filepath.write_text(content, encoding="utf-8")
        state["fetched_ids"].append(pid)
        new_papers.append({"title": title, "keyword": keyword, "file": filename})
        print(f"  ✅ {title[:60]}...")
        if oa_pdf:
            time.sleep(REQ_INTERVAL)  # respect rate limit between PDF downloads

    return new_papers


def main():
    PAPERS_DIR.mkdir(exist_ok=True)
    state = load_state()
    all_new = []

    for kw in KEYWORDS:
        new = fetch_keyword(kw, state)
        all_new.extend(new)
        time.sleep(3)  # respect 1 req/sec rate limit

    save_state(state)
    print(f"\n📊 Summary: {len(all_new)} new papers fetched")
    for p in all_new:
        print(f"  [{p['keyword']}] {p['title'][:60]}")

    return len(all_new)


if __name__ == "__main__":
    n = main()
    sys.exit(0)
