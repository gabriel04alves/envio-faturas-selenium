from services.downloader import InvoiceDownloader

def print_invoice(total_to_pay):
    try:        
        print("-----------------------------")
        print(f'R$ {float(total_to_pay.replace(",", ".")):.2f}')
        print("Fatura impressa com sucesso!")
        
    except Exception as e:
        print(f"Erro ao imprimir a fatura: {e}")
        
    finally:
        print("-----------------------------")
