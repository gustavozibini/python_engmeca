# Solicitar as notas
semestre = 1
medias = []

while semestre <=2:
    semestre = int(input("digite o semestre: "))

    cp1 = float(input("Checkpoint 1 (0 a 10) = "))
    cp2 = float(input("Checkpoint 2 (0 a 10) = "))
    cp3 = float(input("Checkpoint 3 (0 a 10) = "))
    sprint1 = float(input("Sprint 1 (0 a 10) = "))
    sprint2 = float(input("Sprint 2 (0 a 10) = "))
    gs = float(input("Global Solution (0 a 10) = "))

# Descartar o menor checkpoint usando if
notas = []

    # if cp1 <= cp2 and cp1 <= cp3:
    #     soma_checkpoints = cp2 + cp3
    # elif cp2 <= cp1 and cp2 <= cp3:
    #     soma_checkpoints = cp1 + cp3
    # else:
    #     soma_checkpoints = cp1 + cp2

# Calcular a média dos dois melhores checkpoints e das duas sprints
media_check_sprints = (soma_checkpoints + sprint1 + sprint2) / 4

media_semestre = (soma_checkpoints + soma_checkpoints) / 2

# Calcular a nota parcial (40% de media_check_sprints + 60% de GS)
nota_final = (media_check_sprints * 0.4) + (gs * 0.6)

# Exibir o resultado com 1 casa decimal
print(f"Média semestral = {nota_final:.1f}")
