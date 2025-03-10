import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def draw_networkx_with_rectangles(G, pos, ax):
    for node, (x, y) in pos.items():
        ax.add_patch(Rectangle((x - 0.6, y - 0.2), 1.2, 0.4, color="White", ec="black"))
        ax.text(x, y, node, fontsize=10, ha='center', va='center', fontweight='bold')

G = nx.DiGraph()

nodes = {
    "Trained AI Model": (0, 10),
    "Hyperparameter Optimization": (-2, 8),
    "Google Colab Training": (2, 8),
    "Cloud Deployment": (0, 6),
    "Real-Time Threat Simulation": (0, 4),
    "Performance Evaluation": (-2, 2),
    "Continuous Model Update": (2, 2),
    "Final AI Cybersecurity System": (0, 0),
}

G.add_edges_from([
    ("Trained AI Model", "Hyperparameter Optimization"),
    ("Trained AI Model", "Google Colab Training"),
    ("Hyperparameter Optimization", "Cloud Deployment"),
    ("Google Colab Training", "Cloud Deployment"),
    ("Cloud Deployment", "Real-Time Threat Simulation"),
    ("Real-Time Threat Simulation", "Performance Evaluation"),
    ("Real-Time Threat Simulation", "Continuous Model Update"),
    ("Performance Evaluation", "Final AI Cybersecurity System"),
    ("Continuous Model Update", "Final AI Cybersecurity System"),
])

fig, ax = plt.subplots(figsize=(20, 10))
pos = {key: value for key, value in nodes.items()}
nx.draw(G, pos, with_labels=False, node_size=0, edge_color="gray", width=2, ax=ax)
draw_networkx_with_rectangles(G, pos, ax)

ax.set_xlim(-3, 3)
ax.set_ylim(-1, 11)
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)
plt.title("Figure 12: Deployment and Testing Strategy")
plt.show()
