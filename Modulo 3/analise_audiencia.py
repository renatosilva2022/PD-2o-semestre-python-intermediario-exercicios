# analise_audiencia.py
def jogo_maior_audiencia(wc):
    maior_audiencia = wc.sort_values("comparecimento", ascending=False).iloc[0]
    return maior_audiencia