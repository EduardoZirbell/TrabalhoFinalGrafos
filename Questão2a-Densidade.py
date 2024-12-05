def calcular_densidade_grafo(file_path, num_vertices):
    """
    Questão 2a.
    Equipe: Eduardo Zirbell, Guilherme Kuhnen, Lucas Testoni
    
    Calcula a densidade de um grafo a partir de um arquivo contendo as arestas.
    
    Parâmetros:
        file_path (str): Caminho para o arquivo contendo as arestas do grafo.
        num_vertices (int): Número total de vértices no grafo.
        
    Retorna:
        float: Densidade do grafo.
    """
    # Contar o número de arestas no arquivo
    with open(file_path, 'r') as file:
        num_arestas = sum(1 for _ in file)
    
    # Fórmula da densidade
    densidade = (2 * num_arestas) / (num_vertices * (num_vertices - 1))
    return num_arestas, densidade

# Configurações
file_path = "data/scientometrics.net"
num_vertices = 1656

# Calcular densidade
num_arestas, densidade = calcular_densidade_grafo(file_path, num_vertices)

# Resultados
print(f"Número de arestas (M): {num_arestas}")
print(f"Densidade do grafo: {densidade:.4f}")
