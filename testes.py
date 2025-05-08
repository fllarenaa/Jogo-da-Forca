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

# import random

# words = ["abacaxi", "sapato", "laranja"]
# questionRequest = "S"


# wordSelected = random.choice(words)
# print(f"A palavra foi: {wordSelected}")
# countWord = len(wordSelected)    # break
# while questionRequest != "N":
      
#         insertWord = input("Digite uma letra:")
# n = 0
# tryCount = 0 
# while tryCount < countWord:
#     if insertWord == wordSelected[n]:
#         print("acertou")
#         tryCount += 1
#         print(wordSelected[n], tryCount)     
# else: 
#         print("errou") 
#         questionRequest = input("Deseja jogar novamente? S ou N: ").upper()
valuenum = 10
if valuenum == 10:
    head1 = "_"
    head2 = "\\"
    head3 = "/"
    head4 = "--"
    body1 = "|"
    body2 = "|"
    body3 = "|"
    body4 = "|"
    arm = "/"
    arm2 = '\\'
    leg1 = "/"
    leg2 = "\\"
else:
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