import tkinter as tk
from tkinter.ttk import Treeview

janela = tk.Tk()

class Interface:
    def __init__(self):
        self.janela = janela
        self.janela.geometry('300x200')
        self.janela.resizable(False, False)
        self.janela.title('Biblioteca interface')




