from collections import defaultdict

def ler_grafo(file_path):
    """
    Lê um arquivo contendo as arestas do grafo e cria uma representação de lista de adjacências.
    
    Parâmetros:
        file_path (str): Caminho para o arquivo contendo as arestas do grafo.
        
    Retorna:
        tuple: (grafo, grafo_transposto)
    """
    grafo = defaultdict(list)
    grafo_transposto = defaultdict(list)

    # Construir lista de adjacências e grafo transposto
    with open(file_path, 'r') as file:
        for line in file:
            u, v = map(int, line.split())  # u -> v
            grafo[u].append(v)
            grafo_transposto[v].append(u)

    return grafo, grafo_transposto


def kosaraju(grafo, grafo_transposto, num_vertices):
    """
    Implementa o algoritmo de Kosaraju para encontrar componentes fortemente conectados.
    
    Parâmetros:
        grafo (dict): Lista de adjacências do grafo.
        grafo_transposto (dict): Lista de adjacências do grafo transposto.
        num_vertices (int): Número de vértices no grafo.
        
    Retorna:
        int: Número de componentes fortemente conectados.
    """
    def dfs(v, visitado, stack, grafo_local):
        visitado[v] = True
        for vizinho in grafo_local[v]:
            if not visitado[vizinho]:
                dfs(vizinho, visitado, stack, grafo_local)
        stack.append(v)
    
    # Passo 1: Fazer a DFS para determinar a ordem de finalização dos vértices
    visitado = [False] * (num_vertices + 1)
    stack = []
    for i in range(1, num_vertices + 1):
        if not visitado[i]:
            dfs(i, visitado, stack, grafo)
    
    # Passo 2: Fazer a DFS no grafo transposto na ordem inversa
    visitado = [False] * (num_vertices + 1)
    num_componentes = 0
    while stack:
        v = stack.pop()
        if not visitado[v]:
            dfs(v, visitado, [], grafo_transposto)
            num_componentes += 1
    
    return num_componentes


# Configurações
file_path = "data/scientometrics.net"
num_vertices = 1656

# Construir o grafo e o grafo transposto
grafo, grafo_transposto = ler_grafo(file_path)

# Calcular o número de componentes fortemente conectados
num_componentes = kosaraju(grafo, grafo_transposto, num_vertices)

print(f"Número de componentes fortemente conectados: {num_componentes}")
