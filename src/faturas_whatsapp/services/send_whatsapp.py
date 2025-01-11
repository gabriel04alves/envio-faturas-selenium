from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def send_invoice(contact_name, holder, address, consumer_unit, month, due_date, total_to_pay, barcode):
    profile_path = os.path.join(os.getcwd(), "chrome_profile")

    # Configuração das opções do Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    options.add_argument(f"user-data-dir={profile_path}") 
    options.add_argument("--profile-directory=Default")
    
    driver = webdriver.Chrome(options=options)
    driver.get("https://web.whatsapp.com/")
    
    print("Escaneie o QR code para fazer login...")
    time.sleep(3)
    

    print(f"Buscando o contato {contact_name}...")
    try:
        contact_element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, f'//span[@title="{contact_name}"]')) # Elemento do contato
        )
        contact_element.click()  
        print(f"Contato {contact_name} encontrado.")

        messages = [f"Olá, *{contact_name}*!", f"A fatura de *{holder}* na *CELESC* está disponível", f"A cobrança é referente ao mês *{month}* no endereço *{address}*, unidade consumidora *{consumer_unit}*.", f"O total a pagar é *R${total_to_pay}*. O vencimento do boleto é em *{due_date}*." , f"Segue o código de barras para pagamento: {barcode}"]

        message_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true" and @data-tab="10"]')) # Local do input de mensagem 
        )

        def send_message(message):
            print(f"Tentando enviar mensagem.")
            message_box.click()
            message_box.send_keys(message)  
            time.sleep(1) 
            message_box.send_keys(Keys.ENTER)  
            print(f"Mensagem enviada com sucesso!")

        for message in messages:
            send_message(message)
            time.sleep(1)

        print("Mensagem enviada com sucesso!")

    except Exception as e:
        print(f"Erro ao enviar a mensagem: {str(e)}")
        return e
    
    finally:
        print("---------------------------------")
        driver.quit()  
