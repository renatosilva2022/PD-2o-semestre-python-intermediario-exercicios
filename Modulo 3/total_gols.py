# total_gols.py
def calcular_total_gols(wc):
    # Somando gols de cada time
    gols_time1 = wc.groupby("time_1")["gols_1"].sum().reset_index(name="total_gols")
    gols_time2 = wc.groupby("time_2")["gols_2"].sum().reset_index(name="total_gols")

    # Combinando os resultados
    gols = pd.concat([gols_time1, gols_time2], ignore_index=True)
    gols = gols.groupby("time_1").sum().reset_index().rename(columns={"time_1": "país"})

    # Ordenando pelo total de gols
    gols = gols.sort_values("total_gols", ascending=False)
    return gols