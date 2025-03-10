import numpy as np
import matplotlib.pyplot as plt

categories = ["Detection Speed", "Adaptability", "Automation", "Accuracy", "False Positives"]
traditional_security = [3, 2, 2, 3, 4]  # Scores out of 5
ai_security = [5, 5, 5, 5, 1]  # Higher is better

x = np.arange(len(categories))
bar_width = 0.4

plt.figure(figsize=(10, 7))
plt.bar(x, traditional_security, width=bar_width, label="Traditional Security", color='red')
plt.bar(x + bar_width, ai_security, width=bar_width, label="AI-Driven Security", color='green')

plt.xticks(x + bar_width / 2, categories, rotation=20)
plt.ylabel("Effectiveness Score (1-5)")
plt.title("Figure 8: AI vs. Traditional Cybersecurity Approaches")
plt.legend()
plt.show()
