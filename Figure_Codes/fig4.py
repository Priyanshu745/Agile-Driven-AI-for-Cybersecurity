import networkx as nx
import matplotlib.pyplot as plt

# Define the graph structure
G = nx.DiGraph()

# Add nodes
nodes = ["Signature-Based Detection", "Slow Response Time", "Static Rule-Based Security", "Lack of AI Adaptability", "Ineffective Against Zero-Day Attacks"]
for node in nodes:
    G.add_node(node)

# Add edges
G.add_edges_from([
    ("Signature-Based Detection", "Ineffective Against Zero-Day Attacks"),
    ("Slow Response Time", "Lack of AI Adaptability"),
    ("Static Rule-Based Security", "Ineffective Against Zero-Day Attacks"),
    ("Lack of AI Adaptability", "Ineffective Against Zero-Day Attacks")
])

# Draw the graph
plt.figure(figsize=(8, 4))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightcoral", font_size=10, edge_color="black", width=2)
plt.title("Figure 4: Challenges in Traditional Cybersecurity")
plt.show()
