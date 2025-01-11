from services.pdf_extractor import InvoiceExtractor
from services.send_whatsapp import send_invoice
from services.get_user_data import get_user_data
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == "__main__": 
    unit_consumption, cpf, date_birth = get_user_data()

    invoice_details = InvoiceExtractor(unit_consumption, cpf, date_birth)

    total_to_pay = invoice_details.get_total_to_pay()
    month = invoice_details.get_reference_month()
    holder = invoice_details.get_holder_name()
    address = invoice_details.get_address()
    due_date = invoice_details.get_due_date()
    barcode = invoice_details.get_barcode()

    # print(invoice_details._extract_text())

    print("Enviando fatura via WhatsApp...")

    contact_name = input('Digite o nome do contato: ')
    send_invoice(contact_name, holder, address, unit_consumption, month, due_date, total_to_pay, barcode)
