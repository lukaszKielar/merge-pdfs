import io
import PIL.Image as Image
from pathlib import Path
from typing import Union

import fitz


def render_preview(pdf_path: Union[str, Path], page_nr: int = 0):
    pdf = fitz.open(pdf_path)

    if page_nr > pdf.page_count or page_nr < 0:
        raise ValueError(
            f"Invalid page name: {page_nr}. File has {pdf.page_count} pages."
        )

    # TODO: I should hold state of previews.
    #  It doesn't make any sense to generate them if they were already created.
    #  Dict could be handy here, where key: name of the file, value: Image
    page = pdf.load_page(page_nr)
    pixmap = page.get_pixmap().getImageData()

    return Image.open(io.BytesIO(pixmap))
