from operacoes import( somar, subtrair, multiplicar, dividir, potenciacao, raiz_quadrada)

from utils import ler_numero

from historico import salvar_historico, carregar_historico

def exibir_menu():
    print("="*30)
    print(" CALCULADORA INTELIGENTE ")
    print("="*30)
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potenciação")
    print("6. Raiz Quadrada")
    print("7. Ver Histórico")
    print("8. Limpar Histórico")
    print("0. Sair")

def executar_operacao(funcao, simbolo, historico):
    numero1 = ler_numero("Digite o primeiro número: ")
    numero2 = ler_numero("Digite o segundo número: ")

    resultado = funcao(numero1, numero2)

    historico.append(f"{numero1} {simbolo} { numero2} = {resultado}")

    salvar_historico(historico)

    print(f"\nO resultado da operação é: {resultado}\n")

def executar_operacoes_unarias(funcao, simbolo, historico):
    numero = ler_numero("Digite um número: ")

    resultado = funcao(numero)

    historico.append(f"{simbolo}{numero} = {resultado}")

    salvar_historico(historico)

    print(f"\nO resultado da operação é: {resultado}\n")

historico = carregar_historico()

while True:
    exibir_menu()

    opcao = input("\nEscolha uma opção: ")

    if opcao == "0":
        print("\nDesligando Calculadora...")
        break

    elif opcao == "1":
        executar_operacao(somar, "+", historico)

    elif opcao == "2":
        executar_operacao(subtrair, "-", historico)

    elif opcao == "3":
        executar_operacao(multiplicar, "*", historico)

    elif opcao == "4":
        executar_operacao(dividir, "/", historico)

    elif opcao == "5":
        executar_operacao(potenciacao, "^", historico)

    elif opcao == "6":
        executar_operacoes_unarias(raiz_quadrada, "√", historico)
        
    elif opcao == "7":

        if not historico:
            print("\nNenhuma operação foi realizada.\n")

        else:
            print("\n==== HISTÓRICO ====\n")

            for indice, operacao in enumerate(historico, start=1):
                print(f"{indice}. {operacao}")

    elif opcao =="8":

        historico.clear()

        salvar_historico(historico)

        print("\nHistórico apagado com sucesso!\n")
