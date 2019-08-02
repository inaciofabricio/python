# -*- coding: utf-8 -*-

import tkinter as tk

janela = tk.Tk()

janela.title("Janela Principal")
janela["bg"] = "green" #ou janela["background"] = "green"

#largura X altura + ditancia esquerda + distancia Top
janela.geometry("500x300+100+100")


janela.mainloop()

