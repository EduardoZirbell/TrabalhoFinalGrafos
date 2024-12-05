def calcular_graus_medios(file_path, num_vertices):
    """
    
    Questão 2b.
    Equipe: Eduardo Zirbell, Guilherme Kuhnen, Lucas Testoni
    
    Calcula os graus médios de entrada e saída de um grafo a partir de um arquivo.
    
    Parâmetros:
        file_path (str): Caminho para o arquivo contendo as arestas do grafo.
        num_vertices (int): Número total de vértices no grafo.
        
    Retorna:
        tuple: (grau_medio_entrada, grau_medio_saida)
    """
    # Inicializar contadores
    num_arestas = 0

    # Processar o arquivo para contar arestas
    with open(file_path, 'r') as file:
        for line in file:
            num_arestas += 1  # Cada linha representa uma aresta
    
    # Grau médio de entrada e saída
    grau_medio_entrada = num_arestas / num_vertices
    grau_medio_saida = num_arestas / num_vertices

    return grau_medio_entrada, grau_medio_saida


# Configurações
file_path = "data/scientometrics.net"
num_vertices = 1656

# Calcular graus médios
grau_medio_entrada, grau_medio_saida = calcular_graus_medios(file_path, num_vertices)

# Resultados
print(f"Grau médio de entrada: {grau_medio_entrada:.2f}")
print(f"Grau médio de saída: {grau_medio_saida:.2f}")
