# main.py
from carregar_dados import carregar_dados
from analise_audiencia import jogo_maior_audiencia
from contagem_copas import contar_copas
from participacao_paises import calcular_participacao
from total_gols import calcular_total_gols
from cartoes_amarelos import calcular_cartoes_amarelos
from top_jogadores import calcular_top_jogadores

def main():
    # Carregar os dados
    wc = carregar_dados()

    # Análise de audiência
    print("Jogo com maior audiência:")
    print(jogo_maior_audiencia(wc))

    # Contagem de Copas
    print("\nQuantidade de Copas:")
    print(contar_copas(wc))

    # Participação dos países
    print("\nTop 5 países por participação:")
    participacao = calcular_participacao(wc)
    print("Feminina:")
    print(participacao["top5_feminina"])
    print("Masculina:")
    print(participacao["top5_masculina"])

    # Total de gols por país
    print("\nTotal de gols por país:")
    print(calcular_total_gols(wc))

    # Cartões amarelos por país
    print("\nCartões amarelos por país:")
    print(calcular_cartoes_amarelos(wc))

    # Top 10 jogadores com mais gols
    print("\nTop 10 jogadores com mais gols:")
    print(calcular_top_jogadores(wc))

if __name__ == "__main__":
    main()