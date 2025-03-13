# cartoes_amarelos.py
def calcular_cartoes_amarelos(wc):
    # Função para contar cartões
    def contar_cartoes(observacao):
        if pd.isna(observacao):
            return 0
        return len(observacao.split("|"))

    # Aplicando a função às colunas
    wc["num_cartoes_1"] = wc["cartao_amarelo_1"].apply(contar_cartoes)
    wc["num_cartoes_2"] = wc["cartao_amarelo_2"].apply(contar_cartoes)

    # Somando cartões por país
    cartoes_time1 = wc.groupby("time_1")["num_cartoes_1"].sum().reset_index(name="cartoes_amarelos")
    cartoes_time2 = wc.groupby("time_2")["num_cartoes_2"].sum().reset_index(name="cartoes_amarelos")

    # Combinando os resultados
    cartoes = pd.concat([cartoes_time1, cartoes_time2], ignore_index=True)
    cartoes = cartoes.groupby("time_1").sum().reset_index().rename(columns={"time_1": "país"})

    # Ordenando pelo total de cartões
    cartoes = cartoes.sort_values("cartoes_amarelos", ascending=False)
    return cartoes