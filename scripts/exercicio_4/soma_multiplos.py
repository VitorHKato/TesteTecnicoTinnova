"""
    Desenvolvedor: Vitor Henrique Kato
    Data: 30/05/2025
    Calcula a soma dos múltiplos de 3 e 5 até um número x.
"""

def soma_multiplos(x: int) -> int:
    """
    Calcula a soma dos múltiplos de 3 e 5 até um número x.

    :param x: Número até o qual calcular a soma dos múltiplos.
    :return: Soma dos múltiplos de 3 e 5 até x.
    :raises ValueError: Se x for menor que 0.
    """
    if x < 0:
        raise ValueError("O número deve ser maior ou igual a zero.")

    soma = 0
    for i in range(x + 1):
        if i % 3 == 0 or i % 5 == 0:
            soma += i

    return soma