from __future__ import annotations

import logging
import shutil
import tempfile
from pathlib import Path

from PIL import Image
from pypdf import PdfWriter

from merge_pdfs.app_data import APP_DATA

logger = logging.getLogger(__name__)


class PDFWriter:
    def __init__(self) -> None:
        tmpDir = APP_DATA.settingsDir() / "tmp"
        Path(tmpDir).mkdir(parents=True, exist_ok=True)

        self._tmpDir = tempfile.TemporaryDirectory(dir=tmpDir)

    def _mergeFiles(self, files: list[Path]) -> PdfWriter:
        logger.debug("Merging [%d] files", len(files))

        merger = PdfWriter()

        for _file in files:
            # if it's image convert it to pdf first
            if _file.suffix.lower().endswith((".jpg", ".png")):
                with Image.open(_file) as image:
                    image.convert("RGB")

                    # save it as tmp file
                    _file = Path(self._tmpDir.name) / f"{_file.stem}.pdf"

                    logger.debug("Saving image as tmp [%s] file", _file)
                    image.save(_file)

            fd = open(_file, "rb")
            merger.append(fd)

        return merger

    def write(self, path: Path, files: list[Path]) -> None:
        merger = self._mergeFiles(files)

        # add extension if doesn't exist
        if not path.suffix.lower().endswith(".pdf"):
            path = Path(f"{path!s}.pdf")

        logger.debug("Writing to [%s] file", path)

        with open(path, "wb") as fd:
            merger.write(fd)

        merger.close()

        # clean up
        shutil.rmtree(self._tmpDir.name)
        logger.debug("Deleting [%s] tmp folder", self._tmpDir.name)
