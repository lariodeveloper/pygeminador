import os
import re
from tkinter import END

from customtkinter import CTkFrame, CTkLabel, CTkTextbox

from src.components.my_button import my_button

TAGS = {
    'python': {
        'for ': 'blue',
        'def ': 'red',
        'from ': '#470146',
        'if ': '#470146',
        'else': '#470146',
        'try ': '#470146',
        'import ': '#470146',
        'class ': '#0a41f5',

    }
    
}


class MyCodeTextBox(CTkTextbox):
    """Classe que representa uma caixa de texto que realça palavras-chave em Python."""

    def __init__(self, *args, **kwargs):
        super().__init__(
            *args, **kwargs, fg_color='#e6e3da', text_color='black'
        )
        self.bind('<KeyRelease>', self.change_color)
        self.language = 'python'
        self.config_tags()

    def config_tags(self):
        tags = TAGS[self.language]
        for tag in tags:
            self.tag_config(tag, foreground=tags[tag])


    def search_re(self, pattern):

        matches = []
        text = self.get("1.0", END).splitlines()
        for i, line in enumerate(text):
            for match in re.finditer(pattern, line):
                matches.append((f"{i + 1}.{match.start()}", f"{i + 1}.{match.end()}"))
        
        return matches
    
    def change_color(self):
        tags = TAGS[self.language]
        
        # Remove todas as tags de realce existentes
        self.tag_remove(self, '1.0', END) 
        
        # Obtem texto
        text = self.get('1.0', 'end')
        for tag in tags:
            for match in self.search_re(tag):
                self.tag_add(tag, match[0], match[1])

