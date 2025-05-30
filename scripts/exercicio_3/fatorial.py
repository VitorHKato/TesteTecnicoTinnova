"""
    Desenvolvedor: Vitor Henrique Kato
    Data: 29/05/2025
    Calcula o fatorial de um número natural maior ou igual a dois.
"""

def fatorial(numero: int) -> int:
    """
    Calcula o fatorial de um número natural maior ou igual a dois.

    :param numero: Número natural maior ou igual a dois.
    :return: Fatorial do número.
    :raises ValueError: Se n for menor que 2.
    """
    if numero < 2:
        raise ValueError("O número deve ser maior ou igual a 2.")

    resultado = 1
    for i in range(2, numero + 1):
        resultado *= i

    return resultado