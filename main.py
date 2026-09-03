from operacoes import( somar, subtrair, multiplicar, dividir, potenciacao, raiz_quadrada, porcentagem)

from utils import ler_numero

from historico import salvar_historico, carregar_historico
from menu import exibir_menu

def executar_operacao(funcao, simbolo, historico):
    numero1 = ler_numero("Digite o primeiro número: ")
    numero2 = ler_numero("Digite o segundo número: ")

    resultado = funcao(numero1, numero2)

    if isinstance(resultado, str):
        print(f"\n{resultado}\n")
        return

    historico.append(f"{numero1} {simbolo} { numero2} = {resultado}")

    salvar_historico(historico)

    print(f"\nO resultado da operação é: {resultado}\n")

def executar_operacoes_unarias(funcao, simbolo, historico):
    numero = ler_numero("Digite um número: ")

    resultado = funcao(numero)

    if isinstance(resultado, str):
            print(f"\n{resultado}\n")
            return

    historico.append(f"{simbolo}{numero} = {resultado}")

    salvar_historico(historico)

    print(f"\nO resultado da operação é: {resultado}\n")

operacoes = {
    "1": (somar, "+"),
    "2": (subtrair, "-"),
    "3": (multiplicar, "*"),
    "4": (dividir, "/"),
    "5": (potenciacao, "^"),
    "7": (porcentagem, "%")
}

operacoes_unarias = {
    "6": (raiz_quadrada, "√")
}

historico = carregar_historico()

while True:
    exibir_menu()

    opcao = input("\nEscolha uma opção: ")

    if opcao == "0":
        print("\nDesligando Calculadora...")
        break

    elif opcao in operacoes:
        funcao, simbolo = operacoes[opcao]

        executar_operacao(funcao, simbolo, historico)

    elif opcao in operacoes_unarias:
        funcao, simbolo = operacoes_unarias[opcao]

        executar_operacoes_unarias(funcao, simbolo, historico)
      
    elif opcao == "8":

        if not historico:
            print("\nNenhuma operação foi realizada.\n")

        else:
            print("\n==== HISTÓRICO ====\n")

            for indice, operacao in enumerate(historico, start=1):
                print(f"{indice}. {operacao}")

    elif opcao =="9":

        historico.clear()

        salvar_historico(historico)

        print("\nHistórico apagado com sucesso!\n")
