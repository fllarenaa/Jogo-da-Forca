import random

# while questionRequest != "N":
words = ["abacaxi", "sapato", "laranja"]
wordSelected = random.choice(words)
print(f"A palavra foi: {wordSelected}")
# insertWord = input("Digite uma letra:")
# 
    
    # break
countWord = len(wordSelected)

n = 0
tryCount = 0 

while tryCount < countWord:
    insertWord = input("Digite uma letra:")
# if tryCount < countWord: 
    if insertWord == wordSelected[n]:
        print("Acertou a letra!")
        tryCount += 1
        n += 1
        print(f"O tryCont agora é {tryCount}")
        # break
    else:
        print("Errou a letra!")

        # Fazer lógica para quando errar
    

        
# questionRequest = input("Deseja jogar novamente? S ou N").upper()
print("Fim do jogo.")
