from services.web_driver import create_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests

class InvoiceDownloader:
    def __init__(self):
        self.driver = create_driver(
            additional_options=[
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--headless"
            ]
        )

    def get_invoice(self, unit_consumption, cpf, date_birth):
        try:
            print("Acessando o site...")
            self.driver.get("https://celchatbotcom.celesc.com.br/")
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#textInput"))
            )
            print("Site acessado.")

            print("Interagindo com o bot...")
            text_input = self.driver.find_element(By.CSS_SELECTOR, "#textInput")

            # Enviar "segunda via" e pressionar Enter
            text_input.send_keys("segunda via")
            text_input.send_keys(Keys.RETURN)
            time.sleep(2)

            # Enviar a unidade consumidora e pressionar Enter
            text_input.send_keys(unit_consumption)
            text_input.send_keys(Keys.RETURN)
            time.sleep(2)

            # Enviar o CPF e pressionar Enter
            text_input.send_keys(cpf)
            text_input.send_keys(Keys.RETURN)
            time.sleep(2)

            # Enviar a data de nascimento e pressionar Enter
            text_input.send_keys(date_birth)
            text_input.send_keys(Keys.RETURN)
            time.sleep(2)

            print("Aguardando o botão de seleção da primeira fatura em aberto...")
            fatura_radio = WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="radio"]'))
            )
            fatura_radio.click()
            print("Fatura selecionada.")

            print("Aguardando o botão de download...")
            link_element = WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[target="_blank"]'))
            )
            link_element.click()
            print("Botão de download clicado.")

            print("Mudando para a aba de download...")
            self.driver.switch_to.window(self.driver.window_handles[-1])

            pdf_url = self.driver.current_url
            response = requests.get(pdf_url)
            pdf_path = "invoice_downloaded.pdf"
            with open(pdf_path, "wb") as f:
                f.write(response.content)
            
            return pdf_path 
        
        except Exception as e:
            print(f"Erro ao obter detalhes da fatura: {e}")
            raise
        
        finally:
            self.driver.quit()
