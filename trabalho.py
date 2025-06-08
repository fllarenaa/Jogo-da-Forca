def escolher_categoria():
    categorias = {
        "1": ("Profissões", ["professor", "engenheiro", "padeiro", "cozinheiro", "segurança"]),
        "2": ("Comidas", ["lasanha", "hamburguer", "sushi","pizza"]),
        "3": ("Cores", ["vermelho", "azul", "amarelo","verde"]),
        "4": ("Objetos", ["cadeira", "telefone", "garrafa","colher"]),
         }

import random
def desenhar_forca(erros):
    estagios = [
        """
           _______
           |     |
           |     
           |    
           |     
           |    
        ___|___
        """,
        """
           _______
           |     |
           |     O
           |    
           |     
           |    
        ___|___
        """,
        """
           _______
           |     |
           |     O
           |     |
           |     
           |    
        ___|___
        """,
        """
           _______
           |     |
           |     O
           |    /|
           |     
           |    
        ___|___
        """,
        """
           _______
           |     |
           |     O
           |    /|\\
           |     
           |    
        ___|___
        """,
        """
           _______
           |     |
           |     O
           |    /|\\
           |    / 
           |    
        ___|___
        """,
        """
           _______
           |     |
           |     O
           |    /|\\
           |    / \\
           |    
        ___|___
        """
    ]
    print(estagios[erros])
    
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