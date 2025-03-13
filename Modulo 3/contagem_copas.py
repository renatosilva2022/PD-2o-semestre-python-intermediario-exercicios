# contagem_copas.py
def contar_copas(wc):
    contagem_copas = wc["copa"].value_counts()
    return {
        "Masculina": contagem_copas.get("Masculina", 0),
        "Feminina": contagem_copas.get("Feminina", 0)
    }