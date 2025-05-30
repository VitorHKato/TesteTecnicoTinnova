"""
    Desenvolvedor: Vitor Henrique Kato
    Data: 29/05/2025
    Descrição: Arquivo main com chamadas para classes que devolvam as respostas dos exercícios.
"""
from exercicio_1.calcula_votos import CalculaVotos


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
    pass


if __name__ == "__main__":
    # Chamada para o exercício 1
    exercicio_1()

    # Chamada para o exercício 2
    exercicio_2()