
import os
from customtkinter import CTkFrame, filedialog, CTkLabel, CTkFont, CTkImage
from src.components.my_button import my_button
from src.components.my_image import my_image
from tkinter import BOTH, LEFT
from PIL import Image

class InitView(CTkFrame):
    def __init__(self, *args, app, **kwargs):
        self.app = app
        super().__init__(*args, **kwargs)
        self.layout()

    def handler_open_folder(self):
        # Abre o diálogo para seleção da pasta do projeto
        
        filename = filedialog.askdirectory()
        if filename != '':
            self.app.paths.project_folder = filename
            self.app.change_page('project_view')


    def layout(self):
        area1 = CTkFrame(self)
        area1.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Carrega logo do app
        self.image = CTkImage(
            light_image=Image.open(os.path.join(self.app.paths.imgs, 'logo.png')),
            dark_image=Image.open(os.path.join(self.app.paths.imgs, 'logo.png')),
            size=(400,400)
        )
        # Exibe o logo na tela
        image = my_image(area1, self.image)
        image.pack(fill=BOTH)

         # Cria o título do aplicativo
        label = CTkLabel(area1, text='PyGeminador', font=CTkFont(size=20, weight='bold'))
        label.pack(fill=BOTH)

        label2 = CTkLabel(area1, text='Seu assistente para programar.')
        label2.pack(fill=BOTH)

        # Cria o botão para abrir o projeto
        button = my_button(area1, 'Open your project', self.handler_open_folder)
        button.pack(expand=True)

