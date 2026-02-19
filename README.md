# 🟥 ThinkPad OS

![Version](https://img.shields.io/badge/version-v1.0.0-red)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Platform](https://img.shields.io/badge/platform-Linux-black)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

A unified ThinkPad-inspired terminal operating environment built with Python + Textual.

ThinkPad OS consolidates multiple custom TUIs into one master launcher called **ThinkOS**.

---

## ✨ What Is ThinkPad OS?

ThinkPad OS is a modular terminal ecosystem featuring:

- 🌧 **ThinkRain** — Cinematic ThinkPad rain engine
- 📺 **ThinkTube** — Terminal YouTube streaming client (mpv powered)
- 📰 **ThinkReddit** — Reddit browser with image preview
- 📁 **Commander (TPC)** — ThinkPad-style file manager
- 🎵 **M.A.M** — Media browser
- 🧠 **TPHelp** — Interactive command dashboard
- 🛰 **Nexus** — Sci-fi control interface
- 🖥 **ThinkOS** — Master launcher & control layer

---

## 🏗 Architecture

thinkpad-os/
│
├── thinkos/ # Master launcher
├── thinkrain/ # Cinematic animation engine
├── thinktube/ # YouTube streaming TUI
├── tpr/ # Reddit client
├── tpc/ # File manager
├── mam/ # Media manager
├── tphelp/ # Interactive dashboard
├── nexus/ # Themed command interface
│
├── install.sh
├── requirements.txt
└── README.md


Built using:

- Python 3
- Textual
- Rich
- mpv
- yt-dlp

---

## 📦 Requirements

### System Dependencies

Fedora:

```bash
sudo dnf install mpv yt-dlp git

Debian/Ubuntu:

sudo apt install mpv yt-dlp git

Python Dependencies

pip install --user textual rich psutil requests yt-dlp

Or simply run:

./install.sh

🚀 Installation

git clone https://github.com/Aector84/thinkpad-os.git
cd thinkpad-os
chmod +x install.sh
./install.sh

Launch the ecosystem:

thinkos

🧠 Usage
Command	Description
thinkos	Master launcher
rain	ThinkRain animation
tpvid	ThinkTube
tpr	ThinkReddit
tpc	Commander file manager
mam	Media browser
tphelp	Command dashboard
nexus	Nexus interface
🎛 Controls

Most applications use:

    ↑ ↓ Arrow navigation

    Enter to select

    q to quit

🖼 Screenshots

Add screenshots here for visual preview.

Example:

![ThinkOS](assets/thinkos.png)
![ThinkRain](assets/thinkrain.gif)

🛠 Troubleshooting
Command Not Found

Ensure ~/.local/bin is in your PATH:

echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

Textual Errors

Update textual:

pip install --user --upgrade textual

mpv Opens Fullscreen

ThinkTube should use:

--no-fullscreen
--geometry=960x540

🛣 Roadmap

    Shared theme engine

    Plugin architecture

    Auto-update system

    RPM packaging

    pip package release

    Cross-distro compatibility

    Config file support

    Animated ThinkOS splash

🤝 Contributing

Pull requests are welcome.

For major changes, open an issue first to discuss what you would like to change.
📜 License

MIT License
👤 Author

Built by Tony
Inspired by classic ThinkPad aesthetics.
