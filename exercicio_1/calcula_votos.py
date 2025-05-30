class CalculaVotos:
    """
        Desenvolvedor: Vitor Henrique Kato
        Data: 29/05/2025
        Calcula os percentuais de votos válidos, votos brancos e votos nulos em relação ao total de eleitores.
    """

    def __init__(self, total_eleitores: int = 0, votos_validos: int = 0, votos_brancos: int = 0,
                 votos_nulos: int = 0) -> None:
        """
        :param total_eleitores: número total de eleitores.
        :param votos_validos: número de votos válidos.
        :param votos_brancos: número de votos em branco.
        :param votos_nulos: número de votos nulos.
        """
        self.total_eleitores = total_eleitores
        self.votos_validos = votos_validos
        self.votos_brancos = votos_brancos
        self.votos_nulos = votos_nulos

    def calcula_percentuais(self) -> dict[str, float]:
        """
        Calcula os percentuais de votos válidos, votos brancos e votos nulos em relação ao total de eleitores.

        :return: Dicionário com os percentuais de cada tipo de voto.
        """
        if self.total_eleitores == 0:
            return {
                "validos": 0.0,
                "brancos": 0.0,
                "nulos": 0.0
            }

        percentual_validos = (self.votos_validos / self.total_eleitores) * 100
        percentual_brancos = (self.votos_brancos / self.total_eleitores) * 100
        percentual_nulos = (self.votos_nulos / self.total_eleitores) * 100

        return {
            "validos": round(percentual_validos, 2),
            "brancos": round(percentual_brancos, 2),
            "nulos": round(percentual_nulos, 2)
        }
