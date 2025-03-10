import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def draw_networkx_with_rectangles(G, pos, ax):
    for node, (x, y) in pos.items():
        ax.add_patch(Rectangle((x - 0.5, y - 0.2), 1, 0.4, color="lightblue", ec="black"))
        ax.text(x, y, node, fontsize=10, ha='center', va='center', fontweight='bold')

G = nx.DiGraph()

nodes = {
    "Raw Data": (0, 10),
    "Feature Extraction": (0, 8),
    "Machine Learning Model": (0, 6),
    "Threat Classification": (0, 4),
    "Automated Response": (0, 2),
    "Threat Neutralization": (0, 0)
}

G.add_edges_from([
    ("Raw Data", "Feature Extraction"),
    ("Feature Extraction", "Machine Learning Model"),
    ("Machine Learning Model", "Threat Classification"),
    ("Threat Classification", "Automated Response"),
    ("Automated Response", "Threat Neutralization")
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
plt.title("Figure 6: AI-Driven Threat Detection Workflow")
plt.show()
