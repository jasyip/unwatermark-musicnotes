from pathlib import Path
import PyPDF2
from PyPDF2 import pdf.PageObject as PageObject
import io

def rm_watermark(pdf: Union[bytes, io.BytesIO]) -> Path:
    reader = PyPDF2.PdfFileReader(io.BytesIO(pdf) if isinstance(pdf, bytes) else pdf)
    for i in range(reader.getNumPages()):
        page: PageObject = reader.getPage(i)
        print(f"{repr(page)=}")
