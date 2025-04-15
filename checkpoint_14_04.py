cp1 = float(input("Digite o valor do primeiro CheckPoint (O valor deve ser de 0 até 10):"))
cp2 = float(input("Digite o valor do segundo CheckPoint (O valor deve ser de 0 até 10):"))
cp3 = float(input("Digite o valor do terceiro CheckPoint (O valor deve ser de 0 até 10):"))
sp1 = float(input("Digite o valor da primeira Sprint (O valor deve ser de 0 até 10):"))
sp2 = float(input("Digite o valor da Segunda Sprint (O valor deve ser de 0 até 10):"))
gs = float(input("Digite o valor da Global Solution (O valor deve ser de 0 até 10):"))

cpm = cp1
if cp2 <= cp1 and cp2 <= cp3:
    cpm = cp2
if cp3 <= cp1 and cp3 <= cp1:
    cpm = cp3

media = cp1 + cp2 + cp3 - cpm

nota_final = ((((media + sp1 + sp2) / 4) * 0.4) + gs * 0.6)

print(f"A média semestral do aluno é:{nota_final:.1f}")

