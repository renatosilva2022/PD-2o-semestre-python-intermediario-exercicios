from rich.console import Console

def mostrar_estilo(texto, is_arquivo=False):
    if is_arquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    console = Console()
    console.print(texto, style="bold red")

def outro_estilo(texto, is_arquivo=False):
    if is_arquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    console = Console()
    console.print(texto, style="italic green")
