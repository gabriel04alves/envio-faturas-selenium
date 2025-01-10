from services.downloader import InvoiceDownloader
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

    get_invoice_details = InvoiceDownloader().get_invoice_details(unit_consumption, cpf, date_birth)

    def get_total_to_pay():
        try:
            total_to_pay = get_invoice_details
            return total_to_pay
        
        except Exception as e:
            print(f"Erro ao buscar o total a pagar: {e}")
            return e

    total = get_total_to_pay()
    print_invoice(total)


    print("Enviando fatura via WhatsApp...")

    contact_name = input('Digite o nome do contato: ')
    send_invoice(contact_name, total)
