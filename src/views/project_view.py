import os
import threading

from customtkinter import CTkFrame, CTkTextbox, CTkProgressBar
from tkinter import LEFT, BOTH, TOP, RIGHT, DISABLED, NORMAL, BOTTOM


from src.components.my_button import my_button
from src.components.my_directory_tree import MyDirectoryTree
from src.components.my_code_text_box import MyCodeTextBox

from src.services.gemini.chat_gemini import chat_gemini
from src.services.gemini.gemini_improve_code import gemini_improve_code
from src.services.gemini.gemini_add_comments import gemini_add_comments

ignore = [
    '.venv',
    '.git',
    '.vscode',
    '__pycache__',
    '.env'
]

class ProjectView(CTkFrame):
    def __init__(self, *args, app, **kwargs):
        self.nodes = dict()
        self.app = app
        self.chat = chat_gemini()
        self.code_selected = None
        super().__init__(*args, **kwargs)
        self.__layout()
        

    def handler_open_file(self):
        # Função para abrir um arquivo
        self.show_progress_bar()
        curItem = self.tree.focus()
        file_path = self.tree.objects_path.get(curItem)
        if file_path and os.path.isfile(file_path):
            self.code_selected = file_path
            self.file_area.delete('1.0', 'end')
            try:
                with open(file_path, "r") as file:
                    text = file.read()
                    self.file_area.insert(0.0, text)
                    self.file_area.change_color()
            except FileNotFoundError:
                print(f"Erro: Arquivo '{file_path}' não encontrado.")
        else:
            self.app.message_dialog('error', 'select a file!')
        self.hide_progress_bar()

    def hide_progress_bar(self):
        # Função para esconder a barra de progresso
        self.progress.stop()
        self.progress.pack_forget()
        text = self.file_area.get("0.0", "end")
        self.button1.configure(state=NORMAL)

        # Configura os botões de acordo com o conteúdo do arquivo
        buttons = [self.button2, self.button3]
        for button in buttons:
            button.configure(state=NORMAL if text != '' else DISABLED)

        self.buttonSave.configure(state=NORMAL if self.code_selected and self.code_selected != '' else DISABLED)


    def disabled_buttons(self):
        buttons = [self.button1, self.button2, self.button3, self.buttonSave]
        for button in buttons:
            button.configure(state=DISABLED)

    def show_progress_bar(self):
        # Função para mostrar a barra de progresso
        self.disabled_buttons()

        self.progress.pack(side=RIGHT, padx=10, pady=10)
        self.progress.start()

    def __inprove_code(self):
        # Função para melhorar o código

        # Obtém o código do arquivo
        code = self.file_area.get("0.0", "end")

        # Define a função de callback para atualizar a área de texto com o código melhorado
        def callback_file_area(text, status):
            self.file_return_area.delete('1.0', 'end')
            self.file_return_area.insert('end', text)
            if status == 'FINISH':
                self.hide_progress_bar()

        # Chama o serviço do AI Gemini para melhorar o código
        gemini_improve_code(code, self.chat, callback_file_area)

    def create_thread(self, target):
        t = threading.Thread(target=target, daemon=True)
        t.start()

    def handler_improve_code(self):
        # Função para chamar o serviço de melhoria de código
        self.show_progress_bar()
        self.create_thread(self.__inprove_code)

         
    def handler_add_comments(self):
        # Função para chamar o serviço de adição de comentários
        self.show_progress_bar()
        self.create_thread(self.__add_comments)

    def __add_comments(self):
        # Função para adicionar comentários ao código

         # Obtém o código do arquivo
        code = self.file_area.get("0.0", "end")

        # Define a função de callback para atualizar a área de texto com o código comentado
        def callback_file_area(text, status):
            self.file_return_area.delete('1.0', 'end')
            self.file_return_area.insert('end', text)
            if status == 'FINISH':
                self.hide_progress_bar()

        # Chama o serviço Gemini AI para adicionar comentários ao código
        gemini_add_comments(code, self.chat, callback_file_area)
        

    def __createTopArea(self):
        # Função para criar a área superior

        # Cria o botão para abrir o arquivo
        self.button1 = my_button(self.area0, 'Open File', self.handler_open_file)
        self.button1.pack(side=LEFT, padx=10, pady=10)

        # Cria o botão para melhorar o código
        self.button2 = my_button(self.area0, 'Improve my code', self.handler_improve_code, state=DISABLED)
        self.button2.pack(side=LEFT, padx=10, pady=10)

        # Cria a barra de progresso
        self.button3 = my_button(self.area0, 'Add Comments', self.handler_improve_code, state=DISABLED)
        self.button3.pack(side=LEFT, padx=10, pady=10)

        self.progress = CTkProgressBar(self.area0, orientation="horizontal", width=1255)
        self.progress.configure(mode="indeterminate")

    def __createTreeView(self):
        # Função para criar a árvore de diretórios

        self.tree = MyDirectoryTree(self.area1, directory=self.app.paths.project_folder, app=self.app, ignore=ignore)
        self.tree.pack(expand=True, fill=BOTH, padx=10, pady=10)
        
    def handler_save_file(self):
        # Função para salvar o arquivo

        # Verifica se o arquivo foi selecionado e existe
        if self.code_selected  and os.path.isfile(self.code_selected ):
            # Obtém o código do arquivo
            code = self.file_area.get("0.0", "end")
            try:
                with open(self.code_selected , "w", encoding='utf-8') as file:
                    file.write(code)

            except FileNotFoundError:
                print(f"Erro: Arquivo '{self.code_selected }' não encontrado.")
        else:
            self.app.message_dialog('error', 'file not found!')

    def __createTextArea(self):
        # Função para criar a área de texto
        area1 = CTkFrame(self.area2)
        area1.pack(fill=BOTH, expand=True, side=LEFT, padx=10, pady=10)
        
        area2 = CTkFrame(self.area2)
        area2.pack(fill=BOTH, expand=True,  side=RIGHT, padx=10, pady=10)

        
        self.file_area = MyCodeTextBox(area1, font=("Arial",14))
        self.file_area.pack(expand=True, fill=BOTH)

        area3 = CTkFrame(area1)
        area3.pack(fill=BOTH, side=BOTTOM, padx=10, pady=10)

        # Cria um frame para os botões de salvar
        self.buttonSave = my_button(area3, 'Save File', self.handler_save_file,  kind='SUCCESS', state=DISABLED)
        self.buttonSave.pack(side=LEFT, padx=10, pady=10)

        self.file_return_area = CTkTextbox(area2, font=("Arial",14))
        self.file_return_area.pack(expand=True, fill=BOTH)

    def __layout(self):
        self.area0 = CTkFrame(self)
        self.area0.pack(side=TOP, fill=BOTH)
        self.__createTopArea()

        self.area1 = CTkFrame(self)
        self.area1.pack(side=LEFT, fill=BOTH)
        self.__createTreeView()

        self.area2 = CTkFrame(self)
        self.area2.pack(expand=True, fill=BOTH)
        self.__createTextArea()
