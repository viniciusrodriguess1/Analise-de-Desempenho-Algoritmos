import time
import random

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
            resultado.append(esquerda[i])  # Correção do nome do método
            i += 1
        else:
            resultado.append(direita[j])  # Correção do nome do método
            j += 1
    resultado.extend(esquerda[i:])  # Correção do nome do método
    resultado.extend(direita[j:])  # Correção do nome do método
    return resultado

# Definição da seed para garantir reprodutibilidade dos testes
random.seed(42)
tamanhos = [10_000, 50_000, 100_000]

for tamanho in tamanhos:
    dados = [random.randint(1, 1000000) for _ in range(tamanho)]
    inicio = time.time()
    merge_sort(dados)
    fim = time.time()
    print(f"MergeSort ({tamanho} elementos): {fim - inicio:.6f} segundos")
