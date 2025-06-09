import random

def desenhar_forca(error_count, partes):
    head1, head2, head3, head4, body1, body2, body3, body4, arm, arm2, leg1, leg2 = partes
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

def atualizar_partes(error_count):
    partes = [""] * 12
    if error_count >= 1:
        partes[0] = "_"   # head1
        partes[1] = "\\"  # head2
        partes[2] = "/"   # head3
        partes[3] = "--"  # head4
    if error_count >= 2:
        partes[4] = "|"   # body1
        partes[5] = "|"   # body2
        partes[6] = "|"   # body3
        partes[7] = "|"   # body4
    if error_count >= 3:
        partes[8] = "/"   # arm
    if error_count >= 4:
        partes[9] = "\\"  # arm2
    if error_count >= 5:
        partes[10] = "/"  # leg1
    if error_count >= 6:
        partes[11] = "\\" # leg2
    return partes

def escolher_categoria():
    categorias = {
        "1": ("Profissões", ["professor", "engenheiro", "padeiro", "cozinheiro", "segurança"]),
        "2": ("Comidas", ["lasanha", "hamburguer", "sushi","pizza"]),
        "3": ("Cores", ["vermelho", "azul", "amarelo","verde"]),
        "4": ("Objetos", ["cadeira", "telefone", "garrafa","colher"]),
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
    letras_descobertas = ['_' for _ in palavra]
    letras_erradas = []
    tentativas = 6
    error_count = 0

    print(f"\n🎮 Categoria: {categoria}")
    
    while tentativas > 0 and '_' in letras_descobertas:
        partes = atualizar_partes(error_count)
        desenhar_forca(error_count, partes)

        print("Palavra:", ' '.join(letras_descobertas))
        print("Letras erradas:", ', '.join(letras_erradas))
        print(f"Tentativas restantes: {tentativas}")

        letra = input("Digite uma letra: ").lower()

        if not letra.isalpha() or len(letra) != 1:
            print("Digite apenas uma letra válida.\n")
            continue

        if letra in letras_descobertas or letra in letras_erradas:
            print("Você já tentou essa letra.\n")
            continue

        if letra in palavra:
            for i, l in enumerate(palavra):
                if l == letra:
                    letras_descobertas[i] = letra
            print("✅ Acertou!\n")
        else:
            letras_erradas.append(letra)
            error_count += 1
            tentativas -= 1
            print("❌ Errou!\n")

    partes = atualizar_partes(error_count)
    desenhar_forca(error_count, partes)

    if '_' not in letras_descobertas:
        print(f"\n🎉 Parabéns! Você venceu. A palavra era: {palavra}")
    else:
        print(f"\n💀 Você perdeu. A palavra era: {palavra}")


while True:
    jogar_forca()
    jogar_novamente = input("Deseja jogar novamente? (S/N): ").strip().upper()
    if jogar_novamente != "S":
        print("👋 Obrigado por jogar!")
        break
    