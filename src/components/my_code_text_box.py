import os
import re
from tkinter import BOTH, BOTTOM, DISABLED, LEFT, NORMAL, RIGHT, TOP

from customtkinter import CTkFrame, CTkLabel, CTkTextbox

from src.components.my_button import my_button

TAGS = {
    'for': 'blue',
    'def': 'red',
    'from': '#43026b',
}


class MyCodeTextBox(CTkTextbox):
    """Classe que representa uma caixa de texto que realça palavras-chave em Python."""

    def __init__(self, *args, **kwargs):
        super().__init__(
            *args, **kwargs, fg_color='#e6e3da', text_color='black'
        )
        self.bind('<KeyRelease>', self.change_color)
        for tag in TAGS:
            self.tag_config(tag, foreground=TAGS[tag])

    def change_color(self, key=None):
        # Obt�m o texto da caixa de texto
        text = self.get('1.0', 'end')

        # Encontra as ocorr�ncias de palavras-chave usando express�es regulares
        matches = re.finditer(
            r'\b({})\s+|'.format('|'.join(TAGS.keys())), text
        )

        # Remove todas as tags de realce existentes
        self.tag_remove(
            self, '1.0', 'end'
        )  # Clear all existing tags efficiently

        # Aplica as tags de realce correspondentes �s ocorr�ncias de palavras-chave
        # for match in matches:
        # start, end = str(match.start()), str(match.end())
        # print(f"Match: {text[int(start):int(end)]}, Start: {start}, End: {end}")  # Added debugging print
        # self.tag_add(TAGS[match.group(1)], start, end)
