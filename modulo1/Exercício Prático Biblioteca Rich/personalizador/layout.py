from rich.layout import Layout

def mostrar_layout(texto, is_arquivo=False):
    if is_arquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    layout = Layout(name="example")
    layout.update(texto)
    print(layout)

def outro_layout(texto, is_arquivo=False):
    if is_arquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
        Layout(name="footer", size=3)
    )
    layout["main"].update(texto)
    print(layout)
