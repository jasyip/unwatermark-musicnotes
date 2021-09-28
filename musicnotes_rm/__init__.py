#!/usr/bin/env python3

import argparse
from .MusicnotesRM import rm_watermark
from pathlib import Path
from pprint import pp

def _main(args = None):
    parser = argparse.ArgumentParser()

    parser.add_argument("pdf", type=Path)
    parser.add_argument("-o", "--output", type=Path, default=None)
    parser.add_argument("name", nargs='+')

    args = parser.parse_args(args)

    if not (args.pdf.suffix == ".pdf" and args.pdf.is_file()):
        parser.error("Invalid PDF file")

    MusicnotesRM.rm_watermark(args.pdf, ' '.join(args.name), args.output)

if __name__ == "__main__":
    _main()
