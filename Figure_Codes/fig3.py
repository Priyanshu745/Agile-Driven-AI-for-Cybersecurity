import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def draw_networkx_with_rectangles(G, pos, ax):
    for node, (x, y) in pos.items():
        ax.add_patch(Rectangle((x - 0.4, y - 0.2), 0.8, 0.4, color="lightblue", ec="black"))
        ax.text(x, y, node, fontsize=10, ha='center', va='center', fontweight='bold')

G = nx.DiGraph()

# Nodes with positions for vertical layout
nodes = {
    "Input Data": (0, 10),
    "Feature Extraction": (0, 8),
    "ML Model": (0, 6),
    "Threat Classification": (0, 4),
    "Alert & Response": (0, 2),
    "Automated Defense": (0, 0)
}

G.add_edges_from([
    ("Input Data", "Feature Extraction"),
    ("Feature Extraction", "ML Model"),
    ("ML Model", "Threat Classification"),
    ("Threat Classification", "Alert & Response"),
    ("Threat Classification", "Automated Defense")
])

fig, ax = plt.subplots(figsize=(7, 10))
pos = {key: value for key, value in nodes.items()}
nx.draw(G, pos, with_labels=False, node_size=0, edge_color="gray", width=2, ax=ax)
draw_networkx_with_rectangles(G, pos, ax)

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 11)
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)
plt.title("Figure 3: AI-Driven Threat Detection and Response")
plt.show()
