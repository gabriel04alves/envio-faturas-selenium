def print_invoice(total_to_pay, reference_month):
    try:        
        print("-----------------------------")
        print(f'R$ {float(total_to_pay.replace(",", ".")):.2f}')
        print(f'Mês de referência: {reference_month}')
        print("Fatura impressa com sucesso!")
        
    except Exception as e:
        print(f"Erro ao imprimir a fatura: {e}")
        
    finally:
        print("-----------------------------")
