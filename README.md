📘 README.md (Copy Everything Below)
# 🟥 ThinkPad OS — Terminal Ecosystem

A unified ThinkPad-inspired terminal operating environment built with Python + Textual.

ThinkPad OS consolidates multiple custom TUIs into one master launcher:

- 🌧 ThinkRain — Cinematic ThinkPad rain animation
- 📺 ThinkTube — Terminal YouTube streaming client
- 📰 ThinkReddit — Reddit viewer with image support
- 📁 Commander (TPC) — File manager
- 🎵 M.A.M — Media browser
- 🧠 TPHelp — Interactive command dashboard
- 🛰 Nexus — Sci-fi themed control interface
- 🖥 ThinkOS — Master launcher

---

## ✨ Features

- Unified ThinkOS launcher
- Global command installation
- ThinkPad red / IBM blue aesthetic
- Textual-based responsive TUIs
- YouTube playback via `mpv`
- Kitty image protocol support
- Rain animation engine
- Modular architecture
- Fully open-source

---

## 📦 Requirements

### System Requirements
- Linux (Tested on Fedora)
- Python 3.10+
- pip

### Required System Packages

```bash
sudo dnf install mpv yt-dlp git


(Use your distro’s equivalent if not Fedora)

🐍 Python Dependencies

Installed automatically via install.sh, but listed here:

textual

rich

psutil

requests

yt-dlp

Manual install if needed:

pip install --user textual rich psutil requests yt-dlp

🚀 Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/thinkpad-os.git
cd thinkpad-os


Run installer:

chmod +x install.sh
./install.sh


Then launch:

thinkos

🧠 Usage

Launch master control:

thinkos


Or run individual tools:

Command	Tool
rain	ThinkRain
tpvid	ThinkTube
tpr	ThinkReddit
tpc	Commander
mam	Media Manager
tphelp	Help Dashboard
nexus	Nexus Control
🎛 Controls

Most TUIs support:

↑ ↓ Arrow navigation

Enter to select

q to quit

ThinkTube:

Search YouTube

Playlist support

mpv mini-player mode

ThinkRain:

Animated gradient rain

Cinematic mode toggle

🛠 Troubleshooting
Command Not Found

Ensure ~/.local/bin is in your PATH:

echo $PATH


If not:

echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

mpv Opens Fullscreen

Ensure ThinkTube uses:

--no-fullscreen
--geometry=960x540

Kitty Image Mode Not Working

Make sure you are using Kitty terminal.
Image preview requires Kitty graphics protocol.

Textual CSS Errors

Ensure you are using latest textual:

pip install --user --upgrade textual

🧱 Project Structure
thinkpad-os/
│
├── thinkos/
├── thinkrain/
├── thinktube/
├── tpr/
├── tpc/
├── mam/
├── tphelp/
├── nexus/
│
├── install.sh
├── requirements.txt
└── README.md

🛣 Roadmap

 Shared theme engine

 Plugin architecture

 RPM packaging

 Auto-update system

 Config file support

 Cross-distro support

 Boot splash animation

🧑‍💻 Author

Built by Tony
Inspired by classic ThinkPad aesthetics.

📜 License

MIT License
