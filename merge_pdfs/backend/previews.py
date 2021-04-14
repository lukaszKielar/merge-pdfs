import io
import shutil
import tempfile
from pathlib import Path
from typing import Dict, Union

# import fitz
import PIL.Image as Image


# FIXME: fitz library is not installed at the moment
class PreviewRenderer:
    """Class that generates pdf previews.

    It's utility class that allows to generate previews and show them in app viewer.
    It exists because Kivy doesn't support pdf natively.
    """

    def __init__(self, pdf_path: Union[str, Path]):
        self._pdf_file = fitz.open(pdf_path)
        self._page_count = self._pdf_file.page_count
        # init empty list of previews
        self._previews: Dict[int, Path] = dict(
            [(i, None) for i in range(self._page_count)]
        )

        self._tmp_dir = tempfile.TemporaryDirectory(dir=".")

    # TODO: it should be async method
    def render_preview(self, page: int) -> Path:

        if page > self._page_count or page < 0:
            raise ValueError(
                f"Invalid page name: {page}. File has {self._page_count} pages"
            )

        _preview_path = Path(self._tmp_dir.name) / f"{page}.jpg"

        # if the value for the key is present we've already created file
        if self._previews[page] is not None:
            return Image.open(_preview_path)

        # otherwise create preview and save it as a tmp file
        _page = self._pdf_file.load_page(page)
        pixmap = _page.get_pixmap().getImageData()
        preview = Image.open(io.BytesIO(pixmap))

        # save tmp file
        preview.save(_preview_path)

        # add preview path to list of previews
        self._previews[page] = _preview_path

        return _preview_path

    def clean_up(self):
        shutil.rmtree(self._tmp_dir.name)
