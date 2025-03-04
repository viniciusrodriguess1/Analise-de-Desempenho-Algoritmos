import time
import random
import tracemalloc

# Função MergeSort
def merge_sort(array):
    if len(array) <= 1:
        return array
    meio = len(array) // 2
    esquerda = merge_sort(array[:meio])
    direita = merge_sort(array[meio:])
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

# Função para medir o uso de memória durante a execução
def medir_memoria(func, dados):
    tracemalloc.start()  # Começa a rastrear o uso de memória
    inicio = time.time()
    func(dados)  # Executa o algoritmo
    fim = time.time()
    current, peak = tracemalloc.get_traced_memory()  # Obtém o uso de memória atual e o pico
    tracemalloc.stop()  # Para o rastreamento de memória
    return peak / 1024, fim - inicio  # Retorna o pico de memória em KB e o tempo de execução

# Definição da seed para garantir reprodutibilidade dos testes
random.seed(42)
tamanhos = [10_000, 50_000, 100_000]

# Teste para MergeSort
for tamanho in tamanhos:
    dados = [random.randint(1, 1000000) for _ in range(tamanho)]
    
    # Medindo a memória e o tempo de execução para MergeSort
    memoria_merge, tempo_merge = medir_memoria(merge_sort, dados)
    print(f"MergeSort ({tamanho} elementos): Tempo: {tempo_merge:.6f} segundos | Memória: {memoria_merge:.6f} KB")
