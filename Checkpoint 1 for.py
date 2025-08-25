def ler_nota(prompt):
    # Aceita vírgula como decimal e valida 0..10
    while True:
        s = input(prompt).strip().replace(',', '.')
        try:
            n = float(s)
        except ValueError:
            print("Valor inválido. Digite um número entre 0 e 10.")
            continue
        if 0 <= n <= 10:
            return n
        print("Fora do intervalo. Digite de 0 a 10.")

def ler_semestre(num_semestre):
    print(f"\n=== Notas do {num_semestre}º semestre ===")

    # 3 CPs
    cps = []
    for i in range(1, 4):
        cps.append(ler_nota(f"CP{i}: "))

    # 2 Sprints
    sprints = []
    for i in range(1, 3):
        sprints.append(ler_nota(f"Sprint{i}: "))

    # 1 GS
    gs = ler_nota("Global Solution (GS): ")

    # --- descartar o menor CP usando laço for (sem usar min()) ---
    idx_menor = 0
    for i in range(1, len(cps)):
        if cps[i] < cps[idx_menor]:
            idx_menor = i
    menor_descartado = cps[idx_menor]
    # cria uma cópia e remove o menor
    cps_restantes = cps[:]
    cps_restantes.pop(idx_menor)

    # média dos 4 (2 CPs restantes + 2 Sprints)
    media_quatro = (cps_restantes[0] + cps_restantes[1] + sprints[0] + sprints[1]) / 4

    # 40% da média_quatro + 60% da GS
    media_semestral = media_quatro * 0.4 + gs * 0.6

    # feedback opcional
    print(f"(Descartado menor CP = {menor_descartado:.1f}; CPs usados = {cps_restantes})")
    print(f"Média parcial (2 CPs + 2 Sprints)/4 = {media_quatro:.1f}")
    print(f"Média semestral = {media_semestral:.1f}")

    return media_semestral

m1 = ler_semestre(1)
m2 = ler_semestre(2)

media_final = m1 * 0.4 + m2 * 0.6
print(f"\n=== Resultado ===")
print(f"Média do 1º semestre: {m1:.1f}")
print(f"Média do 2º semestre: {m2:.1f}")
print(f"MÉDIA FINAL: {media_final:.1f}")
