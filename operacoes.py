import math

def somar(numero1, numero2):
    """
    Função para somar dois números.

    Args:
        numero1 (float): O primeiro número.
        numero2 (float): O segundo número.

    Returns:
        float: A soma dos dois números.
    """
    return numero1 + numero2

def subtrair(numero1, numero2):
    """
    Função para subtrair dois números.

    Args:
        numero1 (float): O primeiro número.
        numero2 (float): O segundo número.

    Returns:
        float: A diferença entre os dois números.
    """
    return numero1 - numero2

def multiplicar(numero1, numero2):
    """
    Função para multiplicar dois numeros

    Args:
        numero1 (float): O primeiro número
        numero2 (float): O segundo número

    Returns:
        float: A multiplicação entre dois números
    """
    return numero1 * numero2

def dividir(numero1, numero2):
    if numero2 == 0:
        return "Erro: Divisão por zero não é permitida."

    return numero1 / numero2
    

def potenciacao(base, expoente):
    try:
        resultado = base ** expoente

        if abs(resultado) > 1e308:
            return "Erro: resultado muito grande."

        return resultado

    except OverflowError:
        return "Erro: resultado muito grande."

def raiz_quadrada(numero):
    if numero < 0:
        return "Erro: Não é possível calcular a raiz quadrada de um número negativo."

    return math.sqrt(numero)

def porcentagem(numero1, numero2):
    """
    Calcula a porcentagem de um número.

    Args:
        numero (float): Número informado pelo usuário.
        percentual (float): Percentual informado pelo usuário.

    Returns:
        float: Porcentagem do número.
    """
    return (numero1 * numero2) / 100