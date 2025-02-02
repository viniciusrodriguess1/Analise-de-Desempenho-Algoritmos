import time
import random
import tracemalloc

def heap_sort(array):
    import heapq
    heapq.heapify(array)
    return [heapq.heappop(array) for _ in range(len(array))]

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

def quicksort(array):
    if len(array) <= 1:
        return array
    pivo = array[0]
    menores = [x for x in array[1:] if x <= pivo]
    maiores = [x for x in array[1:] if x > pivo]
    return quicksort(menores) + [pivo] + quicksort(maiores)

# Função para medir o uso de memória durante a execução
def medir_memoria(func, dados):
    tracemalloc.start()  # Começa a rastrear o uso de memória
    inicio = time.time()
    func(dados)  # Executa o algoritmo
    fim = time.time()
    current, peak = tracemalloc.get_traced_memory()  # Obtém o uso de memória atual e o pico
    tracemalloc.stop()  # Para o rastreamento de memória
    return peak / 1024  # Retorna o pico de memória em KB

# Definição da seed para garantir reprodutibilidade dos testes
random.seed(42)
tamanhos = [10_000, 50_000, 100_000]

for tamanho in tamanhos:
    # Dados de entrada
    dados = [random.randint(1, 1000000) for _ in range(tamanho)]
    
    # Medindo a memória e o tempo de execução
    memoria = medir_memoria(quicksort, dados)
    print(f"QuickSort ({tamanho} elementos): Memória: {memoria:.6f} KB")
