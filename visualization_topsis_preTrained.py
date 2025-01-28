import matplotlib.pyplot as plt

# Example data
models = ['Model 1', 'Model 2', 'Model 3']
topsis_scores = [0.56021227, 0.49703687, 0.45328415]

# Create a bar chart
plt.figure(figsize=(8, 5))
plt.bar(models, topsis_scores, color=['#4CAF50', '#FFC107', '#2196F3'])
plt.title("TOPSIS Scores for Models", fontsize=14)
plt.xlabel("Models", fontsize=12)
plt.ylabel("TOPSIS Score", fontsize=12)
plt.ylim(0, 1)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
