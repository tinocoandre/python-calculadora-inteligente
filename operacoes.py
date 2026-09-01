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
    """
    Função para dividir dois numeros

    Args:
        numero1 (float): O primeiro número
        numero2 (float): O segundo número

    Returns:
        float: A divisão entre dois números
    """
    return numero1 / numero2

def potenciacao(base, expoente):
    if abs(expoente) > 100:
        return "Erro: o expoente deve estar entre -100 e 100."

    try:
        return base ** expoente
    except OverflowError:
        return "Erro: resultado muito grande."

def raiz_quadrada(numero):

    """
    Calcula a raiz quadrada de um número.

    Args:
        numero (float): Número informado pelo usuário.

    Returns:
        float | str: Raiz quadrada do número ou mensagem de erro.
    """
    if numero < 0:
        return "Erro: não existe raiz real de número negativo"

    return math.sqrt(numero)