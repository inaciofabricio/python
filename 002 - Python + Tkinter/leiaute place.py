# -*- coding: utf-8 -*-

from tkinter import *
from random import randint

janela = Tk()

def bt_click():

    inicio = int(input1.get())
    fim = int(input2.get())

    num = randint(inicio, fim)
    lb2["text"] = num

titulo = Label(janela, text = "Sorteio")
titulo.place(x=100, y=10)

lb1 = Label(janela, text = "Inicio")
lb1.place(x=5, y=50)

input1 = Entry(janela, width=10)
input1.place(x=60,y=50)

lb1 = Label(janela, text = "Fim")
lb1.place(x=5, y=80)

input2 = Entry(janela, width=10)
input2.place(x=60,y=80)


bt = Button(janela, width=20, text="OK", command=bt_click)
bt.place(x=75, y=150)

lb2 = Label(janela, text = " ")
lb2.place(x=125, y=200)


#WxH+L+T
janela.geometry("300x300+200+200")

janela.mainloop()