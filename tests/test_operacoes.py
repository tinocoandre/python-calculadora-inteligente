from operacoes import (somar, subtrair, multiplicar, dividir, potenciacao, raiz_quadrada, porcentagem)

def test_somar():
    assert somar(10, 5) == 15

def test_subtrair():
    assert subtrair(10, 5) == 5

def test_multiplicar():
    assert multiplicar(10, 5) == 50

def test_dividir():
    assert dividir(10, 5) == 2

def test_dividir_por_zero():
    resultado = dividir(10, 0)
    assert resultado == "Erro: Divisão por zero não é permitida."

def test_potenciacao():
    assert potenciacao(2, 3) == 8

def test_raiz_quadrada():
    assert raiz_quadrada(25) == 5

def test_raiz_quadrada_negativa():
    resultado = raiz_quadrada(-25)
    assert resultado == "Erro: Não é possível calcular a raiz quadrada de um número negativo."

def test_raiz_quadrada_zero():
    assert raiz_quadrada(0) == 0

def test_somar_negativos():
    assert somar(-10, -5) == -15

def test_subtrair_negativos():
    assert subtrair(-10, -5) == -5

def test_multiplicar_negativos():
    assert multiplicar(-10, 5) == -50

def test_somar_decimais():
    assert somar(2.5, 2.5) == 5.0

def test_multiplicar_decimais():
    assert multiplicar(2.5, 4) == 10.0

def test_dividir_decimais():
    assert dividir(7.5, 2.5) == 3.0

def test_potenciacao_zero():
    assert potenciacao(10, 0) == 1

def test_potenciacao_negativo():
    assert potenciacao(2, -2) == 0.25

def test_porcentagem():
    assert porcentagem (200, 10) == 20