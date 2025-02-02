from textual import events, log, on, work
from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.screen import Screen, ModalScreen
from textual.widgets import Static, Label, Header, Button, Input, LoadingIndicator
from textual.containers import (
    Horizontal,
    Vertical,
    VerticalScroll,
    HorizontalScroll,
    Center,
    Container,
)
from textual.worker import Worker, WorkerState

from trading_client.screens import TradingScreen, LoginScreen

from trading_client.api import APIClient


class TradingApp(App):
    """ """

    CSS_PATH = ["style.tcss", "screens/screens.tcss"]

    BINDINGS = [("q", "quit", "Quit")]

    api = APIClient("http://localhost:8080")

    async def on_mount(self):
        self.push_screen(LoginScreen())

    async def on_unmount(self) -> None:
        await self.api.client.aclose()

    def action_quit(self):
        self.exit()


if __name__ == "__main__":
    app = TradingApp()
    app.run()
