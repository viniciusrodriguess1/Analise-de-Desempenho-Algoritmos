import matplotlib.pyplot as plt
import numpy as np

# Dados de tempo de execução (em segundos) para cada entrada e algoritmo
algoritmos = ['Quick', 'Merge', 'Heap']
entrada_1 = [ 0.071962, 0.168000, 0.009981]  # Tempos de execução para entrada 1
entrada_2 = [0.313981,  1.200390, 0.059011]  # Tempos de execução para entrada 2
entrada_3 = [0.680006, 2.370053, 0.131999]  # Tempos de execução para entrada 3

# Função para criar os gráficos de barras
def plot_execucao(ax, entrada, titulo, cor):
    ax.bar(algoritmos, entrada, color=cor)
    ax.set_title(titulo)
    ax.set_xlabel('Algoritmo')
    ax.set_ylabel('Tempo (segundos)')

# Determinando o limite máximo para o eixo Y
y_max = max(max(entrada_1), max(entrada_2), max(entrada_3)) * 1.1  # 10% a mais para margem

# Gráfico 1: Tempo de execução para cada entrada
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Criando os gráficos para cada entrada
plot_execucao(axs[0], entrada_1, 'Tempo de Execução - Entrada 1', 'blue')
plot_execucao(axs[1], entrada_2, 'Tempo de Execução - Entrada 2', 'green')
plot_execucao(axs[2], entrada_3, 'Tempo de Execução - Entrada 3', 'red')

# Definindo o mesmo limite para o eixo Y em todos os gráficos
for ax in axs:
    ax.set_ylim(0, y_max)

plt.tight_layout()
plt.show()

# Gráfico 2: Tempo de execução geral (algoritmo e entrada)
entrada_combinada = [entrada_1, entrada_2, entrada_3]
entradas = ['Entrada 1', 'Entrada 2', 'Entrada 3']

fig, ax = plt.subplots(figsize=(8, 6))

# Plotando barras para cada entrada
posicoes = np.arange(len(algoritmos))  # Posições para as barras
largura = 0.2  # Largura das barras
for i, entrada in enumerate(entrada_combinada):
    ax.bar(posicoes + i * largura, entrada, largura, label=f'Entrada {i + 1}')

ax.set_title('Tempo de Execução Geral (Algoritmo e Entrada)')
ax.set_xlabel('Algoritmo e Entrada')
ax.set_ylabel('Tempo (segundos)')
ax.set_xticks(posicoes + largura)
ax.set_xticklabels(algoritmos)
ax.legend()

# Definindo o mesmo limite para o eixo Y
ax.set_ylim(0, y_max)

plt.tight_layout()
plt.show()
