import random

questionRequest = "S"

words = ["abacaxi", "sapato", "laranja"]
wordSelected = random.choice(words)
print(f"A palavra foi: {wordSelected}")
countWord = len(wordSelected)

displayWord = ["-" for _ in wordSelected]  

n = 0
tryCount = 0
errorCount = 0
head1 = ""
head2 = ""
head3 = ""
head4 = ""
body1 = ""
body2 = ""
body3 = ""
body4 = ""
arm = ""
arm2 = ''
leg1 = ""
leg2 = ""

while tryCount < countWord and questionRequest != "N":
    insertWord = input("Digite uma letra:")

    print(" ----------------|")
    print(" |               |")
    print(f" |              {head1}{head1}")
    print(f" |            {head3}    {head2}")
    print(f" |            {head2}    {head3}")
    print(f" |              {head4}")
    print(f" |             {arm}{body1}{arm2}")
    print(f" |            {arm} {body2} {arm2}")
    print(f" |              {body3}")
    print(f" |              {body4}")
    print(f" |             {leg1} {leg2}")
    print(f" |            {leg1}   {leg2}")
    print(f" |           {leg1}     {leg2}")

    if insertWord in wordSelected:
        print("Acertou a letra!")

        countBefore = displayWord.count("-")

        for idx, letter in enumerate(wordSelected):
            if letter == insertWord:
                displayWord[idx] = insertWord

        print("Palavra: " + "".join(displayWord))

        tryCount = len([c for c in displayWord if c != "-"])
        print(f"O tryCont agora é {tryCount}")
    else:
        print("Errou a letra!")
        errorCount += 1
        print("Palavra: " + "".join(displayWord))
        print(f"ErroCount é igual a {errorCount} agora.")

        if tryCount == 6:
            questionRequest = input("Parabéns! Você Ganhou. Deseja jogar novamente? S ou N").upper()
            tryCount = 0
            n = 0
            errorCount = 0
            head1 = ""
            head2 = ""
            head3 = ""
            head4 = ""
            body1 = ""
            body2 = ""
            body3 = ""
            body4 = ""
            arm = ""
            arm2 = ''
            leg1 = ""
            leg2 = ""
            displayWord = ["-" for _ in wordSelected]
        elif errorCount == 1:
            head1 = "_"
            head2 = "\\"
            head3 = "/"
            head4 = "--"
        elif errorCount == 2:
            body1 = "|"
            body2 = "|"
            body3 = "|"
            body4 = "|"
        elif errorCount == 3:
            arm = "/"
        elif errorCount == 4:
            arm2 = '\\'
        elif errorCount == 5:
            leg1 = "/"
        elif errorCount == 6:
            leg2 = "\\"
        elif errorCount == 7:
            questionRequest = input("Você perdeu. Deseja jogar novamente? S ou N").upper()
            tryCount = 0
            n = 0
            errorCount = 0
            head1 = ""
            head2 = ""
            head3 = ""
            head4 = ""
            body1 = ""
            body2 = ""
            body3 = ""
            body4 = ""
            arm = ""
            arm2 = ''
            leg1 = ""
            leg2 = ""
            displayWord = ["-" for _ in wordSelected]

print("Fim do jogo.")