import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

nodes = {
    "Plan": (0, 4),
    "Develop": (2, 3),
    "Build": (4, 4),
    "Test": (6, 3),
    "Release": (8, 4),
    "Deploy": (10, 3),
    "Monitor": (12, 4),
    "Feedback & Improve": (6, 1)
}

G.add_edges_from([
    ("Plan", "Develop"), ("Develop", "Build"), ("Build", "Test"),
    ("Test", "Release"), ("Release", "Deploy"), ("Deploy", "Monitor"),
    ("Monitor", "Feedback & Improve"), ("Feedback & Improve", "Plan")
])

plt.figure(figsize=(10, 5))
pos = {key: value for key, value in nodes.items()}
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightgreen", font_size=10, edge_color="gray", width=2)
plt.title("Figure 7: The Agile DevSecOps Cycle")
plt.show()
