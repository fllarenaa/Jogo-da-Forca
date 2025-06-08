import random

# Lista de palavras para o jogo
palavras = ['python', 'programacao', 'openai', 'inteligencia', 'chatgpt']

# Escolhe uma palavra aleatória
palavra = random.choice(palavras)
letras_descobertas = ['_' for _ in palavra]
tentativas = 6
letras_erradas = []

print("🎮 Bem-vindo ao jogo da Forca!")

while tentativas > 0 and '_' in letras_descobertas:
    print("\nPalavra:", ' '.join(letras_descobertas))
    print("Letras erradas:", ', '.join(letras_erradas))
    print(f"Tentativas restantes: {tentativas}")
    
    chute = input("Digite uma letra: ").lower()

    if not chute.isalpha() or len(chute) != 1:
        print("Digite apenas uma letra.")
        continue

    if chute in letras_descobertas or chute in letras_erradas:
        print("Você já tentou essa letra.")
        continue

    if chute in palavra:
        for i, letra in enumerate(palavra):
            if letra == chute:
                letras_descobertas[i] = chute
        print("✅ Boa! Você acertou uma letra.")
    else:
        letras_erradas.append(chute)
        tentativas -= 1
        print("❌ Letra errada.")

# Resultado final
if '_' not in letras_descobertas:
    print("\n🎉 Parabéns! Você venceu. A palavra era:", palavra)
else:
    print("\n💀 Fim de jogo! A palavra era:", palavra)
