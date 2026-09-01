def ler_numero(mensagens):
    while True:
        try:
            return float(input(mensagens))
            
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")