import matplotlib.pyplot as plt

# Categories
categories = ["Detection", "Response Speed", "Adaptability", "Automation", "Continuous Learning"]
traditional_values = [3, 2, 1, 2, 1]  # Traditional Security Scores
agile_values = [5, 5, 5, 5, 5]  # Agile AI Security Scores

plt.figure(figsize=(8, 5))
bar_width = 0.4
x = range(len(categories))

plt.bar(x, traditional_values, width=bar_width, label="Traditional Security", color='red')
plt.bar([p + bar_width for p in x], agile_values, width=bar_width, label="Agile AI Security", color='green')

plt.xticks([p + bar_width / 2 for p in x], categories, rotation=20)
plt.ylabel("Effectiveness Score (1-5)")
plt.title("Figure 2: Agile vs. Traditional Cybersecurity Approaches")
plt.legend()
plt.show()
