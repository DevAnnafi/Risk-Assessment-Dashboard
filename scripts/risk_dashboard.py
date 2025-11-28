import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv("data/risks.csv")

# Calculate Risk Score
data["Risk_Score"] = data["Likelihood"] * data["Impact"]

# Calculate Residual Risk
data["Residual_Risk"] = data["Risk_Score"] - 1
data["Residual_Risk"] = data["Residual_Risk"].apply(lambda x: max(x, 1))

# Display top risks
print("Top 10 Risks by Risk Score:")
print(data.sort_values(by="Risk_Score", ascending=False).head(10))

# Heatmap
plt.figure(figsize=(12,8))
heatmap_data = data.pivot(index="Risk", columns="Category", values="Risk_Score").fillna(0)
sns.heatmap(heatmap_data, annot=True, cmap="Reds", linewidths=.5)
plt.title("Risk Assessment Heatmap")
plt.tight_layout()
plt.savefig("outputs/risk_heatmap.png")
plt.show()
