# Nome: Gabriel Bastos Nhoncanse RM 562022
# Nome: Gustavo Zibini Belizario RM 561376

while True:
    disciplina = input("Nome da disciplina: ")

    notas = {1: [], 2: []}
    medias = {}

    for semestre in range(1, 3):
        print(f"\n {semestre}º semestre")
        cps, sps = [], []

        plano = [["CP", 3], ["Sprint", 2]]

# armazenamento das CPs e Sprints
        for item in plano:
            tipo_avaliacao = item[0]
            quantidade_notas = item[1]
            for i in range(1, quantidade_notas + 1):
                while True:
                    notas_gs1 = input(f"{tipo_avaliacao}{i} (0–10): ")
                    notas_gs2 = ""
                    for ch in notas_gs1:
                        ch2 = '.' if ch == ',' else ch
                        if ch2 not in " \t\r\n":
                            notas_gs2 += ch2

                    if notas_gs2 and notas_gs2 != ".":
                        pontos = 0
                        valido = True
                        for c in notas_gs2:
                            if c == '.':
                                pontos += 1
                            else:
                                if c in "0123456789":
                                    pass
                                else:
                                    valido = False
                                    break
                        if valido and pontos <= 1:
                            n = float(notas_gs2)
                            if 0 <= n <= 10:
                                if tipo_avaliacao == "CP":
                                    cps.append(n)
                                else:
                                    sps.append(n)
                                break
                    print("Valor inválido. Digite de 0 a 10 (ponto ou vírgula nos decimais).")

        # pparte armazenamento da GS
        while True:
            notas_gs1 = input("GS (0–10): ")
            notas_gs2 = ""
            for ch in notas_gs1:
                ch2 = '.' if ch == ',' else ch
                if ch2 not in " \t\r\n":
                    notas_gs2 += ch2

            if notas_gs2 and notas_gs2 != ".":
                pontos = 0
                valido = True
                for c in notas_gs2:
                    if c == '.':
                        pontos += 1
                    else:
                        if c in "0123456789":
                            pass
                        else:
                            valido = False
                            break
                if valido and pontos <= 1:
                    gs = float(notas_gs2)
                    if 0 <= gs <= 10:
                        break
            print("Valor inválido. Digite de 0 a 10.")

        notas[semestre].extend(cps + sps + [gs])

        # parte calculo media semestral
        soma_maiores_cps = sum(cps) - min(cps)   # descarta o menor CP
        media_quatro = (soma_maiores_cps + sum(sps)) / 4
        medias[semestre] = media_quatro * 0.4 + gs * 0.6

    # parte do calculo da frequencia
    while True:
        notas_gs1 = input("\nFrequência (%): ")
        notas_gs2 = ""
        for ch in notas_gs1:
            ch2 = '.' if ch == ',' else ch
            if ch2 not in " \t\r\n":
                notas_gs2 += ch2

        if notas_gs2 and notas_gs2 != ".":
            pontos = 0
            valido = True
            for c in notas_gs2:
                if c == '.':
                    pontos += 1
                else:
                    if c in "0123456789":
                        pass
                    else:
                        valido = False
                        break
            if valido and pontos <= 1:
                freq = float(notas_gs2)
                if 0 <= freq <= 100:
                    break
        print("frequencia inválida. Digite de 0 a 100.")

    media_final = medias[1] * 0.4 + medias[2] * 0.6
    situacao = ("REPROVADO por faltar muito nas aulas, nos vemos novamente!!!" if freq < 75 else
                "Parabéns foi APROVADO uhuuu!!!" if media_final >= 6 else
                "EXAME mas ainda da para recuperar em!!!" if media_final >= 4 else
                "Parabéns voce foi REPROVADO mas pelo menos compareceu nas aulas!!!")

    print("\nResultado")
    print(f"disciplina: {disciplina}")
    print(f"1 semestre: {medias[1]:.1f}")
    print(f"2 semestre: {medias[2]:.1f}")
    print(f"medica final (40% do 1 semestre + 60% do 2 semestre): {media_final:.1f}")
    print(f"frequencia: {freq:.1f}%")
    print(f"situação: {situacao}")

    while True:
            resp = input("\nCalcular outra disciplina? (s/n): ")
            primeira = None
            for ch in resp:
                if not ch.isspace():
                    primeira = ch
                    break
            if primeira in ('s', 'S'):
                break
            if primeira in ('n', 'N'):
                print("Programa encerrado")
                exit()
            print("Resposta inválida. Digite 's' para sim ou 'n' para não.")