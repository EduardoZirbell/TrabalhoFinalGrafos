import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from collections import Counter
import random

# Carregar os dados (limitando a quantidade de linhas)
# edges_df = pd.read_csv("data/facebook/edges.csv", nrows=50)
# Carregar os dados (sem limitar a quantidade de linhas)
edges_df = pd.read_csv("data/lastfm/edges.csv")
# Define que as colunas 1 e 2 serão source e target para uso do dataframe na proxíma função
edges_df.columns = ["source", "target"]

# Captura os dados do Edges_DF e converte em um grafo com as conexões entre os nós e arestas
# G = nx.from_pandas_edgelist(edges_df, "source", "target")

G1 = nx.Graph([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9)])
G1.add_node('A')
G2 = nx.complete_graph(10)
G2 = nx.relabel_nodes(G2, {i: i + 10 for i in G2.nodes()})

G = nx.compose_all([G1, G2])

option = input(
    """Bem vindo ao trabalho final de grafos. 
a) Forneça a representação visual do grafo.
b) Calcule e gere um gráfico da distribuição do grau dos vértices desse grafo. Calcule também o grau médio do grafo.
c) Calcule o número de componentes do grafo.
d) Gere um gráfico com a distribuição do tamanho dos componentes do grafo. Se o grafo possuir apenas um componente não é preciso plotar. 
e) Calcule a distância média e a distribuição das distâncias de todos os vértices da rede.
f) Implemente uma abordagem para encontrar arestas com grandes chances de serem pontes.
Escolha a opção desejada: """
)
match option.lower():
    case "a":
        nx.draw_circular(
            G, with_labels=False, node_size=5, font_size=3, edge_color="blue"
        )
        plt.show()
    case "b":
        graus = [G.degree(n) for n in G.nodes()]

        # Calcular o grau médio
        grau_medio = sum(graus) / len(graus)

        # Calcular a distribuição do grau (quantidade de nós com cada grau)
        grau_contagem = Counter(graus)

        # Plotar a distribuição do grau dos vértices
        plt.figure(figsize=(12, 6))
        plt.bar(
            grau_contagem.keys(),
            grau_contagem.values(),
            color="skyblue",
            edgecolor="black",
        )
        plt.title(f"Distribuição do Grau dos Vértices: Grau Médio: {grau_medio:.2f}")
        plt.xlabel("Grau")
        plt.ylabel("Número de Nós")
        plt.grid(True)
        plt.show()
    case "c":
        # Calcular o número de componentes conexos
        num_componentes = nx.number_connected_components(G)

        # Exibir o número de componentes conexos
        print(f"Número de componentes conexos: {num_componentes}")
    case "d":
        # Identificar os componentes conectados
        components = list(nx.connected_components(G))
        component_sizes = [len(component) for component in components]

        # Verificar se há mais de um componente
        if len(component_sizes) > 1:
            plt.figure(figsize=(8, 6))
            plt.hist(
                component_sizes,
                bins=range(1, max(component_sizes) + 2),
                edgecolor="black",
                align="left",
            )
            plt.title("Distribuição do Tamanho dos Componentes do Grafo")
            plt.xlabel("Tamanho dos Componentes")
            plt.ylabel("Frequência")
            plt.grid(axis="y", linestyle="--", alpha=0.7)
            plt.show()
        else:
            print("O grafo possui apenas um componente.")
    case "e":
        # Verificar se o grafo é conexo, necessário para calcular distâncias
        if nx.is_connected(G):
            # Calcular a distância média (caminho médio)
            avg_distance = nx.average_shortest_path_length(G)
            print(f"Distância média entre todos os vértices: {avg_distance:.4f}")
            
            # Calcular todas as distâncias de pares de vértices
            distances = []
            for source, path_lengths in nx.shortest_path_length(G):
                distances.extend(path_lengths.values())
            
            # Criar um histograma da distribuição das distâncias
            plt.figure(figsize=(8, 6))
            plt.hist(distances, bins=range(1, max(distances) + 2), edgecolor="black", align="left")
            plt.title("Distribuição das Distâncias entre os Vértices")
            plt.xlabel("Distância")
            plt.ylabel("Frequência")
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.show()
        else:
            print("O grafo não é conexo. Calcule a distância média apenas para os componentes conectados.")
    case "f":
        # Calcula a centralidade de carga das arestas
        edge_centrality = nx.edge_betweenness_centrality(G)

        # Ordena as arestas por centralidade de carga em ordem decrescente
        sorted_edges = sorted(edge_centrality.items(), key=lambda x: x[1], reverse=True)

        # Retorna as arestas com maiores chances de serem pontes
        bridge_edges = sorted_edges[:100]

        # Imprime as arestas com maiores chances de serem pontes
        print("Arestas com grandes chances de serem pontes:")
        for edge, centrality in bridge_edges:
            print(f"{edge}: {centrality:.4f}")
        
        # Identificar os nós conectados às arestas com maiores chances de serem pontes
            bridge_nodes = set()
            for edge, _ in bridge_edges:
                bridge_nodes.update(edge)

        # Desenhar o grafo destacando as arestas com grandes chances de serem pontes
        pos = nx.spring_layout(G)  # Layout para a visualização do grafo
        plt.figure(figsize=(12, 8))

        # Desenhar todas as arestas em cinza claro
        nx.draw_networkx_edges(G, pos, edge_color="lightgray")

        # Desenhar as arestas com grandes chances de serem pontes em vermelho
        nx.draw_networkx_edges(G, pos, edgelist=[edge for edge, _ in bridge_edges], edge_color="red", width=2)

        # Desenhar os nós não conectados às arestas com grandes chances de serem pontes em azul
        non_bridge_nodes = set(G.nodes()) - bridge_nodes
        nx.draw_networkx_nodes(G, pos, nodelist=list(non_bridge_nodes), node_size=50, node_color="blue")

        # Desenhar os nós conectados às arestas com grandes chances de serem pontes em verde
        nx.draw_networkx_nodes(G, pos, nodelist=list(bridge_nodes), node_size=50, node_color="green")

        # Desenhar os rótulos dos nós
        nx.draw_networkx_labels(G, pos, font_size=8, font_color="black")

        # Adicionar rótulos às arestas com os valores de centralidade
        edge_labels = {edge: f"{centrality:.4f}" for edge, centrality in bridge_edges}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red")

        plt.title("Grafo com Arestas com Grandes Chances de Serem Pontes Destacadas")
        plt.show()
        
    case _:
        print("Opção inválida")
