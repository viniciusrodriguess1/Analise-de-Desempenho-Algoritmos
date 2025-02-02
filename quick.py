import time
import random
import tracemalloc

# Função QuickSort
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
    return peak / 1024, fim - inicio  # Retorna o pico de memória em KB e o tempo de execução

# Definição da seed para garantir reprodutibilidade dos testes
random.seed(42)
tamanhos = [10_000, 50_000, 100_000]

# Teste para QuickSort
for tamanho in tamanhos:
    dados = [random.randint(1, 1000000) for _ in range(tamanho)]
    
    # Medindo a memória e o tempo de execução para QuickSort
    memoria_quick, tempo_quick = medir_memoria(quicksort, dados)
    print(f"QuickSort ({tamanho} elementos): Tempo: {tempo_quick:.6f} segundos | Memória: {memoria_quick:.6f} KB")
