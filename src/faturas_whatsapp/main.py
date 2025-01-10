from services.pdf_extractor import InvoiceExtractor
from services.printer import print_invoice
from services.send_whatsapp import send_invoice
from dotenv import load_dotenv
import os

load_dotenv()


if __name__ == "__main__": 
    unit_consumption = os.getenv('UNIT_CONSUMPTION')
    # unit_consumption = input('Digite a unidade consumidora (Ex.: 1234566789): ')

    cpf = os.getenv('CPF')
    # cpf = input('Digite o CPF (Ex.: 000000000-00): ')
    
    date_birth = os.getenv('DATE_BIRTH')
    # date_birth = input('Digite a data de nascimento (Ex.: DD/MM/AAAA): ')

    invoice_details = InvoiceExtractor()

    total_to_pay = invoice_details.get_total_to_pay()
    month = invoice_details.get_reference_month()
    holder = invoice_details.get_holder_name()
    address = invoice_details.get_address()

    print_invoice(total_to_pay, month)

    print("Enviando fatura via WhatsApp...")

    contact_name = input('Digite o nome do contato: ')
    send_invoice(contact_name, holder, address, unit_consumption, month, total_to_pay)
