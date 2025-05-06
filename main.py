import random

words = ["abacaxi", "sapato", "laranja"]
questionRequest = "S"
wordSelected = random.choice(words)
print(f"A palavra foi: {wordSelected}")
# insertWord = input("Digite uma letra:")
# while questionRequest != "N":
    
    # break
countWord = len(wordSelected)

n = 0
tryCount = 0 

while tryCount < countWord:
    insertWord = input("Digite uma letra:")
# if tryCount < countWord: 
    if insertWord == wordSelected[n]:
        print("Acertou a primeira letra!")
        tryCount += 1
        print(f"O tryCont agora é {tryCount}")
        # break
else:
    print("Errou a primeira letra!")
    

        
# questionRequest = input("Deseja jogar novamente? S ou N").upper()
print("Fim do jogo.")