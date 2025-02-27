from rich.progress import Progress

def mostrar_progresso(texto, is_arquivo=False):
    if is_arquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    with Progress() as progress:
        task1 = progress.add_task(texto, total=100)
        while not progress.finished:
            progress.update(task1, advance=1)

def outro_progresso(texto, is_arquivo=False):
    if is_arquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    with Progress() as progress:
        task1 = progress.add_task(texto, total=50)
        while not progress.finished:
            progress.update(task1, advance=1)
