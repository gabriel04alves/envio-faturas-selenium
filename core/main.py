import os
from services.pdf_extractor import InvoiceExtractor
from services.send_whatsapp import send_invoice
from services.get_user_data import get_user_data

if __name__ == "__main__":
    open(os.path.join(os.path.dirname(__file__), '..', '.env'), 'w').close()

    unit_consumption, cpf, date_birth, contact_to_send_message = get_user_data()

    invoice_details = InvoiceExtractor(unit_consumption, cpf, date_birth)

    total_to_pay = invoice_details.get_total_to_pay()
    month = invoice_details.get_reference_month()
    holder = invoice_details.get_holder_name()
    address = invoice_details.get_address()
    due_date = invoice_details.get_due_date()
    barcode = invoice_details.get_barcode()
    # print(invoice_details._extract_text())

    print("Enviando fatura via WhatsApp...")

    send_invoice(contact_to_send_message, holder, address, unit_consumption, month, due_date, total_to_pay, barcode)
