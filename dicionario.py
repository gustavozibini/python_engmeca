# rm_alunos = {"561376": ["Gustavo Zibini Belizario", "14/11/92"], "123456": ["Pedrinho Anaozinho", "11/11/00"]}
# print(rm_alunos)
# print(rm_alunos["561376"])
# print(rm_alunos["123456"])
#
# del rm_alunos["123456"]
# print(rm_alunos)
#
# rm_alunos["561376"][1] = "14/11/1992"
# print(rm_alunos)
#
# print("123456" in rm_alunos)
#
# print (rm_alunos.keys())
# print(rm_alunos.values())


# cursos = {"mecatronica": [2200, "60 Meses", "presencial", 60],
#         "ia":           [1800, "24 Meses", "ead", 50 ],
#         "quimica":      [2560, "60 Meses", "presencial", 40],
#         "cloud":        [800, "25 Meses", "ead", 30],
#         "redes":        [1200, "34 Meses", "presencial", 20],
#         "sistemas":     [1500, "12 Meses", "ead", 10]}
#
# turma = 0
# while True:
#     curso = input("Digite o nome do curso ou sair: ").lower()
#     if curso == "sair":
#         break
#     if curso in cursos:
#         valor, duracao, formato, vagas = cursos[curso]
#         print(f"Valor: R$ {valor}\nDuração: {duracao}\nTipo: {formato}\nVagas: {vagas}")
#     else:
#         print("valor nao encontrado")

cursos = {
    "mecatronica":  [2200.50, "60 Meses", "presencial", 60],
    "ia":           [1800.00, "24 Meses", "ead",        50],
    "quimica":      [2560.00, "60 Meses", "presencial", 40],
    "cloud":        [800.00,  "25 Meses", "ead",        30],
    "redes":        [1200.00, "34 Meses", "presencial", 20],
    "sistemas":     [1500.00, "12 Meses", "ead",        1]
}

while True:
    curso = input("Digite o nome do curso ou 'sair': ").lower()
    if curso == "sair":
        break

    if curso in cursos:
        valor, duracao, formato, vagas = cursos[curso]
        print(f"Valor: R$ {valor}\nDuração: {duracao}\nTipo: {formato}\nVagas: {vagas}")

        if vagas == 0:
            print(" Turma sem vagas no momento.")
            continue

        deseja = input("Deseja se matricular (sim/não)? ").lower()

        if deseja in ("sim"):
            cursos[curso][3] -= 1  #calculo da quantidade de vagas
            print(f" Matrícula realizada! Vagas restantes para '{curso}': {cursos[curso][3]}")
        elif deseja in ("nao"):
            print("Ok, matrícula não realizada.")
        else:
            print("Resposta inválida. Matrícula não realizada.")
    else:
        print("valor nao encontrado")
