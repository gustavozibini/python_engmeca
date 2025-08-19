
# Repetições for
# nomes_alunos = [ "Giovanna", "Gustavo", "Vini"]
# for nome in nomes_alunos:
#     print(nome)

# # *comando .captalize() ele transforma sempre a primeira letra em maiúscula padronizando o nome
# lista_alunos = ["Gustavo", "Vinicius", "Giovanna", "Lucas"]
# pesquisa = input("Insira o nome a pesquisar: ").capitalize()
#
# x = 0
# for n in lista_alunos:
#     if n == pesquisa:
#         print("Encontrado")
#         print(x)
#         break
#     x += 1
# else:
#     print("Nao Encontrado")

# notas = [1,0,5,9,7,2]
# maxima = notas[0]
#
# contador = 0
# for nota in notas:
#     if nota > maxima:
#         maxima = nota
#         print(contador)
#     contador +=1
#
# print(maxima)

notas = [1, 0, 5, 9, 7, 2]

maxima = notas[0]
pos = 0
contador = 0

for nota in notas:
    if nota > maxima:
        maxima = nota
        pos = contador
    contador += 1

print(pos)
print(maxima)  # 3 9
