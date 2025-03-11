import numpy as np
import matplotlib.pyplot as plt

# AI Models
models = ["Decision Tree", "Random Forest", "SVM", "K-Means", "CNN", "LSTM"]

# Accuracy data across different datasets
nsl_kdd = [99.2, 99.8, 97.8, 82.4, 98.45, 97.72]
unsw_nb15 = [100, 99.9, 99.36, 85.1, 99.2, 98.8]
kddcup = [98.7, 99.94, 96.5, 78.3, 98.1, 99.86]
cicids = [100, 100, 98.2, 79.5, 100, 99.3]

x = np.arange(len(models))  # X-axis positions
bar_width = 0.2  # Width of each bar

# Create the bar chart
plt.figure(figsize=(12, 6))
plt.bar(x - 1.5*bar_width, nsl_kdd, width=bar_width, label="NSL-KDD", color="blue")
plt.bar(x - 0.5*bar_width, unsw_nb15, width=bar_width, label="UNSW-NB15", color="green")
plt.bar(x + 0.5*bar_width, kddcup, width=bar_width, label="KDDCup", color="red")
plt.bar(x + 1.5*bar_width, cicids, width=bar_width, label="CICIDS2017", color="purple")

plt.xticks(x, models, rotation=20)  # Rotate labels for clarity
plt.ylabel("Accuracy (%)")
plt.xlabel("AI Models")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
