import random



# while questionRequest != "N":
words = ["abacaxi", "sapato", "laranja"]
words = random.choice(words)
tentativas = 6
letras_erradas=[]
letras_certas=['_' for _ in words]

print("🎮 Bem-vindo ao jogo da Forca")

while tentativas > 0 and '_' in letras_certas:
    print("\nPalavra:", ' '.join(letras_certas))

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


while tryCount < questionRequest != "NS":
    insertWord = input("Digite uma letra:")

    print(" ----------------|")
    print(" |               |")
    # print(f" |             {head} ")
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

# if tryCount < countWord: 
    if insertWord == words[n]:
        print("Acertou a letra!")
        tryCount += 1
        n += 1
        print(f"O tryCont agora é {tryCount}")
        # break
    else:
        print("Errou a letra!")
        errorCount += 1
        print(f"ErroCount é igual a {errorCount} agora.")
        # Fazer lógica para quando errar
        if tryCount == 7:
            questionRequest = input("Você Ganhou. Deseja jogar novamente? S ou N").upper()
            tryCount = 0
            n = 0
            errorCount = 0
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
            # break





    
questionRequest = input("Deseja jogar novamente? S ou N").upper()
print("Fim do jogo.")

        
# questionRequest = input("Deseja jogar novamente? S ou N").upper()
# print("Fim do jogo.")