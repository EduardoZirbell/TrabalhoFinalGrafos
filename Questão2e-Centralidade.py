def calcular_centralidade_grau_top3(file_path, num_vertices):
    """
    Calcula a centralidade de grau de cada vértice de um grafo direcionado
    e retorna os 3 principais vértices com base nos graus de entrada e saída.
    
    Parâmetros:
        file_path (str): Caminho para o arquivo contendo as arestas do grafo.
        num_vertices (int): Número total de vértices no grafo.
        
    Retorna:
        dict: Os 3 principais vértices por grau de entrada e saída.
    """
    # Inicializar lista de adjacências
    grau_entrada = {i: 0 for i in range(1, num_vertices + 1)}
    grau_saida = {i: 0 for i in range(1, num_vertices + 1)}
    
    # Construir o grafo a partir do arquivo
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                source, target = map(int, line.split())
                grau_saida[source] += 1
                grau_entrada[target] += 1

    # Ordenar vértices pelos graus de entrada e saída
    top3_grau_entrada = sorted(grau_entrada.items(), key=lambda x: x[1], reverse=True)[:3]
    top3_grau_saida = sorted(grau_saida.items(), key=lambda x: x[1], reverse=True)[:3]

    return {
        "top3_grau_entrada": top3_grau_entrada,
        "top3_grau_saida": top3_grau_saida
    }

# Configurações
file_path = "data/scientometrics.net"
num_vertices = 1656

# Calcular centralidade de grau
top3_centralidade = calcular_centralidade_grau_top3(file_path, num_vertices)

# Exibir resultados
print("Top 3 vértices por Grau de Entrada:")
for rank, (vertex, grau) in enumerate(top3_centralidade["top3_grau_entrada"], start=1):
    print(f"{rank}. Vértice {vertex} com Grau de Entrada = {grau}")

print("\nTop 3 vértices por Grau de Saída:")
for rank, (vertex, grau) in enumerate(top3_centralidade["top3_grau_saida"], start=1):
    print(f"{rank}. Vértice {vertex} com Grau de Saída = {grau}")
