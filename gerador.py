import random
import string


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
    senha = "".join(senha[:tam])

    return senha
