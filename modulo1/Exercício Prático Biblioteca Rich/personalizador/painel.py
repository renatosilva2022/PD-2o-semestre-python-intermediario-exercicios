from rich.panel import Panel

def mostrar_painel(texto, is_arquivo=False):
    if is_arquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    panel = Panel(texto)
    print(panel)

def outro_painel(texto, is_arquivo=False):
    if is_arquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    panel = Panel(texto, title="Painel Exemplo", subtitle="Rodapé")
    print(panel)
