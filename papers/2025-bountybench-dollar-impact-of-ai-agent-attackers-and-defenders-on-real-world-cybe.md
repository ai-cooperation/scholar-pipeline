---
title: "BountyBench: Dollar Impact of AI Agent Attackers and Defenders on Real-World Cybersecurity Systems"
source: semantic-scholar
keyword: "AI agent"
year: 2025
authors: ["Andy K. Zhang", "Joey Ji", "Celeste Menders", "Riya Dulepet", "T. Qin"]
doi: "10.48550/arXiv.2505.15216"
arxiv: "2505.15216"
citations: 17
is_open_access: false
pdf_url: ""
has_fulltext: false
tags: [ai-agent]
content_layer: L1
fetched: "2026-04-11"
---

## Abstract

AI agents have the potential to significantly alter the cybersecurity landscape. Here, we introduce the first framework to capture offensive and defensive cyber-capabilities in evolving real-world systems. Instantiating this framework with BountyBench, we set up 25 systems with complex, real-world codebases. To capture the vulnerability lifecycle, we define three task types: Detect (detecting a new vulnerability), Exploit (exploiting a given vulnerability), and Patch (patching a given vulnerability). For Detect, we construct a new success indicator, which is general across vulnerability types and provides localized evaluation. We manually set up the environment for each system, including installing packages, setting up server(s), and hydrating database(s). We add 40 bug bounties, which are vulnerabilities with monetary awards from \$10 to \$30,485, covering 9 of the OWASP Top 10 Risks. To modulate task difficulty, we devise a new strategy based on information to guide detection, interpolating from identifying a zero day to exploiting a given vulnerability. We evaluate 10 agents: Claude Code, OpenAI Codex CLI with o3-high and o4-mini, and custom agents with o3-high, GPT-4.1, Gemini 2.5 Pro Preview, Claude 3.7 Sonnet Thinking, Qwen3 235B A22B, Llama 4 Maverick, and DeepSeek-R1. Given up to three attempts, the top-performing agents are Codex CLI: o3-high (12.5% on Detect, mapping to \$3,720; 90% on Patch, mapping to \$14,152), Custom Agent: Claude 3.7 Sonnet Thinking (67.5% on Exploit), and Codex CLI: o4-mini (90% on Patch, mapping to \$14,422). Codex CLI: o3-high, Codex CLI: o4-mini, and Claude Code are more capable at defense, achieving higher Patch scores of 90%, 90%, and 87.5%, compared to Exploit scores of 47.5%, 32.5%, and 57.5% respectively; while the custom agents are relatively balanced between offense and defense, achieving Exploit scores of 17.5-67.5% and Patch scores of 25-60%.

## Metadata

- **DOI**: https://doi.org/10.48550/arXiv.2505.15216
- **ArXiv**: https://arxiv.org/abs/2505.15216
- **Semantic Scholar**: https://www.semanticscholar.org/paper/600d42802b275ea7b2e4ddcd52de5af68d8ee994
- **Open Access PDF**: N/A
- **Citations**: 17
- **Authors**: Andy K. Zhang, Joey Ji, Celeste Menders, Riya Dulepet, T. Qin, Ron Yifeng Wang, Jun Wu, Kyleen Liao, Jiliang Li, Jinghan Hu, Sara Hong, Nardos Demilew, Shivatmica Murgai, Jason Tran, Nishka Kacheria, Ethan Ho, Denis Liu, Lauren McLane, O. Bruvik, Dai-Rong Han, Seungwoo Kim, Akhil Vyas, Cui Chen, Ryan Li, Weiran Xu, J. Z. Ye, Prerit Choudhary, Siddharth M. Bhatia, V. Sivashankar, Yu Bao, D. Song, Dan Boneh, Daniel E. Ho, Percy Liang
- **Full Text**: ❌ Abstract only (PDF unavailable or not Open Access)
