# import random

words = ["abacaxi"]

# wordSelected = random.choice(words)

def contador(words):
    for nome in words:
        r = len(nome)
        print(f'A letra "o" se repete {r} vezes no nome "{words}"')

contador(words)