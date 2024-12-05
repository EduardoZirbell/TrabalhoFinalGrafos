def analisar_grafo(file_path, num_vertices):
    """
    Análise de um grafo a partir de um arquivo contendo as arestas.
    
    Calcula:
        - Presença de ciclos no grafo.
        - Média do comprimento dos caminhos mais curtos entre os pares de vértices.
    
    Parâmetros:
        file_path (str): Caminho para o arquivo contendo as arestas do grafo.
        num_vertices (int): Número total de vértices no grafo.
        
    Retorna:
        dict: Resultados contendo:
            - "has_cycles" (bool): Indica se o grafo contém ciclos.
            - "average_shortest_path_length" (float ou None): 
                Média do comprimento dos caminhos mais curtos, ou None se não for possível calcular.
    """
    # Carregar o grafo como lista de adjacências
    graph = {i: [] for i in range(1, num_vertices + 1)}
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                source, target = map(int, line.split())
                graph[source].append(target)
    
    # Detectar ciclos (usando DFS)
    def has_cycle(graph):
        def dfs(vertex, visited, stack):
            visited.add(vertex)
            stack.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    if dfs(neighbor, visited, stack):
                        return True
                elif neighbor in stack:
                    return True
            stack.remove(vertex)
            return False

        visited = set()
        for node in graph:
            if node not in visited:
                if dfs(node, visited, set()):
                    return True
        return False

    # Calcular caminhos mais curtos (usando BFS)
    def average_shortest_path(graph):
        def bfs(start):
            queue = [start]
            distances = {start: 0}
            while queue:
                current = queue.pop(0)
                for neighbor in graph[current]:
                    if neighbor not in distances:
                        distances[neighbor] = distances[current] + 1
                        queue.append(neighbor)
            return distances

        total_length = 0
        count = 0
        for vertex in graph:
            distances = bfs(vertex)
            total_length += sum(distances.values())
            count += len(distances) - 1  # Não contar o próprio nó como caminho

        return total_length / count if count > 0 else None

    # Analisar o grafo
    has_cycles = has_cycle(graph)
    avg_path_length = average_shortest_path(graph)

    return {
        "has_cycles": has_cycles,
        "average_shortest_path_length": avg_path_length
    }

# Configurações
file_path = "data/scientometrics.net"
num_vertices = 1656

# Analisar o grafo
resultados = analisar_grafo(file_path, num_vertices)

# Resultados
print(f"O grafo possui ciclos: {'Sim' if resultados['has_cycles'] else 'Não'}")
if resultados['average_shortest_path_length'] is not None:
    print(f"Média do comprimento dos caminhos mais curtos: {resultados['average_shortest_path_length']:.4f}")
else:
    print("Não foi possível calcular a média dos caminhos mais curtos.")
