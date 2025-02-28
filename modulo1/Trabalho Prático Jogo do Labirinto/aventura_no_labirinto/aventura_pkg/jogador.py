from pynput import keyboard

def iniciar_jogador(labirinto):
    """
    Inicia o jogador na posição inicial do labirinto.
    
    :param labirinto: Labirinto representado como uma lista de listas
    :return: Posição inicial do jogador (x, y)
    """
    for i, linha in enumerate(labirinto):
        for j, celula in enumerate(linha):
            if celula == ' ':
                return (i, j)
    return (0, 0)

def mover(jogador_pos, tecla):
    """
    Move o jogador com base na tecla pressionada.
    
    :param jogador_pos: Posição atual do jogador (x, y)
    :param tecla: Tecla pressionada
    :return: Nova posição do jogador (x, y)
    """
    x, y = jogador_pos
    if tecla == keyboard.Key.up:
        return (x - 1, y)
    elif tecla == keyboard.Key.down:
        return (x + 1, y)
    elif tecla == keyboard.Key.left:
        return (x, y - 1)
    elif tecla == keyboard.Key.right:
        return (x, y + 1)
    return (x, y)

def pontuar(pontuacao, item_coletado):
    """
    Atualiza a pontuação do jogador.
    
    :param pontuacao: Pontuação atual do jogador
    :param item_coletado: Item coletado pelo jogador
    :return: Nova pontuação
    """
    return pontuacao + 10 if item_coletado else pontuacao