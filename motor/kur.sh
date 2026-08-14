#!/usr/bin/env bash
set -e
PY=${PY:-python3}
OS=$(uname -s)

echo "==> python paketleri"
"$PY" -m pip install --quiet playwright pillow 2>/dev/null \
  || "$PY" -m pip install --quiet --break-system-packages playwright pillow

echo "==> chromium"
if [ -n "$PLAYWRIGHT_BROWSERS_PATH" ] && ls "$PLAYWRIGHT_BROWSERS_PATH"/chromium-*/chrome-linux*/chrome >/dev/null 2>&1; then
  echo "    hazır chromium: $PLAYWRIGHT_BROWSERS_PATH"
else
  "$PY" -m playwright install chromium
fi

if [ "$OS" = "Darwin" ]; then FDIR="$HOME/Library/Fonts"; else FDIR="$HOME/.fonts"; fi
mkdir -p "$FDIR"; echo "==> fontlar -> $FDIR"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT

# Inter: referans render rsms'in STATİK kesimini kullanıyor, önce onu dene
if [ ! -f "$FDIR/Inter-Regular.ttf" ]; then
  if curl -sfL -o "$TMP/i.zip" "https://github.com/rsms/inter/releases/download/v4.0/Inter-4.0.zip"; then
    unzip -o -q "$TMP/i.zip" -d "$TMP/i"
    for f in Regular Medium SemiBold Bold ExtraBold; do
      src=$(find "$TMP/i" -name "Inter-$f.ttf" | head -1)
      [ -n "$src" ] && cp "$src" "$FDIR/Inter-$f.ttf"
    done
  else
    echo "    release zip olmadı, Google variable Inter'e düşülüyor"
    curl -sfL -o "$FDIR/Inter-Regular.ttf" \
      "https://raw.githubusercontent.com/google/fonts/main/ofl/inter/Inter%5Bopsz%2Cwght%5D.ttf" || true
  fi
fi
[ -f "$FDIR/Anton-Regular.ttf" ] || curl -sfL -o "$FDIR/Anton-Regular.ttf" \
  "https://raw.githubusercontent.com/google/fonts/main/ofl/anton/Anton-Regular.ttf" || true
[ -f "$FDIR/Archivo.ttf" ] || curl -sfL -o "$FDIR/Archivo.ttf" \
  "https://raw.githubusercontent.com/google/fonts/main/ofl/archivo/Archivo%5Bwdth%2Cwght%5D.ttf" || true

command -v fc-cache >/dev/null 2>&1 && fc-cache -f >/dev/null 2>&1 || true

echo "==> font kontrolü"
EKSIK=0
for n in Inter-Regular Anton-Regular Archivo; do
  if [ -f "$FDIR/$n.ttf" ]; then echo "    ✓ $n"; else echo "    ✗ $n EKSİK"; EKSIK=1; fi
done
[ "$EKSIK" = "1" ] && echo "    UYARI: eksik font var, tipografi fallback'e düşecek"
echo "==> hazır:  $PY render.py T01"
