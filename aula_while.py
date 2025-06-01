#EXERCICIO1------
# x = 1
# while x <= 100:
#     print(x)
#     x = x + 1
#
#EXERCICIO2------
# x = 50
# while x <= 100:
#     print(x)
#     x = x + 1
#
#EXERCICIO3-------
# x = 10
# while x >= 0:
#     print(x)
#     x = x - 1
# print("Fogo!")
#
#EXERCICIO4-------
# fim = int(input("digite o último numero"))
# x = 1
# while x <= fim:
#     print(x)
#     x = x + 2
#
#EXERCICIO5________
# x = 3
# while x <= 30:
#     print(x)
#     x = x + 3
#
#*****EXEMPLO*****
# n = int(input("digite qual tabuada deseja: "))
# x = 1
# while x <= 10:
#     print(x * n)
#     x = x + 1
#
# EXERCICIO6
# n = int(input("digite a tabuada desejada: "))
# x = 1
# while x <= 10:
#     print(f"{n} x {x}=", n * x)
#     x = x + 1
#
# EXERCICIO7
# tabuada = int(input("Tabuada de: "))
# n1 = int(input("Digite o inicio: "))
# n2 = int(input("Digite o final: "))
# while n1 <= n2:
#     print(f"{tabuada} x {n1} =",tabuada * n1)
#     n1 =  n1 + 1
#
# exercicio8
# deposito = float(input("Deposito: "))
# taxa = float(input("Taxa de juros: "))
# mes = 1
# while mes <= 24:
#     deposito = deposito + (deposito * (taxa / 100))
#     print(f"Saldo do mês {mes} é de R${deposito:.2f}.")
#     mes = mes + 1
# print(f"O ganho com juros foi de R${deposito:.2f}.")
#
#
#
# EXERCICIO9
# deposito = float(input("Deposito: "))
# taxa = float(input("Taxa de juros: "))
# investimento = float(input("Investimento mensal: "))
# mes = 1
# while mes <= 24:
#     deposito = deposito + (deposito * (taxa / 100)) + investimento
#     print(f"Saldo do mês {mes} é de R${deposito:.2f}.")
#     mes = mes + 1
# print(f"O ganho com juros foi de R${deposito:.2f}.")
# #
# EXERCICIO10
# soma = 0
# cont = 0
# while True:
#     num = int(input("Digite:"))
#     if num == 0:
#         break
#     soma = soma + num
#     cont += 1
# print("quantidade de numeros:", cont)
# print("Soma=", soma)
# print(f"Media={soma/cont:.2f}")
#
# # EXERCICIO11
# soma = 0
# while True:
#     codigo = int(input("digite o código do produto: "))
#     vlr = 0
#     if codigo == 0:
#         break
#     elif codigo == 1:
#         vlr = 0.1
#     elif codigo == 2:
#         vlr = 0.2
#     elif codigo == 3:
#         vlr = 0.3
#     elif codigo == 4:
#         vlr = 0.4
#     elif codigo == 5:
#         vlr = 0.5
#     elif codigo == 6:
#          vlr = 0.6
#     else:
#         print("Digite o código correto apenas de 1 até 6")
#     if vlr != 0:
#         quantidade = int(input("quantidade: "))
#         soma = soma + (vlr * quantidade)
# print(f"total a pagar R$: {soma:.2f}")