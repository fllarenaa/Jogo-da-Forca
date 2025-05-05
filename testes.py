# # import random

# words = ["abacaxi"]

# # wordSelected = random.choice(words)

# def contador(words):
#     for nome in words:
#         r = len(nome)
#         print(f'A letra "o" se repete {r} vezes no nome "{words}"')

# contador(words)

# words = ["abacaxi"]

numberTest = 2

while numberTest > 1:
    print(numberTest)
    verify = int(input("Digite um número: "))
    if verify == 10:
        numberTest = numberTest + 1
        print(numberTest)