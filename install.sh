#!/usr/bin/env bash

echo "Installing ThinkPad OS..."

pip install --user -r requirements.txt

mkdir -p ~/.local/bin

echo '#!/usr/bin/env bash
python3 $HOME/thinkpad-os/thinkos/main.py' > ~/.local/bin/thinkos

echo '#!/usr/bin/env bash
python3 $HOME/thinkpad-os/thinkrain/thinkrain.py' > ~/.local/bin/rain

echo '#!/usr/bin/env bash
python3 $HOME/thinkpad-os/thinktube/main.py' > ~/.local/bin/tpvid

echo '#!/usr/bin/env bash
python3 $HOME/thinkpad-os/tpr/main.py' > ~/.local/bin/tpr

echo '#!/usr/bin/env bash
python3 $HOME/thinkpad-os/tpc/main.py' > ~/.local/bin/tpc

echo '#!/usr/bin/env bash
python3 $HOME/thinkpad-os/mam/main.py' > ~/.local/bin/mam

echo '#!/usr/bin/env bash
python3 $HOME/thinkpad-os/tphelp/tphelp.py' > ~/.local/bin/tphelp

chmod +x ~/.local/bin/*

echo "Installation complete."
echo "Run: thinkos"
