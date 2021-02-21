from pathlib import Path
from typing import List

import kivy
from kivy.app import App as KivyApp
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


kivy.require("2.0.0")


class AppLayout(BoxLayout):
    pass


class App(KivyApp):
    _app_size = (800, 600)

    _pdf_files: List[Path] = []

    def build(self):
        self._app_layout = AppLayout()
        Window.bind(on_dropfile=self._on_dropfile)
        Window.size = self._app_size
        return self._app_layout

    def _on_dropfile(self, window: Window, file_path: bytes) -> None:
        file_path = Path(file_path.decode("utf-8"))

        # skip if it's not PDF
        if file_path.suffix.lower() != ".pdf":
            return

        # skip if file is already added as a Label
        if file_path in self._pdf_files:
            return
        # otherwise add to self._pdf_files
        else:
            self._pdf_files.append(file_path)

        _label = Label(
            text=Path(file_path).name,
            halign="left",
            valign="center",
            text_size=((self._app_size[0] / 2) - 50, None),
            max_lines=1,
            shorten=True,
        )

        self._app_layout.ids.pdf_files.add_widget(_label)


if __name__ == "__main__":
    App().run()
