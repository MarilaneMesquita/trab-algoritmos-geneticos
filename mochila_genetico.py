# mochila_genetico.py

import random
import copy

def inicializar_populacao(tamanho_populacao, num_itens):
    return [ [random.randint(0,1) for _ in range(num_itens)] for _ in range(tamanho_populacao) ]

def calcular_fitness(cromossomo, itens, peso_maximo):
    peso_total = valor_total = 0
    for i in range(len(cromossomo)):
        if cromossomo[i] == 1:
            peso_total += itens[i][0]
            valor_total += itens[i][1]
    if peso_total > peso_maximo:
        return 0  # Penalidade por exceder o peso
    else:
        return valor_total

def selecao_roleta(populacao, fitnesses):
    soma_fitness = sum(fitnesses)
    pick = random.uniform(0, soma_fitness)
    current = 0
    for individuo, fitness in zip(populacao, fitnesses):
        current += fitness
        if current > pick:
            return individuo

def crossover(pai1, pai2):
    ponto = random.randint(1, len(pai1)-1)
    filho1 = pai1[:ponto] + pai2[ponto:]
    filho2 = pai2[:ponto] + pai1[ponto:]
    return filho1, filho2

def mutacao(cromossomo, taxa_mutacao=0.01):
    for i in range(len(cromossomo)):
        if random.random() < taxa_mutacao:
            cromossomo[i] = 1 - cromossomo[i]
    return cromossomo

def algoritmo_genetico(itens, peso_maximo, tamanho_populacao, geracoes):
    num_itens = len(itens)
    populacao = inicializar_populacao(tamanho_populacao, num_itens)
    historico_melhores = []

    for geracao in range(geracoes):
        fitnesses = [calcular_fitness(individuo, itens, peso_maximo) for individuo in populacao]
        nova_populacao = []

        for _ in range(tamanho_populacao // 2):
            pai1 = selecao_roleta(populacao, fitnesses)
            pai2 = selecao_roleta(populacao, fitnesses)
            filho1, filho2 = crossover(pai1, pai2)
            filho1 = mutacao(filho1)
            filho2 = mutacao(filho2)
            nova_populacao.extend([filho1, filho2])

        populacao = nova_populacao
        fitnesses = [calcular_fitness(individuo, itens, peso_maximo) for individuo in populacao]
        melhor_fitness = max(fitnesses)
        melhor_individuo = populacao[fitnesses.index(melhor_fitness)]
        historico_melhores.append([melhor_fitness, melhor_individuo])

        print(f"Geração {geracao+1}: Melhor Valor = {melhor_fitness}")

    return historico_melhores

if __name__ == "__main__":
    pesos_e_valores = [[2, 10], [4, 30], [6, 300], [8, 10], [8, 30],
                       [8, 300], [12, 50], [25, 75], [50, 100], [100, 400]]
    peso_maximo = 100
    numero_de_cromossomos = 150
    geracoes = 50

    historico = algoritmo_genetico(pesos_e_valores, peso_maximo, numero_de_cromossomos, geracoes)
    print("\nHistórico dos melhores indivíduos por geração:")
    for i, (fitness, individuo) in enumerate(historico):
        print(f"Geração {i+1}: Valor = {fitness}, Cromossomo = {individuo}")
