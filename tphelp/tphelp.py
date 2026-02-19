#!/usr/bin/env python3

import shutil
import subprocess
import platform
import psutil

from textual.app import App, ComposeResult
from textual.widgets import ListView, ListItem, Label, Input, Static
from textual.containers import Horizontal, Vertical
from textual import events

ASCII_HEADER = r"""
████████╗██████╗ ██╗  ██╗███████╗██╗     ██████╗ 
╚══██╔══╝██╔══██╗██║  ██║██╔════╝██║     ██╔══██╗
   ██║   ██████╔╝███████║█████╗  ██║     ██████╔╝
   ██║   ██╔═══╝ ██╔══██║██╔══╝  ██║     ██╔═══╝ 
   ██║   ██║     ██║  ██║███████╗███████╗██║     
   ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     
"""

COMMANDS = {
    # =========================
    # 🔴 ThinkPad TUI Apps
    # =========================
    "rain": "ThinkRain cinematic engine",
    "tpvid": "ThinkTube streaming client",
    "tpr": "ThinkReddit client",
    "tpc": "ThinkPad Commander",
    "tphelp": "ThinkPad Help dashboard",
    "nexus": "Weyland-Yutani Nexus interface",
    "mam": "Music And Movies manager",

    # =========================
    # 📦 Git & GitHub
    # =========================
    "git status": "Check repository status",
    "git add .": "Stage all changes",
    "git commit -m": "Commit changes",
    "git push": "Push to GitHub",
    "git pull": "Pull from GitHub",
    "git log --oneline": "View commit history",
    "git tag": "Create version tag",
    "gh release create": "Create GitHub release",

    # =========================
    # 🐍 Python
    # =========================
    "python3 file.py": "Run Python file",
    "pip install package": "Install Python package",
    "pip list": "List installed packages",
    "venv": "Create virtual environment",

    # =========================
    # 🖥️ Linux Basics
    # =========================
    "ls": "List directory contents",
    "ls -la": "List with hidden files",
    "cd folder": "Change directory",
    "pwd": "Show current directory",
    "mkdir folder": "Create directory",
    "rm -rf folder": "Remove directory",
    "chmod +x file": "Make file executable",
    "clear": "Clear terminal",
    "history": "Show command history",

    # =========================
    # 🎥 Media / MPV
    # =========================
    "mpv url": "Play media from URL",
    "mpv file.mp4": "Play local file",
    "mpv --no-fullscreen": "Force windowed mode",

    # =========================
    # 🧪 Dev Utilities
    # =========================
    "grep -R": "Recursive search",
    "find . -name": "Find files",
    "top": "System monitor",
    "htop": "Enhanced system monitor",
    "neofetch": "System info display",

    # =========================
    # 🧩 ThinkRain Dev
    # =========================
    "rain --cinema": "Enable cinematic mode",
    "rain --dense": "Increase rain density",
    "rain --slow": "Slow motion mode",
}

def tool_exists(cmd):
    return shutil.which(cmd.split()[0]) is not None

ALL_TOOLS = {

    "ThinkPad Apps": [
        ("rain", "ThinkRain cinematic engine"),
        ("tpvid", "ThinkTube streaming client"),
        ("tpr", "ThinkReddit client"),
        ("tpc", "ThinkPad Commander"),
        ("tphelp", "ThinkPad Help dashboard"),
        ("nexus", "Weyland-Yutani Nexus interface"),
        ("mam", "Music And Movies manager"),
    ],

    "Git & GitHub": [
        ("git status", "Check repository status"),
        ("git add .", "Stage all changes"),
        ("git commit -m", "Commit changes"),
        ("git push", "Push to GitHub"),
        ("git pull", "Pull from GitHub"),
        ("git log --oneline", "View commit history"),
        ("git tag", "Create version tag"),
        ("gh release create", "Create GitHub release"),
    ],

    "Python": [
        ("python3 file.py", "Run Python file"),
        ("pip install package", "Install Python package"),
        ("pip list", "List installed packages"),
        ("python3 -m venv venv", "Create virtual environment"),
    ],

    "Linux Basics": [
        ("ls", "List directory contents"),
        ("ls -la", "List with hidden files"),
        ("cd folder", "Change directory"),
        ("pwd", "Show current directory"),
        ("mkdir folder", "Create directory"),
        ("rm -rf folder", "Remove directory"),
        ("chmod +x file", "Make file executable"),
        ("clear", "Clear terminal"),
        ("history", "Show command history"),
    ],

    "Media / MPV": [
        ("mpv url", "Play media from URL"),
        ("mpv file.mp4", "Play local file"),
        ("mpv --no-fullscreen", "Force windowed mode"),
    ],

    "Dev Utilities": [
        ("grep -R", "Recursive search"),
        ("find . -name", "Find files"),
        ("top", "System monitor"),
        ("htop", "Enhanced system monitor"),
        ("neofetch", "System info display"),
    ],
}


class TPHelp(App):

    CSS = """
    Screen {
        background: #111111;
    }

    #header {
        color: #5fa8ff;
        text-align: center;
    }

    #subtitle {
        color: #ff2b2b;
        text-align: center;
        padding-bottom: 1;
    }

    #left {
        width: 60%;
        border: round #333333;
    }

    #right {
        width: 40%;
        border: round #333333;
        padding: 1;
    }

    ListItem.-highlight {
        background: #222222;
        color: #ff2b2b;
    }

    #search {
        dock: bottom;
        border: round #333333;
    }
    """

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("/", "focus_search", "Search"),
    ]

    def compose(self) -> ComposeResult:
        yield Static(ASCII_HEADER, id="header")
        yield Static("ThinkPad Control Console", id="subtitle")

        with Horizontal():
            with Vertical(id="left"):
                self.list_view = ListView()
                yield self.list_view

            with Vertical(id="right"):
                self.sysinfo = Static(self.get_system_info())
                yield self.sysinfo

        self.search = Input(placeholder="Search...", id="search")
        yield self.search
        self.search.display = False

    def on_mount(self):
        self.populate_list()

    def populate_list(self, filter_text=""):
        self.list_view.clear()

        for category, items in ALL_TOOLS.items():
            visible = [
                (cmd, desc)
                for cmd, desc in items
                if tool_exists(cmd) and (
                    filter_text.lower() in cmd.lower()
                    or filter_text.lower() in desc.lower()
                )
            ]

            if visible:
                self.list_view.append(ListItem(Label(f"[ {category} ]")))

                for cmd, desc in visible:
                    item = ListItem(Label(f"{cmd:<20} {desc}"))
                    item.command = cmd
                    self.list_view.append(item)

    def action_focus_search(self):
        self.search.display = True
        self.search.focus()

    def on_input_changed(self, event: Input.Changed):
        self.populate_list(event.value)

    def on_input_submitted(self, event: Input.Submitted):
        self.search.display = False
        self.set_focus(self.list_view)

    def on_list_view_selected(self, event):
        cmd = getattr(event.item, "command", None)
        if cmd:
            self.suspend()
            subprocess.run(cmd, shell=True)
            self.resume()

    def get_system_info(self):
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory().percent
        sys = platform.system()
        release = platform.release()

        return (
            f"System: {sys} {release}\n"
            f"CPU Usage: {cpu}%\n"
            f"Memory Usage: {mem}%\n"
        )

if __name__ == "__main__":
    TPHelp().run()
