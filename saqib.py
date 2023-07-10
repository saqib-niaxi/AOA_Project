import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Read the Excel file into a pandas DataFrame
df = pd.read_excel('your_excel_file.xlsx')

# Create a directed graph
G = nx.DiGraph()

# Add nodes to the graph
for index, row in df.iterrows():
    G.add_node(row['Pointer'])

# Add edges to the graph
for index, row in df.iterrows():
    for col in df.columns[1:]:
        if pd.notnull(row[col]):
            G.add_edge(row['Pointer'], row[col])

# # Draw the graph
pos = nx.circular_layout(G)  # Positions of nodes for visualization
nx.draw_networkx(G, pos, with_labels=True, arrows=True)

# Show the modified graph
plt.show()
def calculate_page_rank(graph):
    page_rank = {}
    num_nodes = len(graph)
    initial_score = 1 / num_nodes
    damping_factor = 0.85

    for node in graph.nodes():
        page_rank[node] = initial_score

    new_page_rank = {}
    for _ in range(num_nodes):
        for node in graph.nodes():
            rank = (1 - damping_factor) / num_nodes
            for neighbor in graph.predecessors(node):
                rank += damping_factor * page_rank[neighbor] / len(list(graph.successors(neighbor)))
            new_page_rank[node] = rank
        page_rank = new_page_rank.copy()

    return page_rank


# Calculate PageRank using the implemented function
pagerank = calculate_page_rank(G)

# Print the PageRank scores
sorted_data = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)
print("Page Ranks for each node are:")
for item in sorted_data:
    print(item)
