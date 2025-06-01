# A GLOBAL SOLUTION ESTÁ DISPONÍVEL NO ANEXO.
# O ARQUIVO .PY DEVE SER POSTADO ATÉ O DIA 06/06/2025 (SEXTA-FEIRA), ÀS 23H55.
# NA PRIMEIRA LINHA DO CÓDIGO, INCLUA O LINK DO VÍDEO COMO COMENTÁRIO.
# NA SEGUNDA LINHA, TAMBÉM COMO COMENTÁRIO, INSIRA OS NOMES COMPLETOS DOS INTEGRANTES DO GRUPO.
#
# A ENTREGA DEVE SER FEITA POR APENAS UM INTEGRANTE DO GRUPO (MÁXIMO DE 3 ALUNOS) NO PORTAL DO ALUNO, NA SEÇÃO ENTREGA DE TRABALHOS.
#
# Requisitos:
# Leitura de Dados:
# Você terá uma série de leituras (simuladas) de sensores, cada uma representando:
# - Velocidade do vento (km/h),
# - Direção do vento (graus de 0 a 360),
# - Umidade relativa do ar (%).
# Condições Críticas:
# - Velocidade do vento acima de 75 km/h;
# - Variação da direção do vento superior a 100° entre leituras consecutivas;
# - Umidade abaixo de 20% ou acima de 95%.
# Emissão de Alertas:
# - Condição crítica: "Alerta: Condições de vento severo identificadas!"
# - Caso contrário: "Sistema estável. Nenhuma anomalia detectada."
# Cálculo de Médias e Desvio Padrão:
# - Média e desvio padrão da velocidade do vento, direção e umidade.
# Estado Geral do Ambiente:
# - Mais de 40% das leituras críticas: "Estado Geral: Instável";
# - Caso contrário: "Estado Geral: Estável".
# Análise Histórica:
# - Máximos e mínimos dos parâmetros;
# - Tendência da velocidade do vento.
# Tarefas:
# - Entrada dos dados simulados;
# - Verificação de condições críticas, cálculos e análise;
# - Impressão de alertas e análises.
#
#
# Gustavo Zibini Belizario
# Gabriel

# Listas para armazenar as leituras
velocidades = []
direcoes = []
umidades = []

print("Insira os dados do sensor. Digite 'sair' a qualquer momento para encerrar.\n")

while True:
    # Ler velocidade do vento
    vel_input = input("Velocidade do vento (km/h) ou 'sair' para encerrar: ")
    if vel_input.lower() == "sair":
        break
    try:
        vel = float(vel_input)
    except ValueError:
        print("Entrada inválida. Insira um número para a velocidade ou 'sair'.")
        continue

    # Ler direção do vento com validação de 0 a 360
    while True:
        dir_input = input("Direção do vento (0–360°) ou 'sair' para encerrar: ")
        if dir_input.lower() == "sair":
            vel = None  # marca para não salvar esta leitura parcial
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
        break  # usuário digitou 'sair' durante a direção

    # Ler umidade relativa do ar com validação de 0 a 100
    while True:
        umid_input = input("Umidade relativa do ar (0–100%) ou 'sair' para encerrar: ")
        if umid_input.lower() == "sair":
            vel = None  # marca para não salvar esta leitura parcial
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
        break  # usuário digitou 'sair' durante a umidade

    # Adiciona aos arrays após todas as validações
    velocidades.append(vel)
    direcoes.append(dir_vento)
    umidades.append(umid)

    # Exibe a leitura atual para confirmacao
    idx = len(velocidades)
    print(f"\nLeitura {idx} registrada:")
    print(f"  Velocidade = {vel:.1f} km/h")
    print(f"  Direção   = {dir_vento:.1f}°")
    print(f"  Umidade   = {umid:.1f}%\n")

print("\nPrograma encerrado. Todas as leituras registradas:")

if velocidades:
    for i in range(len(velocidades)):
        print(f"Leitura {i+1}: Vel={velocidades[i]:.1f} km/h, Dir={direcoes[i]:.1f}°, Umid={umidades[i]:.1f}%")
else:
    print("Nenhuma leitura foi registrada.")