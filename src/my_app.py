import os
from pathlib import Path
from tkinter import BOTH, Menu

from customtkinter import (
    CTk,
    CTkFrame,
    filedialog,
    set_appearance_mode,
    set_default_color_theme,
)
from dotenv import load_dotenv

from src.components.my_message_dialog import MyMessageDialog
from src.utils.my_paths import MyPaths
from src.views.init_view import InitView
from src.views.project_view import ProjectView

# Define o tema escuro
set_appearance_mode('dark')
set_default_color_theme('dark-blue')

# Define o diretório base
BASE_DIR = Path(__file__).resolve().parent.parent

# Carrega o arquivo .env se existir
dotenv_path = os.path.join(BASE_DIR, '.env')
if os.path.isfile(dotenv_path):
    load_dotenv(dotenv_path)

# Classe principal da aplicação
class MyApp(CTk):
    def __init__(self, *args, **kwargs):
        # Inicializa a classe pai
        super().__init__(*args, **kwargs)

        # Define os caminhos
        self.paths = MyPaths(BASE_DIR)

        # Define as configurações da janela
        self.title('PyGeminador')
        self.iconbitmap(os.path.join(self.paths.imgs, 'logo.ico'))

        # Cria uma janela secundária para mensagens
        self.toplevel_window = None

        # Cria o menu da aplicação
        self.create_menu()

        self.main_frame = CTkFrame(self)
        self.main_frame.pack(expand=True, fill=BOTH)

        self.change_page('init_view')

    def handlerOpenFolder(self):
        # Abre uma janela de seleção de pasta
        filename = filedialog.askdirectory()
        if filename != '':
            self.paths.project_folder = filename
            self.change_page('project_view')

    def create_menu(self):
        # Cria o menu da aplica��o
        menu = Menu(self)
        menu_project = Menu(menu, tearoff=0)

        menu_project_open_folder = Menu(menu_project, tearoff=0)
        menu_project_open_folder.add_command(
            label='Open your project', command=self.handlerOpenFolder
        )
        menu_project.add_cascade(
            label='Projects', menu=menu_project_open_folder
        )

        menu.add_cascade(label='Projects', menu=menu_project)

        self.config(menu=menu)

    def change_page(self, page):
        # Altera a p�gina exibida

        # Destr�i todos os widgets do frame principal
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        if page == 'project_view':
            self.geometry(f'{1600}x{800}')
            self.view = ProjectView(self.main_frame, app=self)
        else:
            self.view = InitView(self.main_frame, app=self)

        self.view.pack(expand=True, fill=BOTH)

    def message_dialog(self, title: str, text: str):
        # Exibe uma mensagem na janela secund�ria
        if (
            self.toplevel_window is None
            or not self.toplevel_window.winfo_exists()
        ):
            self.toplevel_window = MyMessageDialog(
                self, title=title, text=text
            )
        else:
            self.toplevel_window.focus()

