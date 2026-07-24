#!/bin/zsh
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

PORT="${PORT:-3000}"
URL="http://localhost:${PORT}/"

echo "=========================================="
echo "  TSN 腎臟專科考題練習站 (Exam Prepare)"
echo "=========================================="
echo
echo "開啟網址: $URL"
echo "按 Control-C 可關閉伺服器"
echo

if command -v open >/dev/null 2>&1; then
  (sleep 1.5 && open "$URL") &
fi

if [[ -d "$SCRIPT_DIR/node_modules" ]]; then
  npm run dev
else
  echo "正在首次安裝依賴套件..."
  npm install
  npm run dev
fi
