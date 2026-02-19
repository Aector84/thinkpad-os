from textual.app import App, ComposeResult
from textual.widgets import Footer, ListView, ListItem, Label, Static
import subprocess


ASCII_HEADER = """
████████╗██╗  ██╗██╗███╗   ██╗██╗  ██╗ ██████╗ ███████╗
╚══██╔══╝██║  ██║██║████╗  ██║██║ ██╔╝██╔═══██╗██╔════╝
   ██║   ███████║██║██╔██╗ ██║█████╔╝ ██║   ██║███████╗
   ██║   ██╔══██║██║██║╚██╗██║██╔═██╗ ██║   ██║╚════██║
   ██║   ██║  ██║██║██║ ╚████║██║  ██╗╚██████╔╝███████║
   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
"""


TOOLS = [
    ("🌧 ThinkRain", "rain"),
    ("📺 ThinkTube", "tpvid"),
    ("📰 ThinkReddit", "tpr"),
    ("📁 Commander", "tpc"),
    ("🛰 Nexus", "nexus"),
    ("🎵 M.A.M", "mam"),
    ("🧠 TPHelp", "tphelp"),
    ("❌ Exit", None),
]


class ThinkOS(App):

    CSS = """
    Screen {
        background: #111111;
        align: center top;
    }

    #ascii {
        color: #5fa8ff;
        text-align: center;
        padding-top: 1;
        padding-bottom: 1;
    }

    ListView {
        border: round #333333;
        width: 50%;
        margin-top: 1;
    }

    ListItem.-highlight {
        background: #1a1a1a;
        color: #ff2b2b;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static(ASCII_HEADER, id="ascii")

        yield ListView(
            *[ListItem(Label(label)) for label, _ in TOOLS]
        )

        yield Footer()

    def on_list_view_selected(self, event: ListView.Selected):
        index = event.list_view.index
        label, command = TOOLS[index]

        if command is None:
            self.exit()
            return

        self.exit()
        subprocess.run(command, shell=True)


if __name__ == "__main__":
    ThinkOS().run()
