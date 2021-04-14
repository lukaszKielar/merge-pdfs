import logging
import shutil
import tempfile
from pathlib import Path
from typing import List, Union

from PIL import Image
from PyPDF4 import PdfFileMerger

logger = logging.getLogger(__name__)


class PDFWriter:
    def __init__(self) -> None:
        self._merger = PdfFileMerger()

        self._tmp_dir = tempfile.TemporaryDirectory(dir=".")

    def merge_files(self, *files: List[Union[str, Path]]) -> None:
        logger.debug("Merging %d files", len(files))
        for _file in files:
            # if it's image convert it to pdf first
            if str(_file).lower().endswith((".jpg", ".png")):

                image = Image.open(_file)
                image.convert("RGB")

                # save it as tmp file
                _file = Path(self._tmp_dir.name) / f"{Path(_file).stem}.pdf"

                logger.debug("Save image as tmp pdf file '%s'", _file)
                image.save(_file)

            with open(_file, "rb") as f:
                self._merger.append(f)

    def save(self, out_path: Union[str, Path]) -> Path:
        logger.debug("Saving '%s' file", out_path)
        # add extension if doesn't exist
        if not str(out_path).lower().endswith(".pdf"):
            out_path += ".pdf"

        with open(out_path, "wb") as fd:
            self._merger.write(fd)

        # clean up
        shutil.rmtree(self._tmp_dir.name)
        logger.debug("Tmp folder '%s' deleted", self._tmp_dir.name)

        return Path(out_path)
