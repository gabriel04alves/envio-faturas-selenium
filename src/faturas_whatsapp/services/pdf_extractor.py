import fitz
import re

def extract_total_to_pay(pdf_path):
    document = fitz.open(pdf_path)
    text = "".join(page.get_text() for page in document)
    pattern = r"Total a Pagar \(R\$.*?\n(\d{1,3}(?:\.\d{3})*,\d{2})"
    match = re.search(pattern, text, re.DOTALL)
    return match.group(1) if match else None