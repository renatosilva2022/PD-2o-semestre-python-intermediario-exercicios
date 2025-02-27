import argparse
from personalizador import layout, painel, progresso, estilo

def main():
    parser = argparse.ArgumentParser(description='Personalizador com rich')
    parser.add_argument('texto', type=str, help='Texto ou nome do arquivo para impressão formatada')
    parser.add_argument('-a', '--arquivo', action='store_true', help='Indica se o argumento é o caminho para um arquivo')
    parser.add_argument('-m', '--modulo', type=str, choices=['layout', 'painel', 'progresso', 'estilo'], required=True, help='Módulo para acessar')
    parser.add_argument('-f', '--funcao', type=str, choices=['mostrar_layout', 'outro_layout', 'mostrar_painel', 'outro_painel', 'mostrar_progresso', 'outro_progresso', 'mostrar_estilo', 'outro_estilo'], required=True, help='Função do módulo para acessar')

    args = parser.parse_args()

    modulo = globals()[args.modulo]
    funcao = getattr(modulo, args.funcao)
    funcao(args.texto, args.arquivo)

if __name__ == "__main__":
    main()
