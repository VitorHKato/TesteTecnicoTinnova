"""
    Desenvolvedor: Vitor Henrique Kato
    Data: 29/05/2025
    Descrição: Arquivo main com chamadas para classes que devolvam as respostas dos exercícios.
"""
from scripts.exercicio_1.calcula_votos import CalculaVotos
from scripts.exercicio_2 import bubble_sort
from scripts.exercicio_3 import fatorial
from scripts.exercicio_4 import soma_multiplos


def exercicio_1() -> None:
    """
    Executa o exercício 1, instanciando a classe CalculadoraDeVotos e exibindo os percentuais.
    """
    votos = CalculaVotos(
        total_eleitores=1000,
        votos_validos=800,
        votos_brancos=150,
        votos_nulos=50
    )

    percentuais = votos.calcula_percentuais()
    print("Percentuais de votos:")
    for tipo, percentual in percentuais.items():
        print(f"{tipo.capitalize()}: {percentual:.2f}%")


def exercicio_2() -> None:
    """
    Executa o exercício 2, ordenando uma lista de inteiros usando o algoritmo Bubble Sort.
    """
    lista = [5, 3, 2, 4, 7, 1, 0, 6]
    print("Lista original:", lista)

    lista_ordenada = bubble_sort.bubble_sort(lista)
    print("Lista ordenada:", lista_ordenada)


def exercicio_3() -> None:
    """
    Executa o exercício 3, calculando o fatorial de um número natural maior ou igual a dois.
    :raises ValueError: Se n for menor que 2.
    """
    try:
        for i in range(2, 7):
            resultado = fatorial.fatorial(i)
            print(f"O fatorial de {i} é: {resultado}")
    except ValueError as e:
        print(e)


def exercicio_4() -> None:
    """
    Executa o exercício 4, calculando a soma dos múltiplos de 3 e 5 até um número x.
    :raises ValueError: Se x for menor que 0.
    """
    try:
        x = 9
        resultado = soma_multiplos.soma_multiplos(x)
        print(f"A soma dos múltiplos de 3 e 5 até {x} é: {resultado}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    # Chamada para o exercício 1
    exercicio_1()

    # Chamada para o exercício 2
    exercicio_2()

    # Chamada para o exercício 3
    exercicio_3()

    # Chamada para o exercício 4
    exercicio_4()