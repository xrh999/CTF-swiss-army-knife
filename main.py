# main.py
from textual.app import App, ComposeResult
from textual.widgets import Static, Header, Footer
from textual.containers import Vertical

class CTFKnifeApp(App):
    CSS_PATH = None  # You can add styling later

    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Static("🔪 Welcome to CTF Swiss Army Knife 🔪\n", id="title"),
            Static("Choose a tool from the menu (coming soon)...", id="body")
        )
        yield Footer()

if __name__ == "__main__":
    CTFKnifeApp().run()
