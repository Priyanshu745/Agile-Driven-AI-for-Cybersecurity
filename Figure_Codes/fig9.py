import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Function to draw rectangular nodes
def draw_networkx_with_rectangles(G, pos, ax):
    for node, (x, y) in pos.items():
        ax.add_patch(Rectangle((x - 0.6, y - 0.2), 1.2, 0.4, color="lightblue", ec="black"))
        ax.text(x, y, node, fontsize=10, ha='center', va='center', fontweight='bold')

# Define methodology workflow as a directed graph
G = nx.DiGraph()

# Define nodes and their positions
nodes = {
    "Cybersecurity Datasets": (0, 10),
    "Data Preprocessing": (0, 8),
    "Feature Engineering": (0, 6),
    "Handling Imbalance": (0, 4),
    "AI Model Training": (-2, 2),
    "ML Models (RF, SVM, K-Means)": (-2, 0),
    "DL Models (CNN, LSTM)": (0, 0),
    "RL Models (DQN)": (2, 0),
    "Deployment & Testing": (0, -2),
    "Real-Time Threat Detection": (0, -4),
    "Continuous Learning & Feedback": (0, -6)
}

# Define directed edges (workflow connections)
G.add_edges_from([
    ("Cybersecurity Datasets", "Data Preprocessing"),
    ("Data Preprocessing", "Feature Engineering"),
    ("Feature Engineering", "Handling Imbalance"),
    ("Handling Imbalance", "AI Model Training"),
    ("AI Model Training", "ML Models (RF, SVM, K-Means)"),
    ("AI Model Training", "DL Models (CNN, LSTM)"),
    ("AI Model Training", "RL Models (DQN)"),
    ("ML Models (RF, SVM, K-Means)", "Deployment & Testing"),
    ("DL Models (CNN, LSTM)", "Deployment & Testing"),
    ("RL Models (DQN)", "Deployment & Testing"),
    ("Deployment & Testing", "Real-Time Threat Detection"),
    ("Real-Time Threat Detection", "Continuous Learning & Feedback"),
    ("Continuous Learning & Feedback", "Data Preprocessing")  # Feedback loop
])

# Draw graph with rectangular nodes
fig, ax = plt.subplots(figsize=(18, 10))
pos = {key: value for key, value in nodes.items()}
nx.draw(G, pos, with_labels=False, node_size=0, edge_color="gray", width=2, ax=ax)
draw_networkx_with_rectangles(G, pos, ax)

ax.set_xlim(-3, 3)
ax.set_ylim(-7, 11)
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)

plt.show()
