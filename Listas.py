# nomes_alunos = []
# print(nomes_alunos)
# print(len(nomes_alunos))
# nomes_alunos = ["nome", "nome2", "nome3", "nome4"]
# print(nomes_alunos)
# print(len(nomes_alunos))
# nomes_alunos[0] = "Gustavo"
# print(nomes_alunos)
# nomes_alunos[1] = "Zibini"
# print(nomes_alunos)


# notas = [6,7,8,5,4,]
# soma = 0
# x = 0
# while x<5:
#     soma +=notas[x]
#     x+=1
#     print(f"Média = {(soma/x):.2f}")


notas = [0,0,0,0,0,0,0]
soma = 0
x = 0
while x<7:
    notas[x] = float(input(f"Nota {x+1}="))
    soma += notas[x]
    x+=1
    print(f"Média={(soma/x):.2f}")

