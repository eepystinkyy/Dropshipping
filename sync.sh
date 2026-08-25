#!/usr/bin/env bash
# Sync this folder with GitHub. Run before a Cowork session and again after.
# Optional argument becomes the commit message:
#     ./sync.sh added three candidate audiences
set -u
cd "$(dirname "$0")"

echo
echo "== Pulling latest from GitHub =="
git pull --no-rebase || { echo; echo "Pull failed. If it mentions CONFLICT, stop and ask Claude Code."; exit 1; }

git add -A
if git diff --cached --quiet; then
    echo
    echo "== Nothing new to save. You are up to date. =="
    exit 0
fi

MSG="${*:-Update from Cowork session}"
echo
echo "== Saving: $MSG =="
git commit -m "$MSG" || exit 1

echo
echo "== Pushing to GitHub =="
git push || { echo; echo "Push failed. Try again, or ask Claude Code."; exit 1; }

echo
echo "== Done. Claude Code can see your changes. =="
