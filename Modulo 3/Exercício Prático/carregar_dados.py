# carregar_dados.py
import pandas as pd

def carregar_dados():
    # Carregando os dados dos arquivos locais
    df1 = pd.read_csv("matches_1930_2022.csv")
    df2 = pd.read_csv("matches_1991_2023.csv")

    # Combinando os dataframes
    wc = pd.concat([df1, df2], ignore_index=True)

    # Renomeando as colunas
    wc.columns = [
        "time_1", "time_2", "gols_1", "gols_2", "data", "ano", "país_sede", "comparecimento",
        "resultado", "rodada", "gols_1_detalhes", "gols_2_detalhes", "gols_1_contra",
        "gols_2_contra", "gols_1_penalti", "gols_2_penalti", "cartao_vermelho_1",
        "cartao_vermelho_2", "cartao_amarelo_1", "cartao_amarelo_2", "copa"
    ]

    # Convertendo os tipos das colunas
    wc["data"] = pd.to_datetime(wc["data"])
    wc["rodada"] = wc["rodada"].astype("category")

    # Salvando o dataframe formatado
    wc.to_csv("wc_formatado.csv", index=False)

    return wc