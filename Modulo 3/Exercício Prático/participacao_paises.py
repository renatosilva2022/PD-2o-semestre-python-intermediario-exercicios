# participacao_paises.py
def calcular_participacao(wc):
    # Criando listas de países participantes
    paises_time1 = wc[["time_1", "copa"]].rename(columns={"time_1": "país"})
    paises_time2 = wc[["time_2", "copa"]].rename(columns={"time_2": "país"})

    # Concatenando as listas
    participacao = pd.concat([paises_time1, paises_time2], ignore_index=True)

    # Contando a participação de cada país
    participacao = participacao.groupby(["país", "copa"]).size().reset_index(name="num_copas")

    # Exibindo os top 5 de cada competição
    top5_feminina = participacao[participacao["copa"] == "Feminina"].sort_values("num_copas", ascending=False).head(5)
    top5_masculina = participacao[participacao["copa"] == "Masculina"].sort_values("num_copas", ascending=False).head(5)

    return {
        "top5_feminina": top5_feminina,
        "top5_masculina": top5_masculina
    }