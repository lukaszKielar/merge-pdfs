from pathlib import Path
from kivy.app import App as KivyApp
from kivy.uix.boxlayout import BoxLayout

from merge_pdfs.backend.app_data import AppData


APP_DATA = AppData()


class MyWidget(BoxLayout):
    def selected(self, filename):
        try:
            self.ids.image.source = filename[0]
        except:
            pass

    def default_path(self) -> Path:
        return str(Path.cwd)


class App(KivyApp):
    def build(self):
        return MyWidget()


if __name__ == "__main__":
    App().run()
