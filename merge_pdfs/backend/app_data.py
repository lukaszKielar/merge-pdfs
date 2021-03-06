import os
import json
import logging
import platform
from pathlib import Path
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)


class AppData:
    """Class that represents Application Data files."""

    def __init__(self):
        self._create_app_data_folder()

        self._settings = self._load_settings()

    def __getattr__(self, attr: str) -> Optional[Any]:
        return self._settings.get(attr, None)

    def _create_app_data_folder(self) -> None:
        Path.mkdir(self._path, exist_ok=True)

    @property
    def _system(self) -> str:
        return platform.system()

    @property
    def _path(self) -> Path:
        if self._system == "Windows":
            _path = Path(os.getenv("APPDATA")) / "MergePDFs"
        else:
            _path = Path(os.getenv("HOME")) / ".mergepdfs"
        return _path

    @property
    def _settings_file(self) -> Path:
        return self._path / "settings.json"

    def _load_settings(self) -> Dict[str, Any]:
        logger.debug("Reading settings file: %s", self._settings_file)
        if not self._settings_file.exists():
            return {}

        with open(self._settings_file, "r") as f:
            return json.load(f)

    def save_setting(self, attr: str, value: Any) -> None:

        oldValue = self._settings.get(attr)

        # if there is old value check if it's different than passed attr and value
        # return when values are the same
        if oldValue:
            if oldValue == value:
                logger.debug(
                    "Ignoring, setting '%s' already has value of '%s'", attr, value
                )
                return

        self._settings[attr] = value

        with open(self._settings_file, "w") as fd:
            logger.debug('Saving {"%s":"%s"} setting into settings file', attr, value)
            json.dump(self._settings, fd, indent=2)

    def getLastDir(self) -> Path:
        if self.lastDir:
            return self.lastDir
        return str(Path.home())


APP_DATA = AppData()
