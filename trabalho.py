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

def escolher_categoria():
    categorias = {
        "1": ("Profissões", ["professor", "engenheiro", "padeiro", "cozinheiro", "segurança"]),
        "2": ("Comidas", ["lasanha", "hamburguer", "sushi", "pizza"]),
        "3": ("Cores", ["vermelho", "azul", "amarelo", "verde"]),
        "4": ("Objetos", ["cadeira", "telefone", "garrafa", "colher"]),
    }

    print("🎮 Bem-vindo ao jogo da Forca!")
    print("Escolha uma categoria:")
    for key, (nome, _) in categorias.items():
        print(f"{key} - {nome}")

    escolha = input("Digite o número da categoria: ").strip()
    while escolha not in categorias:
        escolha = input("Digite um número entre 1 e 4: ").strip()

    nome_categoria, palavras = categorias[escolha]
    return nome_categoria, random.choice(palavras)

def jogar_forca():
    categoria, palavra = escolher_categoria()
    letras_certas = ['_' for _ in palavra]
    letras_erradas = []
    tentativas = 6

    print(f"\n🎮 Jogo da Forca - Categoria: {categoria}")

    while tentativas > 0 and '_' in letras_certas:
        desenhar_forca(len(letras_erradas))
        print("Palavra:", ' '.join(letras_certas))
        print(f"Letras erradas: {', '.join(letras_erradas)}")
        print(f"Tentativas restantes: {tentativas}")

        letra = input("Digite uma letra: ").lower()

        if not letra.isalpha() or len(letra) != 1:
            print("Digite apenas uma letra válida.")
            continue

        if letra in letras_certas or letra in letras_erradas:
            print("Você já tentou essa letra, digite outra.")
            continue

        if letra in palavra:
            for i, l in enumerate(palavra):
                if l == letra:
                    letras_certas[i] = letra
            print("✅ Você acertou!")
        else:
            letras_erradas.append(letra)
            tentativas -= 1
            print("❌ Você errou, tente de novo!")

    desenhar_forca(len(letras_erradas))
    if '_' not in letras_certas:
        print(f"\n🎉 Muito bem, você ganhou! A palavra era: {palavra}")
    else:
        print(f"\n💀 Você perdeu. A palavra era: {palavra}")

while True:
    jogar_forca()
    jogar_novamente = input("\nDeseja jogar novamente? (S/N): ").strip().upper()
    if jogar_novamente != 'S':
        print("👋 Obrigado por jogar!")
        break
