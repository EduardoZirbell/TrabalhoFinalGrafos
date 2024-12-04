import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from collections import Counter

# Carregar os dados (limitando a quantidade de linhas)
# edges_df = pd.read_csv("data/facebook/edges.csv", nrows=50)
# Carregar os dados (sem limitar a quantidade de linhas)
edges_df = pd.read_csv("data/deezer/edges.csv")
# Define que as colunas 1 e 2 serão source e target para uso do dataframe na proxíma função
edges_df.columns = ["source", "target"]

# Captura os dados do Edges_DF e converte em um grafo com as conexões entre os nós e arestas
G = nx.from_pandas_edgelist(edges_df, "source", "target")

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
            G, with_labels=True, node_size=10, font_size=3, edge_color="blue"
        )
        plt.show()

    case "b":
        graus = [G.degree(n) for n in G.nodes()]

        # Calcular o grau médio
        grau_medio = sum(graus) / len(graus)

        # Imprimir o grau médio
        print()

        # Calcular a distribuição do grau (quantidade de nós com cada grau)
        grau_contagem = {}
        for grau in graus:
            if grau not in grau_contagem:
                grau_contagem[grau] = 0
            grau_contagem[grau] += 1

        # Plotar a distribuição do grau
        plt.figure(figsize=(10, 6))
        plt.bar(
            grau_contagem.keys(),
            grau_contagem.values(),
            color="skyblue",
            edgecolor="black",
        )
        plt.title(f"Distribuição do Grau dos Vértices: Grau médio: {grau_medio:.2f}")
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
        component_sizes = [len(c) for c in nx.connected_components(G)]

        # Contar a frequência de cada tamanho
        freq = Counter(component_sizes)

        # Criar o gráfico
        plt.bar(freq.keys(), freq.values())
        plt.xlabel('Tamanho do Componente')
        plt.ylabel('Frequência')
        plt.title('Distribuição do Tamanho dos Componentes')
        plt.show()
    case "e":
        print("teste5")
    case "f":
        print("teste6")
    case _:
        print("Opção inválida")


# graus = [G.degree(n) for n in G.nodes()]

# # Calcular o grau médio
# grau_medio = sum(graus) / len(graus)

# # Imprimir o grau médio
# print(f"Grau médio do grafo: {grau_medio:.2f}")

# # Calcular a distribuição do grau (quantidade de nós com cada grau)
# grau_contagem = {}
# for grau in graus:
#     if grau not in grau_contagem:
#         grau_contagem[grau] = 0
#     grau_contagem[grau] += 1


# # Usar um layout para organizar os nós
# pos = nx.spring_layout(G, k=0.3)  # Layout dos nós

# # Cria o tamanho da Figura do data base
# plt.figure(figsize=(12, 12))
# #Cria o desenho do grafo
# nx.draw(
#     G, #Dados do Grafo
#     pos,
#     node_size=50,
#     edge_color='gray',
#     node_color='blue'
# )


# # Adicionar rótulos dos nós manualmente (posicionados acima dos pontos)
# offset_pos = {node: (x, y + 0.02) for node, (x, y) in pos.items()}  # Ajuste na posição (para cima)
# nx.draw_networkx_labels(
#     G,
#     offset_pos,          # Usa as posições ajustadas
#     font_size=10,        # Tamanho do texto dos rótulos
#     font_color="darkblue"  # Cor dos rótulos
# )

# plt.show()
