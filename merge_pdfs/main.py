from __future__ import annotations

import sys

from PySide6.QtWidgets import QApplication

from merge_pdfs.gui.app import App
from merge_pdfs.logger import AppLogger

logger = AppLogger.default()


if __name__ == "__main__":
    try:
        app = QApplication([])
        window = App()
        window.show()
        exitCode = app.exec()
    except Exception:
        # TODO: print message box with exception and
        #  button that allows to copy the content of the message
        logger.exception("Application failed")
        exitCode = 1
    finally:
        sys.exit(exitCode)
