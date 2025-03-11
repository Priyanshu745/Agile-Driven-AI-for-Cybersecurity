import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Function to draw rectangular nodes with proper spacing
def draw_networkx_with_rectangles(G, pos, ax):
    for node, (x, y) in pos.items():
        ax.add_patch(Rectangle((x - 1, y - 0.3), 2, 0.6, color="lightblue", ec="black"))
        ax.text(x, y, node, fontsize=12, ha='center', va='center', fontweight='bold')

# Define workflow graph
G = nx.DiGraph()

# Define node positions with better spacing to avoid overlap
nodes = {
    "Processed Data": (0, 14),
    "Machine Learning": (-4, 12),
    "Deep Learning": (0, 12),
    "Reinforcement Learning": (4, 12),
    "Random Forest (RF)": (-6, 10),
    "SVM": (-4, 10),
    "K-Means": (-2, 10),
    "CNN": (0, 10),
    "LSTM": (2, 10),
    "DQN": (4, 10),
    "Trained Models": (0, 7),
}

# Define directed edges (connections)
G.add_edges_from([
    ("Processed Data", "Machine Learning"),
    ("Processed Data", "Deep Learning"),
    ("Processed Data", "Reinforcement Learning"),
    ("Machine Learning", "Random Forest (RF)"),
    ("Machine Learning", "SVM"),
    ("Machine Learning", "K-Means"),
    ("Deep Learning", "CNN"),
    ("Deep Learning", "LSTM"),
    ("Reinforcement Learning", "DQN"),
    ("Random Forest (RF)", "Trained Models"),
    ("SVM", "Trained Models"),
    ("K-Means", "Trained Models"),
    ("CNN", "Trained Models"),
    ("LSTM", "Trained Models"),
    ("DQN", "Trained Models"),
])

# Draw graph with properly spaced rectangular nodes
fig, ax = plt.subplots(figsize=(23, 10))  # Increased figure size for clarity
pos = {key: value for key, value in nodes.items()}
nx.draw(G, pos, with_labels=False, node_size=0, edge_color="gray", width=2, ax=ax)
draw_networkx_with_rectangles(G, pos, ax)

ax.set_xlim(-7, 7)
ax.set_ylim(6, 15)
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)

plt.show()
