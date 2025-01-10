import fitz
import re
from services.downloader import InvoiceDownloader
import os
class InvoiceExtractor:
    def __init__(self):
        downloader = InvoiceDownloader()
        self.pdf_path = downloader.get_invoice(
            os.getenv('UNIT_CONSUMPTION'), 
            os.getenv('CPF'), 
            os.getenv('DATE_BIRTH')
        )
        self.text = self._extract_text()

    def _extract_text(self):
        # Extrai o texto de todas as páginas do PDF.
        document = fitz.open(self.pdf_path)
        return "".join(page.get_text() for page in document)

    def get_total_to_pay(self):
        # Extrai o total a pagar da fatura
        pattern = r"Total a Pagar \(R\$.*?\n(\d{1,3}(?:\.\d{3})*,\d{2})"
        match = re.search(pattern, self.text, re.DOTALL)
        return match.group(1) if match else None

    def get_reference_month(self):
        # Extrai o mês de referência da fatura.
        pattern = r"Referência\s*(\d{2}/\d{4})"
        match = re.search(pattern, self.text)
        return match.group(1) if match else None
    
    def get_holder_name(self):
        # Extrai o nome do titular da fatura.
        pattern = r"Pagador:\s*(.*)"
        match = re.search(pattern, self.text)
        return match.group(1).strip() if match else None

    def get_address(self):
        # Extrai o endereço da fatura.
        pattern = r"Endereço:\s*(.*)"
        match = re.search(pattern, self.text)
        return match.group(1).strip() if match else None


