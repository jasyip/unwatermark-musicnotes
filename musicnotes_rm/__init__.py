#!/usr/bin/env python3

import argparse
from .MusicnotesRM import MusicnotesRM
from pathlib import Path

def main(args = None):
    parser = argparse.ArgumentParser()

    parser.add_argument("pdf", type=Path)

    args = parser.parse_args(args)

    if not (arg.pdf.suffix == "pdf" and arg.pdf.is_file()):
        parser.error("Invalid PDF file")

    MusicnotesRM.rm_watermark(args.pdf.read_bytes())

if __name__ == "__main__":
    main()
