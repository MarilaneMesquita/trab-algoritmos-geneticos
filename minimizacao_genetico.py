import random
import math

def funcao_objetivo(x):
    return x**3 - 6*x + 14

def binario_para_real(binario, minimo, maximo):
    valor_decimal = int(''.join(map(str, binario)), 2)
    escala = (maximo - minimo) / (2**len(binario) - 1)
    return minimo + valor_decimal * escala

def inicializar_populacao(tamanho_populacao, bits):
    return [ [random.randint(0,1) for _ in range(bits)] for _ in range(tamanho_populacao) ]

def calcular_fitness(populacao, minimo, maximo):
    fitnesses = []
    for individuo in populacao:
        x = binario_para_real(individuo, minimo, maximo)
        fitness = funcao_objetivo(x)
        fitnesses.append(fitness)
    return fitnesses

def selecao_torneio(populacao, fitnesses):
    participantes = random.sample(list(zip(populacao, fitnesses)), 3)
    participantes.sort(key=lambda x: x[1])  # Minimização
    return participantes[0][0]

def crossover(pai1, pai2, pontos_corte):
    filho1, filho2 = pai1.copy(), pai2.copy()
    if pontos_corte == 1:
        ponto = random.randint(1, len(pai1)-1)
        filho1 = pai1[:ponto] + pai2[ponto:]
        filho2 = pai2[:ponto] + pai1[ponto:]
    elif pontos_corte == 2:
        ponto1 = random.randint(1, len(pai1)-2)
        ponto2 = random.randint(ponto1+1, len(pai1)-1)
        filho1 = pai1[:ponto1] + pai2[ponto1:ponto2] + pai1[ponto2:]
        filho2 = pai2[:ponto1] + pai1[ponto1:ponto2] + pai2[ponto2:]
    return filho1, filho2

def mutacao(cromossomo, taxa_mutacao):
    for i in range(len(cromossomo)):
        if random.random() < taxa_mutacao:
            cromossomo[i] = 1 - cromossomo[i]
    return cromossomo

def algoritmo_genetico(minimo, maximo, bits, tamanho_populacao, geracoes, taxa_mutacao, pontos_corte, metodo_selecao, elitismo_percentual):
    populacao = inicializar_populacao(tamanho_populacao, bits)
    historico_melhores = []

    numero_elitismo = int(elitismo_percentual * tamanho_populacao)
    for geracao in range(geracoes):
        fitnesses = calcular_fitness(populacao, minimo, maximo)
        nova_populacao = []

        # Elitismo
        populacao_com_fitness = list(zip(populacao, fitnesses))
        populacao_com_fitness.sort(key=lambda x: x[1])  # Minimização
        elite = [individuo for individuo, fitness in populacao_com_fitness[:numero_elitismo]]
        nova_populacao.extend(elite)

        while len(nova_populacao) < tamanho_populacao:
            if metodo_selecao == 'torneio':
                pai1 = selecao_torneio(populacao, fitnesses)
                pai2 = selecao_torneio(populacao, fitnesses)
            else:
                # Implementar roleta viciada se necessário
                pai1 = selecao_torneio(populacao, fitnesses)
                pai2 = selecao_torneio(populacao, fitnesses)
            filho1, filho2 = crossover(pai1, pai2, pontos_corte)
            filho1 = mutacao(filho1, taxa_mutacao)
            filho2 = mutacao(filho2, taxa_mutacao)
            nova_populacao.extend([filho1, filho2])

        populacao = nova_populacao[:tamanho_populacao]
        fitnesses = calcular_fitness(populacao, minimo, maximo)
        melhor_fitness = min(fitnesses)
        melhor_individuo = populacao[fitnesses.index(melhor_fitness)]
        melhor_x = binario_para_real(melhor_individuo, minimo, maximo)
        historico_melhores.append((melhor_x, melhor_fitness))

        print(f"Geração {geracao+1}: x = {melhor_x}, f(x) = {melhor_fitness}")

    # Retorna o melhor resultado encontrado
    melhor_resultado = min(historico_melhores, key=lambda x: x[1])
    return melhor_resultado

if __name__ == "__main__":
    minimo = -10
    maximo = 10
    bits = 16  # Precisão de representação
    tamanho_populacao = 10
    geracoes = 100
    taxa_mutacao = 0.01
    pontos_corte = 2  # Pode ser 1 ou 2
    metodo_selecao = 'torneio'  # Ou 'roleta'
    elitismo_percentual = 0.1  # 10% da população

    melhor_x, melhor_fitness = algoritmo_genetico(
        minimo, maximo, bits, tamanho_populacao, geracoes,
        taxa_mutacao, pontos_corte, metodo_selecao, elitismo_percentual
    )

    print(f"\nMelhor solução encontrada: x = {melhor_x}, f(x) = {melhor_fitness}")
