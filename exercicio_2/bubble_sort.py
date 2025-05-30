"""
    Desenvolvedor: Vitor Henrique Kato
    Data: 29/05/2025
    Ordena uma lista de inteiros usando o algoritmo Bubble Sort.
"""
from typing import List


def bubble_sort(lista: List[int]) -> List[int]:
    """
    Ordena uma lista de inteiros usando o algoritmo Bubble Sort.

    :param lista: Lista de inteiros a ser ordenada.
    :return: Nova lista ordenada em ordem crescente.
    """
    tamanho = len(lista)
    lista_ordenada = lista.copy()

    for i in range(tamanho):
        for j in range(0, tamanho - i - 1):
            if lista_ordenada[j] > lista_ordenada[j + 1]:
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]

    return lista_ordenada