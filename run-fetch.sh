#!/bin/bash
cd ~/scholar-pipeline
git pull --rebase origin main 2>/dev/null
python3 scripts/fetch.py
git add papers/ .fetch-state.json
if ! git diff --staged --quiet; then
  COUNT=$(git diff --staged --name-only -- papers/ | wc -l)
  git commit -m "feat: fetch ${COUNT} new papers $(date +%Y-%m-%d)"
  git push origin main
fi
