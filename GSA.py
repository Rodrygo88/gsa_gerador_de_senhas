import random
import string
import tkinter as tk
import os
import sys

##--------------------------------------------------------------------------

##------------##
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")  
    return os.path.join(base_path, relative_path)
##------------##

def gerarSenha(tam, mai, min, num, car):

    lista_A = list(string.ascii_uppercase)

    lista_a = list(string.ascii_lowercase) 

    numeros = list(string.digits)   

    caracteres = ["!", "@", "#", "$", "%", "&", "*"]

    senha = ""

    while len(senha) < tam:
        if mai == "S":
            senha += random.choice(lista_A)
        if min == "S":
            senha += random.choice(lista_a)
        if num == "S":
            senha += random.choice(numeros)
        if car == "S":
            senha += random.choice(caracteres)

    senha = list(senha)
    random.shuffle(senha)
    senha = ''.join(senha)

    return senha

def pegar_valor():
    valor = tam.get()

    lista = []
    if mai.get():
        lista.append("S")
    else:
        lista.append("N")
    if min.get():
        lista.append("S")
    else:
        lista.append("N")
    if num.get():
        lista.append("S")
    else:
        lista.append("N")
    if car.get():
        lista.append("S")
    else:
        lista.append("N")

    if "S" in lista:
        texto = gerarSenha(valor,lista[0],lista[1],lista[2],lista[3])
        label_resultado.config(text=texto)

    else:
        texto = "Defina as opções!"
        label_resultado.config(text=texto)

##--------------------------------------------------------------------------

janela = tk.Tk()
janela.title("GSA 0.1")
janela.geometry("260x400")  
janela.configure(bg="lightblue")
janela.resizable(False, False)

##------------##
janela.iconbitmap(resource_path("GSA_icone.ico"))
##------------##

label1 = tk.Label(janela, text="Python", bg="lightblue", font=("Times New Roman", 5, "italic"))
label1.grid(row=0, column=2)

label1 = tk.Label(janela, text="GERADOR DE SENHAS", bg="lightblue", font=("Times New Roman", 14, "italic"))
label1.grid(row=1, column=1)

label2 = tk.Label(janela, text="ESCOLHA AS OPÇÕES", bg="lightblue", fg="white", font=("Times New Roman", 10, "bold"))
label2.grid(row=2, column=1)

label3 = tk.Label(janela, text="Tamanhos:", bg="lightblue")
label3.grid(row=3, column=1)

##--------------------------------------------------------------------------

tam = tk.IntVar()
tam.set(8)

opcoes = [("4", 4), ("8", 8), ("12", 12)]

for i, (texto, valor) in enumerate(opcoes):
    tk.Radiobutton(janela, text=texto, value=valor, variable=tam, bg="lightblue").grid(row=i+4, column=1, sticky="w")

##--------------------------------------------------------------------------

mai = tk.BooleanVar()
min = tk.BooleanVar()
num = tk.BooleanVar()
car = tk.BooleanVar()

label3 = tk.Label(janela, text="Caracteres:", bg="lightblue")
label3.grid(row=7, column=1)

check1 = tk.Checkbutton(janela, text="Maiúsculos", variable=mai, bg="lightblue")
check1.grid(row=8, column=1, sticky="w")

check2 = tk.Checkbutton(janela, text="Minúsculos", variable=min, bg="lightblue")
check2.grid(row=9, column=1, sticky="w")

check3 = tk.Checkbutton(janela, text="Números", variable=num, bg="lightblue")
check3.grid(row=10, column=1, sticky="w")

check4 = tk.Checkbutton(janela, text="Caracteres Especiais", variable=car, bg="lightblue")
check4.grid(row=11, column=1, sticky="w")

##--------------------------------------------------------------------------

botao_confirmar = tk.Button(janela, text="GERAR", command=pegar_valor, bg="white", fg="black", font=("Times New Roman", 12, "bold"))
botao_confirmar.grid(row=12, column=1, pady=10)

##--------------------------------------------------------------------------

label_resultado = tk.Label(janela, text="", font=("Arial", 12), fg="blue", bg="lightblue")
label_resultado.grid(row=13, column=1, pady=10)

label1 = tk.Label(janela, text="Python", bg="lightblue", font=("Times New Roman", 5, "italic"))
label1.grid(row=14, column=0)

janela.mainloop()
