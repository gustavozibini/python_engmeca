# media_final = float(input("Digite a média de 0 a 10: "))
#
# if media_final >=6:
#     print("aprovado!")
# else:
#     print("reprovado!")
#
# ex1:
# velocidade = int(input("Digite a velocidade do carro: "))
#
# if velocidade > 80:
#     multa = (velocidade - 80) * 5
#     print (f"Você ultrapassou o limite de velocidade e foi multado em: R${multa:.2f}")
# else:
#     print("Você não foi multado")
#
#
# num1 = float(input("Digite o primeiro número: "))
# num2 = float(input("Digite o segundo número: "))
# num3 = float(input("Digite o terceiro número: "))
#
# if num1 >= num2 and num1 >= num3:
#     print(f"O maior numero é {num1}")
# elif num2 >= num1 and num2 >= num3:
#     print(f"O maior numero é {num2}")
# elif num3 >= num1 and num3 >= num2:
#     print(f"O maior numero é {num3}")
#
# if num1 <= num2 and num1 <= num3:
#     print(f"O menor numero é {num1}")
# elif num2 <= num1 and num2 <= num3:
#     print(f"O menor numero é {num2}")
# elif num3 <= num1 and num3 <= num2:
#     print(f"O menor numero é {num3}")

# maior = num1
# if num2 >= num1 and num2 >= num3:
#     maior = num2
# if num3 >= num1 and num3 >= num2:
#     maior = num3
#
# menor = num1
# if num2 >= num1 and num2 >= num3:
#     maior = num2
# if num3 >= num1 and num3 >= num2:
#     maior = num3

# print(maior)
# print(menor)
#
# ex:3
# salario=float(input("digite o salario em reais: "))
# if salario > 1250:
#     percentual = 10
# else:
#     percentual = 15
#
# calculo_salario = salario * (percentual / 100)
# novo_salario = salario + calculo_salario
#
# print (f"Salario anterior R$: {salario:.2f}")
# print (f"percentual foi de {percentual}%")
# print (f"valor do aumento R$: {calculo_salario:.2f}")
# print (f"novo salario R$: {novo_salario:.2f}")
#
# Ex:4
# distancia = int(input("Digite a distância em KM: "))
# if distancia <= 200:
#     preco = 0.50
# else :
#     preco = 0.45
# valor = distancia * preco
# print (f"O valor da passagem é de R${valor:.2f}")
#
# EX:5
# num1 = float(input("digite o primeiro numero: "))
# num2 = float(input("digite o segundo numero: "))
# operacao = input("digite o operacao a realizar (+, -, * ou /)")
#
# if operacao == "+":
#     calculo = num1 + num2
# elif operacao == "*":
#     calculo = num1 * num2
# elif operacao == "/":
#     calculo = num1 / num2
# elif operacao == "-":
#     calculo = num1 - num2
# else:
#     print("operacao invalida")
#     operacao = 0
# print(f"Resultado: {calculo}")
#
#
# EX:6
# valor_casa = float(input("Digite o valor da casa: "))
# salario = float(input("Digite o salario: "))
# anos = int(input("digite a quantidade de anos: "))
# prestacao = valor_casa / (anos * 12)
# if prestacao <= salario * 0.3:
#     print (f"O valor da prestacao sera de R$ {prestacao:.2f}")
# else:
#     print(f"Imprestimo nao aprovado")
#
# EX7
# kwh = float(input("Digite a quantidade de KWh: "))
# tipo = (input("Digite o tipo de instalação: (R,I,C"))
# if tipo == "R":
#     if kwh <= 500:
#         preco = 0.40
#     else :
#         preco =  0.65
# elif tipo == "I":
#     if kwh <= 1000:
#         preco = 0.55
#     else :
#         preco = 0.60
# elif tipo == "C":
#     if kwh <= 5000:
#         preco = 0.55
#     else :
#         preco = 0.60
# else :
#     preco = 0
#     print("Tipo de instalacao desconecida!")
# custo = kwh * preco
# print(f"O preco a pagar pelo fornecimento de energia elétrica é de: {custo:.2f}")
#
#
# # EX:8
# nota1 = float(input("Digite a 1ª nota: "))
# nota2 = float(input("Digite a 2ª nota: "))
# media = (nota1 + nota2) / 2
# if media >= 6:
#     print("Aprovado!")
# else:
#     print("Reprovado!")
#
# # EX9
# nota1 = float(input("Digite a 1ª nota: "))
# nota2 = float(input("Digite a 2ª nota: "))
# media = (nota1 + nota2) / 2
# if media >= 6:
#     print("Aprovado!")
# elif media >= 4 and media <6:
#     print("Exame!")
# else:
#     print("Reprovado!")

# n1 = float(input(""))
# n2 = float(input(""))
# op = input("operação: + - * /")
# if op == "+" :
#     res = n1 + n2
# elif op == "-" :
#     res = n1 - n2
# elif op == "*" :
#     res = n1 * n2
# elif op == "/" :
#     res = n1 / n2
# else :
#     res = None
# if res is None :
#     print ("operacao invalida")
# else :
#     print (f"resultado: {res}")

