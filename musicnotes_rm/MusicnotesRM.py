from pathlib import Path
import fitz
import io
from typing import Union
import re
import time
from pprint import pp

def rm_watermark(pdf: Path, name: str) -> Path:
    doc = fitz.open(pdf)
    for page in doc:
        rects = page.search_for(name)
        for rect in rects:
            page.add_redact_annot(rect)
        page.apply_redactions()
    par_folder = pdf.parents[1] / "new"
    if not par_folder.is_dir():
        par_folder.mkdir()
    doc.save((par_folder / (time.strftime("%Y%m%d-%H%M%S") + ' ' + pdf.stem)).with_suffix(".pdf"))
