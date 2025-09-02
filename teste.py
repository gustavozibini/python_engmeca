# Cálculo da média final (descarta menor CP; (2 CP + 2 Sprint)/4 = 40%; GS = 60%)
res = []  # médias dos 2 semestres

for sem in range(2):
    cpz, spr = [], []

    # ler 3 CPs (0..10)
    for k in range(3):
        while True:
            t = input(f"CP{k+1} (0..10): ")
            ok, p, d = (len(t) > 0), 0, 0
            if ok:
                for ch in t:
                    if ch == '.': p += 1
                    elif '0' <= ch <= '9': d += 1
                    else: ok = False; break
            if ok and p <= 1 and d >= 1 and t != '.':
                v = float(t)
                if 0 <= v <= 10: cpz.append(v); break
            print("Inválido. Digite número entre 0 e 10 (use ponto).")

    # ler 2 Sprints (0..10)
    for k in range(2):
        while True:
            t = input(f"Sprint{k+1} (0..10): ")
            ok, p, d = (len(t) > 0), 0, 0
            if ok:
                for ch in t:
                    if ch == '.': p += 1
                    elif '0' <= ch <= '9': d += 1
                    else: ok = False; break
            if ok and p <= 1 and d >= 1 and t != '.':
                v = float(t)
                if 0 <= v <= 10: spr.append(v); break
            print("Inválido. Digite número entre 0 e 10 (use ponto).")

    # ler GS (0..10)
    while True:
        t = input("GS (0..10): ")
        ok, p, d = (len(t) > 0), 0, 0
        if ok:
            for ch in t:
                if ch == '.': p += 1
                elif '0' <= ch <= '9': d += 1
                else: ok = False; break
        if ok and p <= 1 and d >= 1 and t != '.':
            gs = float(t)
            if 0 <= gs <= 10: break
        print("Inválido. Digite número entre 0 e 10 (use ponto).")

    # descartar menor CP usando laço for (sem min())
    min_i = 0
    for i in range(1, len(cpz)):
        if cpz[i] < cpz[min_i]: min_i = i

    cp2 = []
    for i in range(len(cpz)):
        if i != min_i: cp2.append(cpz[i])

    m4 = (cp2[0] + cp2[1] + spr[0] + spr[1]) / 4
    res.append(m4 * 0.4 + gs * 0.6)

final = res[0] * 0.4 + res[1] * 0.6
print(f"\nMÉDIA FINAL: {final:.1f}")
