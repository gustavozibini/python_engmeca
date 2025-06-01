#link do vídeo:
# Gustavo Zibini Belizario RM:561376
# Gabriel Bastos Nhoncanse RM:562022
# 1EMR




#---------------------------------listas para armazenar as leituras---------------------------------
#onde vai armazenar as leituras
velocidades = []
direcoes = []
umidades = []

# para leituras críticas: vai armazenar um boolean de verdadeiro ou falso indicando se a leitura foi considerada critica
criticos = []

print("Insira os dados do sensor. Digite 'sair' a qualquer momento para encerrar.\n")

while True:
#---------------------------------ler velocidade do vento---------------------------------
#loop principal de leitura: solicita a velocidade.
#foi adicionado um "lower" para aceitar diversos tipos de Sair (sair SAIR SaIr, etc).
#o break está enviando diretamente para a parte final do programa, se for acionado nao irá armazenar a leitura.
#vel_input serve para converter a variavel em float, se ela nao for convertida irá apresentar erro e pedir para digitar novamente.

    vel_input = input("Velocidade do vento (km/h) ou 'sair' para encerrar: ")
    if vel_input.lower() == "sair":
        break
    try:
        vel = float(vel_input)
    except ValueError:
        print("Entrada inválida. Insira um número para a velocidade ou 'sair'.")
        continue

#---------------------------------ler direcao do vento com validacao de 0 a 360---------------------------------
# loop para solicitacao de direcao: o número deve ser entre 0 até 360, caso contrario solicita que o usuário informe um valor valido.
# é feita a tentativa de conversao para float se der erro solicita novamente o valor
# se o valor for entre 0 e 360 ativa break e avanca no código
# se o usuário digitar "sair" a variavel vel solicitado anteriormente é definida como "None"
# e é ativado "Break" para nao salvar a leitura e seguir para o final do código.

    while True:
        dir_input = input("Direção do vento (0–360°) ou 'sair' para encerrar: ")
        if dir_input.lower() == "sair":
            vel = None  #---------------------------------marca para nao salvar esta leitura
            break
        try:
            dir_vento = float(dir_input)
        except ValueError:
            print("Entrada inválida. Insira um número para a direção ou 'sair'.")
            continue

        if 0 <= dir_vento <= 360:
            break
        else:
            print("valor invalido. Digite um valor entre 0 e 360.")

    if vel is None:
        break  #---------------------------------usuario digitou 'sair' durante a direcao

#---------------------------------ler umidade do ar com validacao de 0 a 100---------------------------------
# para a umidade seguimos o mesmo padrao do anterior:
# numero entre 0 até 100
# convertido para float para poder avancar, caso contrario digite novamente
# sair avanca para o final
    while True:
        umid_input = input("Umidade relativa do ar (0–100%) ou 'sair' para encerrar: ")
        if umid_input.lower() == "sair":
            vel = None  #---------------------------------marca para não salvar esta leitura
            break
        try:
            umid = float(umid_input)
        except ValueError:
            print("Entrada inválida. Insira um número para a umidade ou 'sair'.")
            continue

        if 0 <= umid <= 100:
            break
        else:
            print("valor invalido. Digite um valor entre 0 e 100.")

    if vel is None:
        break  #---------------------------------digitou 'sair' durante a umidade

#---------------------------------adiciona aos arrays apos todas as validações---------------------------------
#esses dois alertas podem aparecer pois dependendo do caminho de execucao no caso do caminho do sair que aciona o "break" elas podem nunca serem utilizadas
    velocidades.append(vel)
    direcoes.append(dir_vento)
    umidades.append(umid)

#---------------------------------verifica condicoes criticas---------------------------------
    #primeira validacao: velocidade > 75 km/h nesta condicao aciona alerta
    speed_crit = vel > 75

    #segunda condicao: variacao de direcao > 100°
    #aqui também garante a circularidade ex: valor de 350 e 10 seja de 20 nao de 340
    #essa condicao também so irá acionar caso exista pelo menos 2 medicoes na lista
    if len(direcoes) >= 2:
        prev_dir = direcoes[-2]
        curr_dir = direcoes[-1]
        delta = abs(curr_dir - prev_dir)
        var_dir = delta if delta <= 180 else 360 - delta
        dir_crit = var_dir > 100
    else:
        dir_crit = False

    #terceira condicao: umidade < 20% ou > 95%
    #menor que 20 = critico maior que 95 = critico
    humidity_crit = (umid < 20) or (umid > 95)

    #se qualquer leitura for critica marca na lista boolean logo no proximo comentario
    is_critical = speed_crit or dir_crit or humidity_crit
    criticos.append(is_critical)

#---------------------------------exibe alerta ou sistema estevel---------------------------------
#se a leitura de critica for verdadeira irá imprimir a mensagem de condicao severa.
    if is_critical:
        print("\nAlerta: Condições de vento severo identificadas!\n")
    else:
        print("\nSistema estável. Nenhuma anomalia detectada.\n")

#---------------------------------exibe a leitura atual para confirmacao---------------------------------
# idx = index
    idx = len(velocidades)
    print(f"Leitura {idx} registrada:")
    print(f"  Velocidade = {vel:.1f} km/h")
    print(f"  Direção   = {dir_vento:.1f}°")
    print(f"  Umidade   = {umid:.1f}%\n")

print("\nPrograma encerrado. Todas as leituras registradas:\n")

if velocidades:
# ---------------------------------imprime todas as leituras---------------------------------
#apos acionamento do "break" o programa irá exibir todas as leituras coletadas
# para o o range em seguida ira varrer todos os indices de leitura de 0 até n (n é o numero de leituras)
    for i in range(len(velocidades)):
        status = "Crítico" if criticos[i] else "OK"
        print(f"Leitura {i+1}: Vel={velocidades[i]:.1f} km/h, Dir={direcoes[i]:.1f}°, Umid={umidades[i]:.1f}% → {status}")

    n = len(velocidades)

#---------------------------------calculo de medias---------------------------------
    mean_vel = sum(velocidades) / n
    mean_dir = sum(direcoes) / n
    mean_umid = sum(umidades) / n

#---------------------------------calculo de desvio padrao---------------------------------
    var_vel = sum((x - mean_vel) ** 2 for x in velocidades) / n
    std_vel = var_vel ** 0.5

    var_dir = sum((x - mean_dir) ** 2 for x in direcoes) / n
    std_dir = var_dir ** 0.5

    var_umid = sum((x - mean_umid) ** 2 for x in umidades) / n
    std_umid = var_umid ** 0.5

#---------------------------------maximos e minimos---------------------------------
    max_vel = max(velocidades)
    min_vel = min(velocidades)
    max_dir = max(direcoes)
    min_dir = min(direcoes)
    max_umid = max(umidades)
    min_umid = min(umidades)

#---------------------------------tendencia da velocidade (comparando primeiro e ultimo valor)---------------------------------
    if velocidades[-1] > velocidades[0]:
        tendencia = "crescente"
    elif velocidades[-1] < velocidades[0]:
        tendencia = "decrescente"
    else:
        tendencia = "sem variação"

#---------------------------------estado geral do ambiente---------------------------------
    perc_criticos = (sum(criticos) / n) * 100
    estado_geral = "Instável" if perc_criticos > 40 else "Estável"

#---------------------------------Impressao dos resultados estatisticos e analise historica---------------------------------
    print("\n--- Estatísticas Gerais ---")
    print(f"Média da velocidade: {mean_vel:.2f} km/h")
    print(f"Desvio padrão da velocidade: {std_vel:.2f}")
    print(f"Média da direção: {mean_dir:.2f}°")
    print(f"Desvio padrão da direção: {std_dir:.2f}")
    print(f"Média da umidade: {mean_umid:.2f}%")
    print(f"Desvio padrão da umidade: {std_umid:.2f}")

    print("\n--- Valores Máximos e Mínimos ---")
    print(f"Velocidade → Máx: {max_vel:.1f} km/h, Mín: {min_vel:.1f} km/h")
    print(f"Direção  → Máx: {max_dir:.1f}°, Mín: {min_dir:.1f}°")
    print(f"Umidade  → Máx: {max_umid:.1f}%, Mín: {min_umid:.1f}%")

    print("\n--- Tendência da Velocidade do Vento ---")
    print(f"Tendência geral: {tendencia}")

    print("\n--- Estado Geral do Ambiente ---")
    print(f"Leituras críticas: {sum(criticos)} de {n} ({perc_criticos:.1f}%)")
    print(f"Estado Geral: {estado_geral}")

else:
    print("Nenhuma leitura foi registrada.")