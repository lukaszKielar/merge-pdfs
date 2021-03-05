import logging
from pathlib import Path
from typing import List, Union

from PyPDF4 import PdfFileMerger

logger = logging.getLogger(__name__)


class PDFWriter:
    def __init__(self) -> None:
        self._merger = PdfFileMerger()

    def merge_files(self, *pdf_files: List[Union[str, Path]]) -> None:
        logger.debug("Merging %d files", len(pdf_files))
        for pdf in pdf_files:
            with open(pdf, "rb") as f:
                self._merger.append(f)

    def save(self, out_path: Union[str, Path]) -> Path:
        logger.debug("Saving '%s' file", out_path)
        # add extension if doesn't exist
        if not str(out_path).lower().endswith(".pdf"):
            out_path += ".pdf"

        with open(out_path, "wb") as fd:
            self._merger.write(fd)

        return Path(out_path)
