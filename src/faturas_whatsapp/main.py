from services.printer import print_invoice
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

    print_invoice(unit_consumption, cpf, date_birth)
