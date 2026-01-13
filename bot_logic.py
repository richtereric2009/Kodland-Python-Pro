import random

def pass_gen(size):
    palavra = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    tamanho = size
    senha = ""
    for i in range(tamanho):
        senha += random.choice(palavra)
    return senha
