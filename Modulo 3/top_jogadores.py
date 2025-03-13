# top_jogadores.py
def calcular_top_jogadores(wc):
    # Função para extrair jogadores e contar gols
    def extrair_gols(observacao):
        if pd.isna(observacao):
            return []
        return [gol.split("·")[0].strip() for gol in observacao.split("|")]

    # Criando um dicionário para contar gols
    gols_jogadores = {}

    # Processando as colunas de gols
    for col in ["gols_1_detalhes", "gols_2_detalhes", "gols_1_penalti", "gols_2_penalti"]:
        for observacao in wc[col]:
            jogadores = extrair_gols(observacao)
            for jogador in jogadores:
                gols_jogadores[jogador] = gols_jogadores.get(jogador, 0) + 1

    # Convertendo o dicionário em dataframe
    top10_jogadores = pd.DataFrame(list(gols_jogadores.items()), columns=["jogador(a)", "num_gols"])
    top10_jogadores = top10_jogadores.sort_values("num_gols", ascending=False).head(10)
    return top10_jogadores