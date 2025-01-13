import fitz
import re
from services.downloader import InvoiceDownloader

class InvoiceExtractor:
    def __init__(self, unit_consumption, cpf, date_birth):
        self.unit_consumption, self.cpf, self.date_birth = unit_consumption, cpf, date_birth
        downloader = InvoiceDownloader()
        self.pdf_path = downloader.get_invoice(
            self.unit_consumption, self.cpf, self.date_birth
        )
        self.text = self._extract_text()

    def _extract_text(self):
        document = fitz.open(self.pdf_path)
        return "".join(page.get_text() for page in document)

    def get_total_to_pay(self):
        pattern = r"Total a Pagar \(R\$.*?\n(\d{1,3}(?:\.\d{3})*,\d{2})"
        match = re.search(pattern, self.text, re.DOTALL)
        return match.group(1) if match else None

    def get_reference_month(self):
        pattern = r"Referência\s*(\d{2}/\d{4})"
        match = re.search(pattern, self.text)
        return match.group(1) if match else None
    
    def get_holder_name(self):
        pattern = r"([^\n]+)\s+Pagador:"
        match = re.search(pattern, self.text)
        return match.group(1).strip() if match else None

    def get_address(self):
        pattern = r"([^\n]+)\s+Endereço:"
        match = re.search(pattern, self.text)
        return match.group(1).strip() if match else None

    def get_due_date(self):
        pattern = r"Vencimento\s+(\d{2}/\d{2}/\d{4})"
        match = re.search(pattern, self.text)
        return match.group(1) if match else None
    
    def get_barcode(self):
        pattern = r"(\d{5}\.\d{5}\s*\d{5}\.\d{6}\s*\d{5}\.\d{6}\s*\d\s*\d{14})"
        match = re.search(pattern, self.text, re.DOTALL)
        return match.group(1).replace(" ", "") if match else None
