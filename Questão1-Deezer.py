import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from collections import Counter

# Carrega os dados (limitando a quantidade de linhas)
# edges_df = pd.read_csv("data/deezer/edges.csv", nrows=50)
# Carrega os dados (sem limitar a quantidade de linhas)
edges_df = pd.read_csv("data/deezer/edges.csv")
# Define que as colunas 1 e 2 serão source e target para uso do dataframe na proxíma função
edges_df.columns = ["source", "target"]

# Captura os dados do Edges_DF e converte em um grafo com as conexões entre os nós e arestas
G = nx.from_pandas_edgelist(edges_df, "source", "target")

# Grafo de Teste
# G1 = nx.Graph([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9)])
# G1.add_node("A")
# G2 = nx.complete_graph(9)
# G2 = nx.relabel_nodes(G2, {i: i + 10 for i in G2.nodes()})

# G = nx.compose_all([G1, G2])

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
        nx.draw(
            G,
            node_size=5,
            edge_color="blue",
            node_color="red",
        )
        plt.show()
    case "b":
        graus = [G.degree(n) for n in G.nodes()]

        # Calcula o grau médio
        grau_medio = sum(graus) / len(graus)

        # Calcula a distribuição do grau (quantidade de nós com cada grau)
        grau_contagem = Counter(graus)
        
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
        # Calcula o número de componentes conexos
        num_componentes = nx.number_connected_components(G)

        print(f"Número de componentes conexos: {num_componentes}")
    case "d":
        # Identifica os componentes conectados
        components = list(nx.connected_components(G))
        # Calcula o tamanho de cada componente
        component_sizes = [len(component) for component in components]

        # Verifica se há mais de um componente
        if len(component_sizes) > 1:
            plt.figure(figsize=(12, 6))
            plt.hist(
                component_sizes,
                edgecolor="black",
                align="left",
            )
            plt.title("Distribuição do Tamanho dos Componentes do Grafo")
            plt.xlabel("Tamanho dos Componentes")
            plt.ylabel("Frequência")
            plt.grid(True)
            plt.show()
        else:
            print("O grafo possui apenas um componente.")
    case "e":
        if nx.is_connected(G):
            shortest_path_lengths = dict(nx.all_pairs_shortest_path_length(G))

            # Coleta todas as distâncias
            distances = []
            for source, target_distances in shortest_path_lengths.items():
                distances.extend(target_distances.values())

            frequency = Counter(distances)

            distances = list(frequency.keys())
            frequencies = list(frequency.values())

            # Remove a distância 0 (distância de um nó para ele mesmo)
            distances = [d for d in distances if d > 0]

            # Calcula a distância média
            average_distance = sum(distances) / len(distances)
            print(f"Distância média entre os vértices: {average_distance:.2f}")

            plt.bar(distances, frequencies, color="skyblue", edgecolor="black")
            plt.title("Frequência das Distâncias no Grafo Completo (n=9)")
            plt.xlabel("Distância")
            plt.ylabel("Frequência")
            plt.xticks(distances)
            plt.grid(True)
            plt.show()
        else:
            print("O grafo não é conexo, não é possível calcular a distância média.")
    case "f":
        # Calcula a centralidade de carga das arestas
        edge_centrality = nx.edge_betweenness_centrality(G)

        # Ordena as arestas por centralidade de carga em ordem decrescente (key=lambda x: -x[1] ordena os itens do dicionário edge_centrality com base nos valores, do maior para o menor.)
        bridge_edges = sorted(edge_centrality.items(), key=lambda x: -x[1])

        # Imprime as arestas com maiores chances de serem pontes
        print("Arestas com grandes chances de serem pontes:")
        for edge, centrality in bridge_edges:
            print(f"{edge}: {centrality:.4f}")

        # Identifica os nós conectados às arestas com maiores chances de serem pontes
        bridge_nodes = set()
        for edge, _ in bridge_edges:
            bridge_nodes.update(edge)

        # Desenha a base do grafo
        pos = nx.spring_layout(G)
        plt.figure(figsize=(12, 6))

        # Desenha todas as arestas em cinza claro
        nx.draw_networkx_edges(G, pos, edge_color="lightgray")

        # Desenha as arestas com grandes chances de serem pontes
        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=[edge for edge, _ in bridge_edges],
            edge_color="red",
            width=2,
        )

        # Desenha os nós não conectados às arestas com grandes chances de serem pontes
        non_bridge_nodes = set(G.nodes()) - bridge_nodes
        nx.draw_networkx_nodes(
            G, pos, nodelist=list(non_bridge_nodes), node_size=5, node_color="black"
        )

        # Desenha os nós conectados às arestas com grandes chances de serem pontes
        nx.draw_networkx_nodes(
            G, pos, nodelist=list(bridge_nodes), node_size=5, node_color="blue"
        )

        plt.title("Grafo com Arestas com Grandes Chances de Serem Pontes Destacadas")
        plt.show()
    case _:
        print("Opção inválida")
