import matplotlib.pyplot as plt

# Define timeline events
years = [1990, 2000, 2010, 2020, 2025]
approaches = ["Firewalls & Antivirus", "Signature-Based IDS", "Machine Learning IDS", "Deep Learning & AI", "Agile AI-Driven Security"]

# Plot timeline
plt.figure(figsize=(10, 3))
plt.plot(years, [1, 2, 3, 4, 5], 'ro-', markersize=10, label="Cybersecurity Evolution")
for i in range(len(years)):
    plt.text(years[i], i + 1, approaches[i], fontsize=12, verticalalignment='bottom', horizontalalignment='center')

plt.xlabel("Year")
plt.ylabel("Security Approach Level")
plt.title("Figure 1: Evolution of Cybersecurity Approaches")
plt.grid(True)
plt.show()
