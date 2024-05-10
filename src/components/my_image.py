from customtkinter import CTkImage, CTkLabel


def my_image(master, image: CTkImage):
    """Cria um CTkLabel com a imagem fornecida.

    Args:
        master (Tkinter.Widget): O widget pai do CTkLabel.
        image (CTkImage): A imagem a ser exibida no CTkLabel.

    Returns:
        CTkLabel: O CTkLabel criado.
    """
    return CTkLabel(master, image=image)
