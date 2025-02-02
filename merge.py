import time
import random
import psutil
import os

def medir_memoria():
    processo = psutil.Process(os.getpid())
    return processo.memory_info().rss / 1024 / 1024  # em MB

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

# Definição da seed para garantir reprodutibilidade dos testes
random.seed(42)
tamanhos = [10_000, 50_000, 100_000]

for tamanho in tamanhos:
    # Dados de entrada
    dados = [random.randint(1, 1000000) for _ in range(tamanho)]
    
    # Medindo a memória antes da execução
    memoria_inicial = medir_memoria()
    
    # MergeSort
    inicio = time.time()
    merge_sort(dados)
    fim = time.time()
    memoria_final = medir_memoria()
    
    print(f"MergeSort ({tamanho} elementos): {fim - inicio:.6f} segundos | Memória: {memoria_final - memoria_inicial:.6f} MB")
