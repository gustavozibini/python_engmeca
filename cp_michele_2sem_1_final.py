# Nome: Gabriel Bastos Nhoncanse RM 562022
# Nome: Gustavo Zibini Belizario RM 561376


medias_semestre = []

for semestre in range(1, 3):
    print(f"\n=== {semestre}º SEMESTRE ===")
    cps = []
    sprints = []

    # Ler 3 CHECKPOINT nota de 0 até 10 (diferente vai apresentar erro)
    for i in range(1, 4):
        while True:
            notas = input(f"CP{i} (0 a 10): ")
            ok = True
            pontos = 0
            numero = 0

            if len(notas) == 0:
                ok = False
            else:
                for x in notas:
                    if x == '.':
                        pontos += 1
                    elif '0' <= x <= '9':
                        numero += 1
                    else:
                        ok = False
                        break

            if ok and pontos <= 1 and numero >= 1 and notas != '.':
                nota = float(notas)
                if 0 <= nota <= 10:
                    cps.append(nota)
                    break

            print("Ops! Tenta de novo (número entre 0 e 10; use ponto nos decimais).")

    # Ler 2 Sprints com nota de 0 até 10 (diferente vai apresentar erro)
    for i in range(1, 3):
        while True:
            notas = input(f"Sprint{i} (0 a 10): ")
            ok = True
            pontos = 0
            numero = 0

            if len(notas) == 0:
                ok = False
            else:
                for x in notas:
                    if x == '.':
                        pontos += 1
                    elif '0' <= x <= '9':
                        numero += 1
                    else:
                        ok = False
                        break

            if ok and pontos <= 1 and numero >= 1 and notas != '.':
                nota = float(notas)
                if 0 <= nota <= 10:
                    sprints.append(nota)
                    break

            print("Valor inválido. Digite de 0 a 10 (use ponto para decimais).")
    # Ler 2 Sprints com nota de 0 até 10 (diferente vai apresentar erro)


    # Ler GS nota de 0 até 10 (diferente vai apresentar erro)
    while True:
        notas = input("GS (0 a 10): ")
        ok = True
        pontos = 0
        numero = 0

        if len(notas) == 0:
            ok = False
        else:
            for x in notas:
                if x == '.':
                    pontos += 1
                elif '0' <= x <= '9':
                    numero += 1
                else:
                    ok = False
                    break

        if ok and pontos <= 1 and numero >= 1 and notas != '.':
            gs = float(notas)
            if 0 <= gs <= 10:
                break

        print("Valor inválido. Digite de 0 a 10 (use ponto para decimais).")

    # _______________________Achar o menor CP____________________________________
    menor = 0
    for i in range(1, len(cps)):
        if cps[i] < cps[menor]:
            menor = i

    cp_usados = []
    for i in range(len(cps)):
        if i != menor:
            cp_usados.append(cps[i])
    # _______________________Achar o menor CP____________________________________


    print(f"Descartando o menor CP: CP{menor + 1} = {cps[menor]:.1f}")
    print(f"Usando estes CPs: {cp_usados[0]:.1f} e {cp_usados[1]:.1f}")

    media_quatro = (cp_usados[0] + cp_usados[1] + sprints[0] + sprints[1]) / 4
    media_sem = media_quatro * 0.4 + gs * 0.6

    print(f"Média (2 CPs + 2 Sprints)/4 = {media_quatro:.1f}")
    print(f"Média do {semestre}º semestre = {media_sem:.1f}")

    medias_semestre.append(media_sem)

media_final = medias_semestre[0] * 0.4 + medias_semestre[1] * 0.6
print(f"\n=== RESULTADO GERAL ===")
print(f"1º semestre: {medias_semestre[0]:.1f}")
print(f"2º semestre: {medias_semestre[1]:.1f}")
print(f"MÉDIA FINAL (40% do 1º + 60% do 2º): {media_final:.1f}")
