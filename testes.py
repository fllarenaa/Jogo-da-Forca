# # import random

# words = ["abacaxi"]

# # wordSelected = random.choice(words)

# def contador(words):
#     for nome in words:
#         r = len(nome)
#         print(f'A letra "o" se repete {r} vezes no nome "{words}"')

# contador(words)

# words = ["abacaxi"]

# numberTest = 2

# while numberTest > 1:
#     print(numberTest)
#     verify = int(input("Digite um número: "))
#     if verify == 10:
#         numberTest = numberTest + 1
#         print(numberTest)

import random

words = ["abacaxi", "sapato", "laranja"]
questionRequest = "S"

while questionRequest != "N":
    wordSelected = random.choice(words)
    print(f"A palavra foi: {wordSelected}")
    break
countWord = len(wordSelected)
insertWord = input("Digite uma letra:")
n = 0
tryCount = 0 
 
if insertWord == wordSelected[n]:
    print("acertou")
    print(wordSelected[n])     
else: 
    print("errou") 
questionRequest = input("Deseja jogar novamente? S ou N: ").upper()
