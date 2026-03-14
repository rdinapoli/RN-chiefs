#!/usr/bin/env python3
"""Extract text from Altman PDFs using PyMuPDF with tesseract fallback for image-only pages."""

import fitz
import pytesseract
from PIL import Image
import io
import os

PDF_DIR = "docs/references/pdfs/post_slave_raid/altman_2004"

# Files to extract (skip the book review)
FILES = [
    ("Altman-2004-EarlyVisitorsToEasterIsland-1864-1877-Part1.pdf", "altman_2004_part1_text.txt"),
    ("Altman-2004-EarlyVisitorsToEasterIsland-1864-1877-Part2.pdf", "altman_2004_part2_text.txt"),
    ("Altman-2004-EarlyVisitorsToEasterIsland-1864-1877-Part3.pdf", "altman_2004_part3_text.txt"),
    ("Altman-2004-EarlyVisitorsToEasterIsland-1864-1877-Part4.pdf", "altman_2004_part4_text.txt"),
    ("Altman-2004-EarlyVisitorsToEasterIsland-1864-1877-Part5.pdf", "altman_2004_part5_text.txt"),
    ("Altman-2003-EyraudSojourn.pdf", "altman_2003_eyraud_text.txt"),
]

MIN_TEXT_THRESHOLD = 50  # characters; below this, consider page image-only


def extract_page_text(page):
    """Extract text from a page, falling back to OCR if needed."""
    text = page.get_text()
    if len(text.strip()) >= MIN_TEXT_THRESHOLD:
        return text

    # Try OCR: render page to image at 300 DPI
    mat = fitz.Matrix(300 / 72, 300 / 72)
    pix = page.get_pixmap(matrix=mat)
    img_data = pix.tobytes("png")
    img = Image.open(io.BytesIO(img_data))
    ocr_text = pytesseract.image_to_string(img)

    if len(ocr_text.strip()) > len(text.strip()):
        return f"[OCR] {ocr_text}"
    return text


def extract_pdf(pdf_path, out_path):
    """Extract all text from a PDF."""
    doc = fitz.open(pdf_path)
    all_text = []
    ocr_count = 0

    for i, page in enumerate(doc):
        page_text = extract_page_text(page)
        is_ocr = page_text.startswith("[OCR]")
        if is_ocr:
            ocr_count += 1
        all_text.append(f"--- Page {i + 1} ---\n{page_text}\n")

    doc.close()

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(all_text))

    return len(all_text), ocr_count


if __name__ == "__main__":
    for pdf_name, txt_name in FILES:
        pdf_path = os.path.join(PDF_DIR, pdf_name)
        out_path = os.path.join(PDF_DIR, txt_name)

        if not os.path.exists(pdf_path):
            print(f"MISSING: {pdf_path}")
            continue

        pages, ocr_pages = extract_pdf(pdf_path, out_path)
        print(f"{pdf_name}: {pages} pages extracted ({ocr_pages} via OCR) -> {txt_name}")
