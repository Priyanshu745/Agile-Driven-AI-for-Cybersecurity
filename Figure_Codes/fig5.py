import matplotlib.pyplot as plt

years = [1980, 1995, 2005, 2015, 2020, 2025]
threats = ["Early Viruses", "Malware & Worms", "Phishing & DDoS", "Ransomware & APTs", "AI-Driven Attacks", "Autonomous Cyber Threats"]

plt.figure(figsize=(20, 10))
plt.plot(years, range(len(years)), 'ro-', markersize=8, label="Cyber Threat Evolution")

for i in range(len(years)):
    plt.text(years[i], i, threats[i], fontsize=12, verticalalignment='bottom', horizontalalignment='center')

plt.xlabel("Year")
plt.ylabel("Threat Evolution Level")
plt.title("Figure 5: Evolution of Cyber Threats Over Time")
plt.grid(True)
plt.show()
