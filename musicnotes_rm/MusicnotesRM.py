from pathlib import Path
import fitz
import io
from typing import Union, Optional
import re
import time
from pprint import pp

def rm_watermark(pdf: Path, name: str, output: Optional[Path]) -> Path:
    doc = fitz.open(pdf)
    for page in doc:
        rects = page.search_for(name)
        for rect in rects:
            page.add_redact_annot(rect)
        page.apply_redactions()
    if output is None:
        if pdf.parent.name == "old":
            par_folder = pdf.parents[1] / "new"
            if not par_folder.is_dir():
                par_folder.mkdir()
        else:
            par_folder = pdf.parent
        doc.save((par_folder / (time.strftime("%Y%m%d-%H%M%S") + ' ' + pdf.stem)).with_suffix(".pdf"))
    else:
        doc.save(output)
