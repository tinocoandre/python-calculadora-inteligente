def ler_numero(mensagens):
    while True:
        try:
            numero = float(input(mensagens))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")