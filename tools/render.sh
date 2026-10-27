#!/bin/sh
# Renders the social preview images and PNG icons from the HTML templates
# here into ../public/assets with headless Edge. Run from this folder.
EDGE="/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
OUT="$(cd ../public/assets && pwd -W)"
HERE="$(pwd -W)"
shot() { # template width height output
  "$EDGE" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 \
    --default-background-color=00000000 --user-data-dir="$(mktemp -d)" --window-size="$2,$3" \
    --screenshot="$OUT/$4" "file:///$HERE/$1" 2>/dev/null
}
shot og-nb.html 1200 630 og.png
shot og-en.html 1200 630 og-en.png
