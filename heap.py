import time
import random
import tracemalloc
import heapq

# Função HeapSort
def heap_sort(array):
    heapq.heapify(array)
    return [heapq.heappop(array) for _ in range(len(array))]

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

# Teste para HeapSort
for tamanho in tamanhos:
    dados = [random.randint(1, 1000000) for _ in range(tamanho)]
    
    # Medindo a memória e o tempo de execução para HeapSort
    memoria_heap = medir_memoria(heap_sort, dados)
    print(f"HeapSort ({tamanho} elementos): Memória: {memoria_heap:.6f} KB")
