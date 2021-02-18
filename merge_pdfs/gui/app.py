from pathlib import Path

import kivy
from kivy.app import App as KivyApp
from kivy.uix.boxlayout import BoxLayout

from merge_pdfs.backend.app_data import AppData
from merge_pdfs.backend.previews import PreviewRenderer


kivy.require("2.0.0")


APP_DATA = AppData()


class AppLayout(BoxLayout):
    def selected(self, path: str) -> None:
        _path = Path(path[0])

        # update address bar and skip if it's folder
        if _path.is_dir():
            # self.ids.address_bar.text = path
            return

        _extension = _path.suffix.lower()

        if _extension == ".pdf":
            preview_generator = PreviewRenderer(_path)
            first_page_preview = preview_generator.render_preview(page=0)
            self.ids.image.source = str(first_page_preview)
            preview_generator.clean_up()
        # show all files we can, including all image formats
        else:
            try:
                self.ids.image.source = str(_path)
            # skip when error
            except:
                return

    def default_path(self) -> str:
        return str(Path.cwd())

    def go_to(self, path: str) -> None:
        if Path(path).exists():
            self.ids.filechooser.path = path
        else:
            return


class App(KivyApp):
    def build(self):
        return AppLayout()


if __name__ == "__main__":
    App().run()
