import time
import random
import psutil
import os

def medir_memoria():
    processo = psutil.Process(os.getpid())
    return processo.memory_info().rss / 1024 / 1024  # em MB

def quicksort(array):
    if len(array) <= 1:
        return array
    pivo = array[0]
    menores = [x for x in array[1:] if x <= pivo]
    maiores = [x for x in array[1:] if x > pivo]
    return quicksort(menores) + [pivo] + quicksort(maiores)

# Definição da seed para garantir reprodutibilidade dos testes
random.seed(42)
tamanhos = [10_000, 50_000, 100_000]

for tamanho in tamanhos:
    # Dados de entrada
    dados = [random.randint(1, 1000000) for _ in range(tamanho)]
    
    # Medindo a memória antes da execução
    memoria_inicial = medir_memoria()
    
    # QuickSort
    inicio = time.time()
    quicksort(dados)
    fim = time.time()
    memoria_final = medir_memoria()
    
    print(f"QuickSort ({tamanho} elementos): {fim - inicio:.6f} segundos | Memória: {memoria_final - memoria_inicial:.6f} MB")
