import os
import platform
from pathlib import Path


class AppData:
    """Class that represents Application Data files."""

    def __init__(self):
        self._system = platform.system()
        self._create_app_data_folder()

    def _create_app_data_folder(self) -> None:
        Path.mkdir(self.path, exist_ok=True)

    @property
    def path(self) -> Path:
        if self._system == "Windows":
            _path = Path(os.getenv("APPDATA")) / "MergePDFs"
        else:
            _path = Path(os.getenv("HOME")) / ".mergepdfs"
        return _path

    # TODO: implement this method
    def save_cache(self):
        pass
