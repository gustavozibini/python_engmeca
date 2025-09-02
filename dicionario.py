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


tabela = {"engenharia mecatrônica": ["2200,00", "60 Meses", "presencial"],
        "inteligência artificial": ["1800,00", "24 Meses", "ead"],
        "quimica": ["2200,00", "60 Meses", "presencial"],
        "cloud": ["800,00", "25 Meses", "ead"],
        "redes": ["1200,00", "34 Meses", "presencial"],
        "sistemas": ["1500,00", "12 Meses", "ead"]}


while True:
    curso = input("Digite o nome do curso ou sair: ").lower()
    if curso == "sair":
        break
    if curso in tabela:
        valor, duracao, formato = tabela[curso]
        print(f"Valor: R$ {valor}\nDuração: {duracao}\nTipo: {formato}")
    else:
        print("valor nao encontrado")