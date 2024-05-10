import os
from tkinter import BOTH, BOTTOM, DISABLED, LEFT, NORMAL, RIGHT, TOP

from customtkinter import CTkFrame, CTkLabel, CTkToplevel

from src.components.my_button import my_button


class MyMessageDialog(CTkToplevel):
    def handlerClose(self):
        self.destroy()

    def __createTopArea(self):
        button = my_button(self.area0, 'Open File', self.handlerOpenFile)
        button.pack(side=LEFT, padx=10, pady=10)

    def __appearance_setting(self, title):

        self.title(title)
        self.resizable(width=False, height=False)
        self.iconbitmap(os.path.join(self.app.paths.imgs, 'logo.ico'))
        self.geometry(f'{250}x{150}')
        self.wm_transient(self.app)

    def __init__(self, *args, title: str, text: str, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = args[0]
        self.__appearance_setting(title)
        area = CTkFrame(self)
        area.pack(fill=BOTH, expand=True, padx=10, pady=10)

        area1 = CTkFrame(
            area,
        )
        area1.pack(fill=BOTH, expand=True, padx=10, pady=10)

        area2 = CTkFrame(
            area,
        )
        area2.pack(fill=BOTH, expand=True, side=BOTTOM, padx=10, pady=10)

        self.label = CTkLabel(area1, text=text)
        self.label.pack(padx=20, pady=20)

        button = my_button(area2, 'Close', self.handlerClose, kind='DANGER')
        button.pack(side=LEFT)
