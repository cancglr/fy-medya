#!/usr/bin/env bash
# Flört AI reel motoru — kurulum
# Gereken: python3, ffmpeg, curl, unzip
set -e

echo "==> python paketleri"
pip install --quiet --break-system-packages playwright pillow 2>/dev/null || pip install --quiet playwright pillow

echo "==> chromium"
if [ -n "$PLAYWRIGHT_BROWSERS_PATH" ] && ls "$PLAYWRIGHT_BROWSERS_PATH"/chromium-*/chrome-linux*/chrome >/dev/null 2>&1; then
  echo "    hazır chromium bulundu: $PLAYWRIGHT_BROWSERS_PATH"
else
  python3 -m playwright install chromium
fi

echo "==> fontlar (Inter + Anton)"
mkdir -p "$HOME/.fonts" && cd "$HOME/.fonts"
for f in Regular Medium SemiBold Bold ExtraBold; do
  [ -f "Inter-$f.ttf" ] || curl -sfL -o "Inter-$f.ttf" \
    "https://raw.githubusercontent.com/rsms/inter/v4.0/docs/font-files/Inter-$f.ttf" || true
done
[ -f Anton-Regular.ttf ] || curl -sfL -o Anton-Regular.ttf \
  "https://raw.githubusercontent.com/google/fonts/main/ofl/anton/Anton-Regular.ttf"
[ -f "Archivo.ttf" ] || curl -sfL -o "Archivo.ttf" \
  "https://raw.githubusercontent.com/google/fonts/main/ofl/archivo/Archivo%5Bwdth%2Cwght%5D.ttf"
fc-cache -f >/dev/null 2>&1 || true

echo "==> hazır. çalıştırmak için:  python3 render.py"
