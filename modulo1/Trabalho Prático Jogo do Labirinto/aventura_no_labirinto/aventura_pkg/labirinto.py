def criar_labirinto(dificuldade='facil'):
    """
    Cria um labirinto com base na dificuldade escolhida.
    
    :param dificuldade: Nível de dificuldade do labirinto ('facil', 'medio', 'dificil')
    :return: Labirinto representado como uma lista de listas
    """
    if dificuldade == 'facil':
        return [
            ['#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', '#'],
            ['#', '#', '#', '#', '#']
        ]
    elif dificuldade == 'medio':
        return [
            ['#', '#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', '#', ' ', '#'],
            ['#', ' ', ' ', '#', ' ', '#'],
            ['#', '#', '#', '#', '#', '#']
        ]
    elif dificuldade == 'dificil':
        return [
            ['#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', '#', ' ', '#'],
            ['#', ' ', '#', ' ', '#', ' ', '#'],
            ['#', ' ', '#', ' ', ' ', ' ', '#'],
            ['#', '#', '#', '#', '#', '#', '#']
        ]

def imprimir_labirinto(labirinto, jogador_pos):
    """
    Imprime o labirinto com o jogador na posição atual.
    
    :param labirinto: Labirinto representado como uma lista de listas
    :param jogador_pos: Posição do jogador (x, y)
    """
    for i, linha in enumerate(labirinto):
        for j, celula in enumerate(linha):
            if (i, j) == jogador_pos:
                print('P', end=' ')
            else:
                print(celula, end=' ')
        print()