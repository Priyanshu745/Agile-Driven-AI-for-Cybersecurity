import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Function to draw rectangles
def draw_networkx_with_rectangles(G, pos, ax):
    for node, (x, y) in pos.items():
        ax.add_patch(Rectangle((x - 0.6, y - 0.2), 1.2, 0.4, color="lightblue", ec="black"))
        ax.text(x, y, node, fontsize=10, ha='center', va='center', fontweight='bold')

# Define workflow as a directed graph
G = nx.DiGraph()

nodes = {
    "Cybersecurity Datasets": (0, 10),
    "Data Cleaning": (0, 8),
    "Feature Engineering": (0, 6),
    "Handling Imbalanced Data": (0, 4),
    "Final Processed Dataset": (0, 2),
}

G.add_edges_from([
    ("Cybersecurity Datasets", "Data Cleaning"),
    ("Data Cleaning", "Feature Engineering"),
    ("Feature Engineering", "Handling Imbalanced Data"),
    ("Handling Imbalanced Data", "Final Processed Dataset"),
])

# Draw graph
fig, ax = plt.subplots(figsize=(10, 8))
pos = {key: value for key, value in nodes.items()}
nx.draw(G, pos, with_labels=False, node_size=0, edge_color="gray", width=2, ax=ax)
draw_networkx_with_rectangles(G, pos, ax)

ax.set_xlim(-2, 2)
ax.set_ylim(0, 11)
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)
plt.title("Figure 10: Data Collection & Preprocessing Workflow")
plt.show()
