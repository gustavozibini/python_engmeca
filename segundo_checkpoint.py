#Nomes: Gustavo Zibini Belizario RM: 561376  João Vitor RM: 562126
sem1 = 0
sem2 = 0

semestre = int(input("Digite o semestre (1 ou 2): "))

while semestre <= 2:
    # Leitura das notas
    cp1 = float(input("Checkpoint 1 (0 a 10) = "))
    cp2 = float(input("Checkpoint 2 (0 a 10) = "))
    cp3 = float(input("Checkpoint 3 (0 a 10) = "))
    sprint1 = float(input("Sprint 1 (0 a 10) = "))
    sprint2 = float(input("Sprint 2 (0 a 10) = "))
    gs = float(input("Global Solution (0 a 10) = "))

    # Descartar o menor checkpoint
    if cp1 <= cp2 and cp1 <= cp3:
        soma_checkpoints = cp2 + cp3
    elif cp2 <= cp1 and cp2 <= cp3:
        soma_checkpoints = cp1 + cp3
    else:
        soma_checkpoints = cp1 + cp2

    # Média de checkpoints + sprints
    media_check_sprints = (soma_checkpoints + sprint1 + sprint2) / 4

    # Média do semestre (40% + 60%)
    media_semestre = media_check_sprints * 0.4 + gs * 0.6
    print(f"Média do {semestre}º semestre = {media_semestre:.1f}")

    # Armazenar na variável correspondente
    if semestre == 1:
        sem1 = media_semestre
    else:
        sem2 = media_semestre

    semestre += 1

# Cálculo e exibição da média final
media_final = sem1 * 0.4 + sem2 * 0.6
print(f"\nMédia final = {media_final:.1f}")