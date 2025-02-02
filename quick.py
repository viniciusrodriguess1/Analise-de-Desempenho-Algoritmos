import time
import random

def quicksort(array):
    if len(array) <= 1:
        return array
    pivo = array[0]
    menores = [x for x in array[1:] if x <= pivo]
    maiores = [x for x in array[1:] if x > pivo]
    return quicksort(menores) + [pivo] + quicksort(maiores)

random.seed(42)
tamanhos = [10_000, 50_000, 100_000]

for tamanho in tamanhos:
    dados = [random.randint(1, 1000000) for _ in range(tamanho)]
    inicio = time.time()
    quicksort(dados)
    fim = time.time()
    print(f"QuickSort ({tamanho} elementos): {fim - inicio:.6f} segundos")
