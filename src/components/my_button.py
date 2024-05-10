from tkinter import DISABLED, NORMAL

from customtkinter import CTkButton


def my_button(
    master,
    text: str,
    onClick,
    kind: str = 'PRIMARY',
    width: int = 140,
    state: str = NORMAL,
):
    """Cria um botão personalizado com o texto e função onClick fornecidos.

    Args:
        master (Tkinter.Widget): O widget pai do botão.
        texto (str): O texto a ser exibido no botão.
        onClick (function): A função a ser chamada quando o botão for clicado.
        tipo (str, optional): O tipo de botão a ser criado. Pode ser 'PRIMARY', 'SUCCESS', 'INFO', 'WARNING' ou 'DANGER'. Padrão é 'PRIMARY'.
        largura (int, optional): A largura do botão em pixels. Padrão é 140.
        estado (str, optional): O estado do botão. Pode ser 'NORMAL' ou 'DISABLED'. Padrão é 'NORMAL'.

    Returns:
        CTkButton: O botão criado.
    """

    # Define a cor e a cor de destaque do botão com base no tipo fornecido.
    if kind == 'DANGER':
        button_color = '#dc3545'
        hover_color = '#ab2322'
    elif kind == 'SUCCESS':
        button_color = '#28a745'
        hover_color = '#1e7e34'
    elif kind == 'INFO':
        button_color = '#17a2b8'
        hover_color = '#138496'
    elif kind == 'WARNING':
        button_color = '#ffc107'
        hover_color = '#e0a800'
    else:  # kind == 'PRIMARY'
        button_color = '#3273dc'
        hover_color = '#285eac'

    # Cria o botão
    button = CTkButton(
        master,
        text=text,
        command=onClick,
        fg_color=button_color,
        hover_color=hover_color,
        width=width,
        state=state,
    )

    return button
