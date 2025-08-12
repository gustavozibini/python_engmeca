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
from operator import truediv
#
# notas = [6,7,8,5,4,]
# soma = 0
# x = 0
# while x<5:
#     soma +=notas[x]
#     x+=1
#     print(f"Média = {(soma/x):.2f}")


# notas = [0,0,0,0,0,0,0]
# soma = 0
# x = 0
# while x<7:
#     notas[x] = float(input(f"Nota {x+1}="))
#     soma += notas[x]
#     x+=1
#     print(f"Média={(soma/x):.2f}")


# nomes_alunos = {}
# print(len(nomes_alunos))
# nomes_alunos.append("Gustavo")
# print(nomes_alunos)
# nomes_alunos.append("Teste")
# nomes_alunos.append("teste3")
#
#
# L = []
# while True:
#     num = int(input("Digite um numero (0 sai):"))
#     if num == 0:
#         break
#     L.append(num)
# x = 0
# while x < len(L):
#     print(L[x])
#     x += 1


##utilizando append
# nomes_alunos = []
# while True:
#     nome = input("Nome (Digite sair): ")
#     if nome == "sair":
#         break
#     nomes_alunos.append(nome)
#
# nomes_alunos.sort()
# x = 0
# while x < len(nomes_alunos):
#     print(nomes_alunos[x])
#     x += 1

##segunda forma de fazer:
# nomes_alunos = []
# nomes_alunos = nomes_alunos + ["michele"]
# print(nomes_alunos)
# nomes_alunos += ["Cristiano"]
# print(nomes_alunos)
# nomes_alunos += ["Gustavo","Zibini"]
# print(nomes_alunos)

# #Extend
# nomes_alunos = []
# nomes_alunos.extend("Michele")
# print(nomes_alunos)
#
# PRIMEIRA FORMA DE FAZER
# nomes_alunos1 = []
# while True:
#     nome = input("Lista 1 (Digite sair): ")
#     if nome == "sair":
#         break
#     nomes_alunos1.append(nome)
#
# nomes_alunos1.sort()
# x = 0
# while x < len(nomes_alunos1):
#     x += 1
#
# nomes_alunos2 = []
# while True:
#     nome = input("Lista 2 (Digite sair): ")
#     if nome == "sair":
#         break
#     nomes_alunos2.append(nome)
#
# nomes_alunos2.sort()
# x = 0
# while x < len(nomes_alunos2):
#     x += 1
#
# lista_final= nomes_alunos1 + nomes_alunos2
#
# print(nomes_alunos1)
# print(nomes_alunos2)
# print(lista_final)


# # SEGUNDA FORMA DE FAZER
# nomes_alunos = ["Michele", "Gustavo", "Giovanna", "Yan"]
# nomes_alunos_novos = []
#
# while True:
#     aluno_novo = input ("Nome (fim para sair): ")
#     if aluno_novo == "sair":
#         break
#     nomes_alunos_novos.append(aluno_novo)
#
# # nova_lista = nomes_alunos_novos + nomes_alunos_novos
# # print(nova_lista)
#
# nova_lista = []
# nova_lista.extend(nomes_alunos + nomes_alunos_novos)
# print(nova_lista)

nomes_alunos = ["Gustavo","Gustavo2","Gustavo3","Gustavo4",]
pesquisa = input("Digite o nome a pesquisar: ")

x = 0
while x < len(nomes_alunos):
    if nomes_alunos[x] == pesquisa:
        break
    x += 1

if x < len(nomes_alunos):
    print(f"{pesquisa} achado na posição {x}.")
else:
    print(f"{pesquisa} não encontrado.")

# del nomes_alunos [x]
# print(nomes_alunos)