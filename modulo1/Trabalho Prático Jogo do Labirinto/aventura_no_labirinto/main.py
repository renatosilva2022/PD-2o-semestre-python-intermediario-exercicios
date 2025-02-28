import argparse
from aventura_pkg.labirinto import criar_labirinto, imprimir_labirinto
from aventura_pkg.jogador import iniciar_jogador, mover, pontuar
from aventura_pkg.utils import imprime_instrucoes, imprime_menu
from pynput import keyboard

def main():
    parser = argparse.ArgumentParser(description="Aventura no Labirinto")
    parser.add_argument('--name', type=str, required=True, help="Nome do jogador")
    parser.add_argument('--color', type=str, default="blue", help="Cor principal do jogo")
    parser.add_argument('--dificuldade', type=str, default="facil", help="Dificuldade do labirinto")
    parser.add_argument('--disable-sound', action='store_true', help="Desativar som")
    args = parser.parse_args()

    print(f"Bem-vindo, {args.name}! Vamos começar a aventura no labirinto.")
    imprime_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        imprime_instrucoes()
    elif opcao == '2':
        labirinto = criar_labirinto(args.dificuldade)
        jogador_pos = iniciar_jogador(labirinto)
        pontuacao = 0

        def on_press(key):
            nonlocal jogador_pos, pontuacao
            nova_pos = mover(jogador_pos, key)
            x, y = nova_pos
            if labirinto[x][y] != '#':
                jogador_pos = nova_pos
                if labirinto[x][y] == '*':
                    pontuacao = pontuar(pontuacao, True)
                    labirinto[x][y] = ' '
                imprimir_labirinto(labirinto, jogador_pos)
                print(f"Pontuação: {pontuacao}")

        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

if __name__ == "__main__":
    main()