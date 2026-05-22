import tkinter as tk
import os
import sys
from gerador import gerarSenha

##--------------------------------------------------------------------------


##------------##
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


##------------##


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
        texto = gerarSenha(valor, lista[0], lista[1], lista[2], lista[3])
        label_resultado.config(text=texto, fg=cor_texto)

    else:
        texto = "Defina as opções!"
        label_resultado.config(text=texto, fg="#b42318")


##--------------------------------------------------------------------------

janela = tk.Tk()
janela.title("GSA 0.1")
janela.geometry("300x550")
janela.configure(bg="#dff3f5")
janela.resizable(False, False)

##------------##
janela.iconbitmap(resource_path("GSA_icone.ico"))
##------------##

cor_fundo = "#dff3f5"
cor_texto = "#183b56"
cor_secundaria = "#486581"
cor_botao = "#2f80ed"
cor_resultado = "#ffffff"

janela.grid_columnconfigure(0, weight=1)

label1 = tk.Label(
    janela,
    text="Python",
    bg=cor_fundo,
    fg=cor_secundaria,
    font=("Arial", 7, "italic"),
)
label1.grid(row=0, column=0, padx=20, pady=(8, 0), sticky="e")

label1 = tk.Label(
    janela,
    text="GERADOR DE SENHAS",
    bg=cor_fundo,
    fg=cor_texto,
    font=("Arial", 16, "bold"),
)
label1.grid(row=1, column=0, pady=(16, 4))

label2 = tk.Label(
    janela,
    text="ESCOLHA AS OPÇÕES",
    bg=cor_fundo,
    fg=cor_secundaria,
    font=("Arial", 10, "bold"),
)
label2.grid(row=2, column=0, pady=(0, 18))

label3 = tk.Label(
    janela,
    text="Tamanhos:",
    bg=cor_fundo,
    fg=cor_texto,
    font=("Arial", 10, "bold"),
)
label3.grid(row=3, column=0, padx=52, sticky="w")

##--------------------------------------------------------------------------

tam = tk.IntVar()
tam.set(8)

opcoes = [("4", 4), ("8", 8), ("12", 12)]

for i, (texto, valor) in enumerate(opcoes):
    tk.Radiobutton(
        janela,
        text=texto,
        value=valor,
        variable=tam,
        bg=cor_fundo,
        fg=cor_texto,
        activebackground=cor_fundo,
        selectcolor=cor_resultado,
        font=("Arial", 10),
    ).grid(row=i + 4, column=0, padx=70, sticky="w")

##--------------------------------------------------------------------------

mai = tk.BooleanVar()
min = tk.BooleanVar()
num = tk.BooleanVar()
car = tk.BooleanVar()

label3 = tk.Label(
    janela,
    text="Caracteres:",
    bg=cor_fundo,
    fg=cor_texto,
    font=("Arial", 10, "bold"),
)
label3.grid(row=7, column=0, padx=52, pady=(14, 4), sticky="w")

check1 = tk.Checkbutton(
    janela,
    text="Maiúsculos",
    variable=mai,
    bg=cor_fundo,
    fg=cor_texto,
    activebackground=cor_fundo,
    selectcolor=cor_resultado,
    font=("Arial", 10),
)
check1.grid(row=8, column=0, padx=70, sticky="w")

check2 = tk.Checkbutton(
    janela,
    text="Minúsculos",
    variable=min,
    bg=cor_fundo,
    fg=cor_texto,
    activebackground=cor_fundo,
    selectcolor=cor_resultado,
    font=("Arial", 10),
)
check2.grid(row=9, column=0, padx=70, sticky="w")

check3 = tk.Checkbutton(
    janela,
    text="Números",
    variable=num,
    bg=cor_fundo,
    fg=cor_texto,
    activebackground=cor_fundo,
    selectcolor=cor_resultado,
    font=("Arial", 10),
)
check3.grid(row=10, column=0, padx=70, sticky="w")

check4 = tk.Checkbutton(
    janela,
    text="Caracteres Especiais",
    variable=car,
    bg=cor_fundo,
    fg=cor_texto,
    activebackground=cor_fundo,
    selectcolor=cor_resultado,
    font=("Arial", 10),
)
check4.grid(row=11, column=0, padx=70, sticky="w")

##--------------------------------------------------------------------------

botao_confirmar = tk.Button(
    janela,
    text="GERAR",
    command=pegar_valor,
    bg=cor_botao,
    fg="white",
    activebackground="#1c6dd0",
    activeforeground="white",
    relief="raised",
    bd=2,
    font=("Arial", 12, "bold"),
)
botao_confirmar.grid(row=12, column=0, ipadx=34, ipady=5, pady=18)

##--------------------------------------------------------------------------

label_resultado = tk.Label(
    janela,
    text="Sua senha aparece aqui",
    font=("Arial", 13, "bold"),
    fg=cor_texto,
    bg=cor_resultado,
    width=22,
    height=2,
    relief="groove",
    bd=2,
)
label_resultado.grid(row=13, column=0, pady=(0, 8))

label1 = tk.Label(
    janela,
    text="GSA 0.1",
    bg=cor_fundo,
    fg=cor_secundaria,
    font=("Arial", 8),
)
label1.grid(row=14, column=0, padx=16, sticky="w")

janela.mainloop()
