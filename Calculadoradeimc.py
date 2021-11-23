import string
from tkinter import *
from tkinter import Label
from typing import Tuple


class Application:
    imcValor: Label
    fonte1: tuple[str, str]

    def __init__(self, master=None):
        self.fonte1 = ("Arial"), ("12")

        self.espaço1 = Frame(master)
        self.espaço1['pady'] = 10
        self.espaço1.pack()

        self.espaço2 = Frame(master)
        self.espaço2["padx"] = 20
        self.espaço2.pack()

        self.espaço3 = Frame(master)
        self.espaço3["padx"] = 20
        self.espaço3.pack()

        self.espaço4 = Frame(master)
        self.espaço4["padx"] = 20
        self.espaço4.pack()

        self.espaço5 = Frame(master)
        self.espaço5["padx"] = 20
        self.espaço5.pack()

        self.espaço6 = Frame(master)
        self.espaço6["padx"] = 20
        self.espaço6.pack()

        self.nome = Label(self.espaço1,text="Calculadora IMC: ", font=self.fonte1)
        self.nome["font"] = ("Arial", "10", "bold")
        self.nome.pack()

        self.digitoLabel = Label(self.espaço2, text="PESO", font=self.fonte1)
        self.digitoLabel.pack(side=LEFT)

        self.digito = Entry(self.espaço2)
        self.digito["width"] = 30
        self.digito["font"] = self.fonte1
        self.digito.pack(side=LEFT)

        self.digito2Label = Label(self.espaço3, text="ALTURA", font=self.fonte1)
        self.digito2Label.pack(side=LEFT)

        self.digito2 = Entry(self.espaço3)
        self.digito2["width"] = 30
        self.digito2["font"] = self.fonte1
        self.digito2.pack(side=LEFT)

        # Desifindo a caixa de texto "IMC"
        self.imcLabel = Label(self.espaço4, text="IMC", font=self.fonte1)
        self.imcLabel.pack(side=LEFT)

        self.imcValor = Label(self.espaço5, text="", font=self.fonte1)
        self.imcValor.pack(side=RIGHT)

        # Definindo o botão
        self.calcular = Button(self.espaço6)
        self.calcular["text"] = "CALCULAR"
        self.calcular["font"] = ("Calibri", "8")
        self.calcular["width"] = 12
        self.calcular["command"] = self.calcula
        self.calcular.pack()

    # Calculando
    def calcula(self):
        peso = self.digito.get()
        altura = self.digito2.get()

        resp = (float(peso)) / (float(altura) * float(altura))

        if resp < 17:
            self.imcValor["text"] = resp, 'Muito abaixo do peso'
        elif resp < 18.49:
            self.imcValor["text"] = resp, 'Abaixo do peso'
        elif resp < 24.99:
            self.imcValor["text"] = resp, ' Peso Normal'
        elif resp < 29.99:
            self.imcValor["text"] = resp, ' Acima do Peso'
        elif resp < 34.99:
            self.imcValor["text"] = resp, ' Obesidade Grau 1'
        elif resp < 39.99:
            self.imcValor["text"] = resp, ' Obesidade Grau 2'
        else:
            self.imcValor ["text"] = resp, ' Obesidade Grau 3'

root = Tk()
Application(root)
root.mainloop()