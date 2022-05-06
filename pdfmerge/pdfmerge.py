import argparse
from PyPDF2 import PdfFileMerger


def main():

    parser = argparse.ArgumentParser(
        prog="pdfmerge", description="Merge PDF files with a simple command"
    )

    parser.add_argument(
        "-i",
        "--input",
        metavar="PATH",
        nargs="+",
        required=True,
        help="input files, that should be merged",
    )
    parser.add_argument(
        "-o", "--output", metavar="FILE", default="out.pdf", help="name of output file",
    )

    args = parser.parse_args()
    merge(args.input, args.output)


def merge(paths, output):
    merger = PdfFileMerger()
    for path in paths:
        merger.append(path)

    merger.write(output)
    print("Files merged successfully in " + output)
