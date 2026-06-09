nome_missao = "Ares Sentinel"
nome_equipe = "Equipe 07"

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

dados_missao = [
    [25, 94, 91, 97, 92],
    [28, 82, 76, 94, 86],
    [32, 67, 59, 91, 73],
    [37, 48, 42, 86, 58],
    [40, 26, 18, 77, 34],
    [35, 54, 31, 83, 49]
]


def analisar_temperatura(temperatura):
    if temperatura < 18:
        return "ATENÇÃO", 1, "Temperatura abaixo do ideal"
    elif temperatura <= 30:
        return "NORMAL", 0, "Temperatura estável"
    elif temperatura <= 35:
        return "ATENÇÃO", 1, "Temperatura elevada"
    else:
        return "CRÍTICO", 2, "Risco de superaquecimento"


def analisar_comunicacao(comunicacao):
    if comunicacao < 30:
        return "CRÍTICO", 2, "Comunicação com a base em nível crítico"
    elif comunicacao <= 59:
        return "ATENÇÃO", 1, "Comunicação instável"
    else:
        return "NORMAL", 0, "Comunicação estável"


def analisar_bateria(bateria):
    if bateria < 20:
        return "CRÍTICO", 2, "Bateria em nível crítico"
    elif bateria <= 49:
        return "ATENÇÃO", 1, "Bateria abaixo do recomendado"
    else:
        return "NORMAL", 0, "Energia estável"


def analisar_oxigenio(oxigenio):
    if oxigenio < 80:
        return "CRÍTICO", 2, "Oxigênio em nível crítico"
    elif oxigenio <= 89:
        return "ATENÇÃO", 1, "Oxigênio abaixo do ideal"
    else:
        return "NORMAL", 0, "Oxigênio adequado"


def analisar_estabilidade(estabilidade):
    if estabilidade < 40:
        return "CRÍTICO", 2, "Estabilidade operacional crítica"
    elif estabilidade <= 69:
        return "ATENÇÃO", 1, "Estabilidade operacional reduzida"
    else:
        return "NORMAL", 0, "Estabilidade operacional adequada"


def classificar_ciclo(pontuacao):
    if pontuacao <= 2:
        return "MISSÃO ESTÁVEL"
    elif pontuacao <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


def gerar_recomendacao(pontuacao, riscos_area):
    if pontuacao <= 2:
        return "Manter operação normal e continuar monitoramento."

    maior_risco = max(riscos_area)

    if maior_risco == riscos_area[0]:
        return "Verificar controle térmico da missão."
    elif maior_risco == riscos_area[1]:
        return "Tentar restabelecer contato com a base."
    elif maior_risco == riscos_area[2]:
        return "Ativar modo de economia de energia."
    elif maior_risco == riscos_area[3]:
        return "Acionar protocolo de suporte à vida."
    elif maior_risco == riscos_area[4]:
        return "Reduzir operações não essenciais."
    else:
        return "Monitorar sistemas em atenção e preparar plano de contingência."


def analisar_tendencia(riscos_ciclos):
    primeiro_risco = riscos_ciclos[0]
    ultimo_risco = riscos_ciclos[-1]

    if ultimo_risco > primeiro_risco:
        return "A missão apresentou tendência de piora."
    elif ultimo_risco < primeiro_risco:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável em relação ao início."


def identificar_area_mais_afetada(riscos_acumulados_area):
    maior_risco = max(riscos_acumulados_area)
    indice_area = riscos_acumulados_area.index(maior_risco)

    return areas_monitoradas[indice_area]


def calcular_media_coluna(indice_coluna):
    soma = 0

    for ciclo in dados_missao:
        soma += ciclo[indice_coluna]

    return soma / len(dados_missao)


def gerar_relatorio_final(riscos_ciclos, riscos_acumulados_area):
    media_temperatura = calcular_media_coluna(0)
    media_comunicacao = calcular_media_coluna(1)
    media_bateria = calcular_media_coluna(2)
    media_oxigenio = calcular_media_coluna(3)
    media_estabilidade = calcular_media_coluna(4)

    maior_risco = max(riscos_ciclos)
    ciclo_mais_critico = riscos_ciclos.index(maior_risco) + 1

    risco_medio = sum(riscos_ciclos) / len(riscos_ciclos)

    quantidade_ciclos_criticos = 0

    for risco in riscos_ciclos:
        if risco >= 6:
            quantidade_ciclos_criticos += 1

    tendencia = analisar_tendencia(riscos_ciclos)
    area_mais_afetada = identificar_area_mais_afetada(riscos_acumulados_area)

    classificacao_final = classificar_ciclo(risco_medio)

    print("=" * 60)
    print("RELATÓRIO FINAL DA MISSÃO")
    print("=" * 60)
    print(f"Missão: {nome_missao}")
    print(f"Equipe: {nome_equipe}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print(f"Média de temperatura: {media_temperatura:.2f} °C")
    print(f"Média de comunicação: {media_comunicacao:.2f}%")
    print(f"Média de bateria: {media_bateria:.2f}%")
    print(f"Média de oxigênio: {media_oxigenio:.2f}%")
    print(f"Média de estabilidade: {media_estabilidade:.2f}%")
    print(f"Ciclo mais crítico: Ciclo {ciclo_mais_critico}")
    print(f"Maior pontuação de risco: {maior_risco}")
    print(f"Risco médio da missão: {risco_medio:.2f}")
    print(f"Quantidade de ciclos críticos: {quantidade_ciclos_criticos}")

    print("Tendência da missão:")
    print(tendencia)

    print("Pontuação acumulada por área:")

    for i in range(len(areas_monitoradas)):
        print(f"{areas_monitoradas[i]}: {riscos_acumulados_area[i]} pontos")

    print("Área mais afetada:")
    print(area_mais_afetada)

    print("Classificação final da missão:")
    print(classificacao_final)

    print("Conclusão:")

    if classificacao_final == "MISSÃO ESTÁVEL":
        print("A missão está operando de forma segura, com riscos baixos e sistemas controlados.")
    elif classificacao_final == "MISSÃO EM ATENÇÃO":
        print("A missão apresentou instabilidade relevante durante a operação. A equipe deve manter o plano de contingência ativo.")
    else:
        print("A missão apresentou risco elevado. É necessário ativar protocolos de emergência e priorizar os sistemas críticos.")


def executar_monitoramento():
    riscos_ciclos = []
    riscos_acumulados_area = [0, 0, 0, 0, 0]

    print("=" * 60)
    print("MISSION CONTROL AI")
    print("=" * 60)
    print(f"Missão: {nome_missao}")
    print(f"Equipe: {nome_equipe}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print("=" * 60)

    for indice, ciclo in enumerate(dados_missao):
        temperatura = ciclo[0]
        comunicacao = ciclo[1]
        bateria = ciclo[2]
        oxigenio = ciclo[3]
        estabilidade = ciclo[4]

        status_temp, risco_temp, mensagem_temp = analisar_temperatura(temperatura)
        status_com, risco_com, mensagem_com = analisar_comunicacao(comunicacao)
        status_bat, risco_bat, mensagem_bat = analisar_bateria(bateria)
        status_oxi, risco_oxi, mensagem_oxi = analisar_oxigenio(oxigenio)
        status_est, risco_est, mensagem_est = analisar_estabilidade(estabilidade)

        riscos_area = [risco_temp, risco_com, risco_bat, risco_oxi, risco_est]

        pontuacao_ciclo = sum(riscos_area)
        classificacao = classificar_ciclo(pontuacao_ciclo)
        recomendacao = gerar_recomendacao(pontuacao_ciclo, riscos_area)

        riscos_ciclos.append(pontuacao_ciclo)

        for i in range(len(riscos_acumulados_area)):
            riscos_acumulados_area[i] += riscos_area[i]

        print(f"CICLO {indice + 1}")
        print("-" * 60)
        print(f"Temperatura: {temperatura} °C | {status_temp} | {mensagem_temp}")
        print(f"Comunicação: {comunicacao}% | {status_com} | {mensagem_com}")
        print(f"Bateria: {bateria}% | {status_bat} | {mensagem_bat}")
        print(f"Oxigênio: {oxigenio}% | {status_oxi} | {mensagem_oxi}")
        print(f"Estabilidade: {estabilidade}% | {status_est} | {mensagem_est}")
        print(f"Pontuação de risco do ciclo: {pontuacao_ciclo}")
        print(f"Classificação do ciclo: {classificacao}")
        print(f"Recomendação: {recomendacao}")
        print()

    gerar_relatorio_final(riscos_ciclos, riscos_acumulados_area)


executar_monitoramento()