# Algoritmos Genéticos: Minimização de Função e Problema da Mochila

Este projeto implementa dois algoritmos genéticos para resolver problemas de otimização:
1. **Minimização de uma função matemática**.
2. **Problema clássico da mochila**.

## Descrição Geral

Algoritmos genéticos são técnicas de otimização baseadas em princípios da evolução biológica, como **seleção natural**, **crossover**, **mutação** e **elitismo**. Estes algoritmos permitem a busca por soluções aproximadas em espaços complexos.

### 1. **Algoritmo Genético para Minimização de Função**

Este algoritmo genético busca o valor de `x` que minimiza a função:

```plaintext
f(x) = x^3 - 6x + 14
```

O valor de `x` está restrito ao intervalo [-10, +10].

### 2. **Algoritmo Genético para o Problema da Mochila**

Neste problema, o objetivo é selecionar um subconjunto de itens com o maior valor total, sem exceder o limite de peso da mochila. Cada item tem um peso e um valor associado.

## Como Executar

### Pré-requisitos

- **Python 3.x**: Certifique-se de que o Python 3 está instalado no seu sistema.

### Instruções

1. **Clone o repositório**:
   - Para obter o código, clone o repositório diretamente do GitHub:
     ```bash
     git clone https://github.com/seu-usuario/seu-repositorio.git
     cd seu-repositorio
     ```

2. **Execute o código**:
   - Para rodar o algoritmo de minimização de função:
     ```bash
     python algoritmo_genetico.py
     ```
   - Para rodar o algoritmo da mochila:
     ```bash
     python mochila_genetico.py
     ```

3. **Saídas esperadas**:
   - O programa exibirá os resultados por geração para ambos os algoritmos. No caso da minimização de função, será exibido o valor de `x` que minimiza a função e o valor da função correspondente. Para o problema da mochila, será exibido o histórico das melhores soluções (valores e itens selecionados) ao longo das gerações.

## Estrutura dos Algoritmos

### 1. Minimização de Função

#### Funcionamento:
1. **Codificação Binária**: O valor de `x` é representado como uma sequência binária, onde a quantidade de bits define a precisão.
2. **Função de Fitness**: Avalia cada cromossomo convertendo-o de binário para um número real e calculando o valor da função \( f(x) = x^3 - 6x + 14 \).
3. **Seleção por Torneio**: Três indivíduos são escolhidos aleatoriamente, e o de menor fitness é selecionado.
4. **Crossover**: Dois pais são cruzados usando 1 ou 2 pontos de corte para gerar dois novos filhos.
5. **Mutação**: Pequenas alterações são feitas nos bits dos cromossomos para manter a diversidade genética.
6. **Elitismo**: As melhores soluções são preservadas em cada geração.

#### Funções Principais:
- **funcao_objetivo(x)**: Calcula o valor de \( f(x) = x^3 - 6x + 14 \).
- **binario_para_real(binario, minimo, maximo)**: Converte um cromossomo binário em um número real dentro do intervalo [-10, +10].
- **inicializar_populacao(tamanho_populacao, bits)**: Gera uma população inicial de cromossomos.
- **calcular_fitness(populacao, minimo, maximo)**: Calcula o fitness de cada indivíduo.
- **selecao_torneio(populacao, fitnesses)**: Seleciona pais para reprodução.
- **crossover(pai1, pai2, pontos_corte)**: Realiza o crossover entre dois pais.
- **mutacao(cromossomo, taxa_mutacao)**: Aplica mutação a um cromossomo.
- **algoritmo_genetico**: Executa o processo completo do algoritmo genético.

### 2. Problema da Mochila

#### Funcionamento:
1. **Codificação Binária**: Cada cromossomo representa uma combinação de itens, onde `1` significa que o item está na mochila e `0` significa que não está.
2. **Função de Fitness**: Calcula o valor total dos itens na mochila, penalizando soluções que excedem o limite de peso.
3. **Seleção por Roleta**: Indivíduos com maior fitness têm maior chance de serem selecionados.
4. **Crossover**: Realizado com um ponto de corte para gerar dois novos indivíduos.
5. **Mutação**: Bits aleatórios dos cromossomos podem ser invertidos, mantendo a diversidade.
6. **Iteração**: O processo é repetido por várias gerações, e o melhor indivíduo de cada geração é armazenado.

#### Funções Principais:
- **inicializar_populacao(tamanho_populacao, num_itens)**: Cria uma população inicial de cromossomos.
- **calcular_fitness(cromossomo, itens, peso_maximo)**: Calcula o fitness baseado no valor total dos itens.
- **selecao_roleta(populacao, fitnesses)**: Seleciona indivíduos para reprodução usando o método da roleta.
- **crossover(pai1, pai2)**: Realiza crossover de um ponto entre dois pais.
- **mutacao(cromossomo, taxa_mutacao)**: Aplica mutação aos bits dos cromossomos.
- **algoritmo_genetico**: Executa o processo completo do algoritmo genético.

## Parâmetros e Configurações

### Para a Minimização de Função:
- **minimo** e **maximo**: Definem o intervalo de valores possíveis para `x` ([-10, +10]).
- **bits**: Define o número de bits usados para representar `x`.
- **tamanho_populacao**: Quantidade de indivíduos por geração.
- **geracoes**: Quantidade de gerações.
- **taxa_mutacao**: Probabilidade de mutação em cada bit do cromossomo.
- **pontos_corte**: Define se o crossover usará 1 ou 2 pontos de corte.
- **metodo_selecao**: Método de seleção (torneio ou roleta).
- **elitismo_percentual**: Percentual da população mantido intacto.

### Para o Problema da Mochila:
- **itens**: Lista de itens com seus pesos e valores. Exemplo:
  ```python
  pesos_e_valores = [[2, 10], [4, 30], [6, 300], [8, 10], [8, 30], [8, 300], [12, 50], [25, 75], [50, 100], [100, 400]]
  ```
- **peso_maximo**: Limite de peso da mochila.
- **tamanho_populacao**: Número de indivíduos por geração.
- **geracoes**: Quantidade de gerações.

## Exemplo de Saída

### Minimização de Função:
```bash
Geração 1: x = -1.234375, f(x) = 9.5087890625
...
Melhor solução encontrada: x = -1.2333984375, f(x) = 9.508396196078062
```

### Problema da Mochila:
```bash
Geração 1: Melhor Valor = 610
Geração 2: Melhor Valor = 650
...
Histórico dos melhores indivíduos por geração:
Geração 1: Valor = 610, Cromossomo = [1, 0, 1, 0, 0, 1, 0, 0, 0, 0]
```

## Conclusão

Neste projeto, vimos como algoritmos genéticos podem ser aplicados para resolver problemas de otimização, como a minimização de uma função matemática e o problema da mochila. Ambos os algoritmos utilizam seleção, crossover e mutação para encontrar soluções aproximadas e eficientes.
