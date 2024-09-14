from __future__ import annotations

import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class AppData:
    """Class that represents Application Data files."""

    def __init__(self) -> None:
        self._settingsDir = Path.home() / ".mergepdfs"
        self._settingsFile = self._settingsDir / "settings.json"
        if not self._settingsFile.exists():
            Path.mkdir(self._settingsDir, parents=True, exist_ok=True)
            with open(self._settingsFile, "w") as f:
                json.dump({}, f)

        self._settings: dict[str, str] = self._loadSettings()

    def settingsDir(self) -> Path:
        return self._settingsDir

    def _loadSettings(self) -> dict[str, str]:
        logger.debug("Reading settings file: %s", self._settingsFile)
        with open(self._settingsFile, "r") as f:
            return dict(json.load(f))

    def _saveSettings(self) -> None:
        with open(self._settingsFile, "w") as fd:
            logger.debug("Saving settings file")
            json.dump(self._settings, fd, indent=2)

    def getSetting(self, setting: str) -> str | None:
        return self._settings.get(setting, None)

    def updateSetting(self, setting: str, value: str) -> None:
        oldValue = self._settings.get(setting, None)

        if oldValue == value:
            logger.debug(
                "Ignoring [%s] setting. Existing value is the same.", setting
            )
            return

        self._settings[setting] = value
        self._saveSettings()


APP_DATA = AppData()
