from rich import print

def imprime_instrucoes():
    """
    Imprime as instruções do jogo formatadas.
    """
    print("[bold]Instruções do Jogo:[/bold]")
    print("1. Use as setas do teclado para mover o jogador (P).")
    print("2. Colete todos os itens para ganhar pontos.")
    print("3. Encontre a saída para vencer o jogo.")

def imprime_menu():
    """
    Imprime o menu de opções do jogo.
    """
    print("[bold]Menu:[/bold]")
    print("1. Instruções")
    print("2. Jogar")
    print("3. Sair")