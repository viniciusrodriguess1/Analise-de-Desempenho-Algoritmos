import time
import random
import heapq

def heap_sort(array):
    heapq.heapify(array)
    return [heapq.heappop(array) for _ in range(len(array))]

random.seed(42)
tamanhos = [10_000, 50_000, 100_000]

for tamanho in tamanhos:
    dados = [random.randint(1, 1000000) for _ in range(tamanho)]
    inicio = time.time()
    heap_sort(dados)
    fim = time.time()
    print(f"HeapSort ({tamanho} elementos): {fim - inicio:.6f} segundos")
