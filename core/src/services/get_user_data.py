from dotenv import load_dotenv, set_key
import os

def get_user_data():
    load_dotenv()  # Carregar variáveis de ambiente do arquivo .env

    if not os.getenv('UNIT_CONSUMPTION') or not os.getenv('CPF') or not os.getenv('DATE_BIRTH'):
        unit_consumption = input('Digite a unidade consumidora (Ex.: 1234566789): ')
        cpf = input('Digite o CPF (Ex.: 000000000-00): ')
        date_birth = input('Digite a data de nascimento (Ex.: DD/MM/AAAA): ')

        set_key('.env', 'UNIT_CONSUMPTION', unit_consumption)
        set_key('.env', 'CPF', cpf)
        set_key('.env', 'DATE_BIRTH', date_birth)
        
    else:
        unit_consumption = os.getenv('UNIT_CONSUMPTION')
        cpf = os.getenv('CPF')
        date_birth = os.getenv('DATE_BIRTH')

    return unit_consumption, cpf, date_birth
