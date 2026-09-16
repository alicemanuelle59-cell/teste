import tkinter as tk
from tkinter.ttk import Treeview

janela = tk.Tk()
class Functions:
    def limpa_tela(self):
        self.codigo_entrada.delete(0,tk.END)
        self.nome_entrada.delete(0,tk.END)
        self.telefone_entrada.delete(0,tk.END)
        self.cidade_entrada.delete(0,tk.END)
class Aplication(Functions):
    def __init__(self,janela):
        self.janela = janela
        self.frame_tela()
        self.entrar_frame1()
        self.buttons_frame1()
        self.lista()
        self.tela()
        self.janela.mainloop()
    def tela(self):
        self.janela.title("Tela de cadastro")
        self.janela.geometry("1080x720")
        self.janela.maxsize(1080,720)
        self.janela.minsize(720,460)
        self.janela.configure(background= "#83AB82")
    def frame_tela(self):
        self.frame1 = tk.Frame(self.janela)
        self.frame1.configure(bg="lightblue", bd=0.5,highlightbackground="blue",highlightthickness=5)
        self.frame1.place(relheight=0.475, relwidth=0.97, relx=0.015, rely=0.012)
        self.frame2 = tk.Frame(self.janela)
        self.frame2.configure(bg="lightblue", bd=0.5,highlightbackground="black",highlightthickness=5)
        self.frame2.place(relheight=0.475, relwidth=0.97, relx=0.015, rely=0.51)
    def buttons_frame1(self):
        self.limpar = tk.Button(self.frame1, text="Limpar", font=("Arial", 14, "bold"), command= self.limpa_tela)
        self.limpar.place(relheight=0.107, relwidth=0.101, relx=0.21, rely= 0.07)
        self.limpar.configure(background="#050B3B", foreground="white")
        self.buscar = tk.Button(self.frame1, text="Buscar", font=("Arial", 14, "bold"))
        self.buscar.place(relheight=0.107, relwidth=0.101, relx=0.31, rely= 0.07)
        self.buscar.configure(background="#050B3B", foreground="white")
        self.apagar = tk.Button(self.frame1, text="Apagar", font=("Arial", 14, "bold"))
        self.apagar.place(relheight=0.107, relwidth=0.101, relx=0.6, rely= 0.07)
        self.apagar.configure(background="#050B3B", foreground="white")
        self.novo = tk.Button(self.frame1, text="Novo", font=("Arial", 14, "bold"))
        self.novo.place(relheight=0.107, relwidth=0.101, relx=0.7, rely= 0.07)
        self.novo.configure(background="#050B3B", foreground="white")
        self.alterar = tk.Button(self.frame1, text="Alterar", font=("Arial", 14, "bold"))
        self.alterar.place(relheight=0.107, relwidth=0.101, relx=0.8, rely= 0.07)
        self.alterar.configure(background="#050B3B", foreground="white")
    def entrar_frame1(self):
        self.codigo = tk.Label(self.frame1,text="Codigo", font=("Arial", 14, "bold"), bg="lightblue")
        self.codigo.place(relheight=0.107, relwidth=0.101, relx=0.05, rely=0.031)
        self.codigo_entrada = tk.Entry(self.frame1, width=45)
        self.codigo_entrada.place(relheight=0.100, relwidth=0.098, relx=0.05, rely=0.15)
        self.nome = tk.Label(self.frame1,text="Nome", font=("Arial", 14, "bold"), bg="lightblue")
        self.nome.place(relheight=0.107, relwidth=0.101, relx=0.05, rely=0.3)
        self.nome_entrada = tk.Entry(self.frame1, width=45)
        self.nome_entrada.place(relheight=0.1, relwidth=0.64, relx=0.17, rely=0.3)
        self.telefone = tk.Label(self.frame1,text="Telefone", font=("Arial", 14, "bold"), bg="lightblue")
        self.telefone.place(relheight=0.107, relwidth=0.101, relx=0.062, rely=0.54)
        self.telefone_entrada = tk.Entry(self.frame1, width=45)
        self.telefone_entrada.place(relheight=0.1, relwidth=0.29, relx=0.17, rely=0.54)
        self.cidade = tk.Label(self.frame1,text="Cidade", font=("Arial", 14, "bold"), bg="lightblue")
        self.cidade.place(relheight=0.107, relwidth=0.101, relx=0.057, rely=0.78)
        self.cidade_entrada = tk.Entry(self.frame1, width=45)
        self.cidade_entrada.place(relheight=0.1, relwidth=0.29, relx=0.17, rely=0.78)
    def lista(self):

        self.lista_frame2=Treeview(self.frame2, height=3, columns=("col1", "col2", "col3", "col4"))
        self.lista_frame2.heading("#0", text="")
        self.lista_frame2.heading("#1", text="Codigo")
        self.lista_frame2.heading("#2", text="Nome")
        self.lista_frame2.heading("#3", text="Telefone")
        self.lista_frame2.heading("#4", text="Cidade")

        self.lista_frame2.column("#0", width=1)
        self.lista_frame2.column("#1", width= 100)
        self.lista_frame2.column("#2", width=270)
        self.lista_frame2.column("#3", width=215)
        self.lista_frame2.column("#4", width=215)
        self.lista_frame2.place(relheight=0.92, relwidth=0.96, relx=0.012, rely=0.05)

        self.scroll_lista_frame2 = tk.Scrollbar(self.frame2, orient="vertical")
        self.scroll_lista_frame2.configure(command=self.lista_frame2.yview)
        self.scroll_lista_frame2.place(relheight=0.92, relwidth=0.028, relx=0.97, rely=0.05)

Aplication(janela)