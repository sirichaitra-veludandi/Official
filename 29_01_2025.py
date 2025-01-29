import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(10)
data = {
    "Study Hours": np.random.randint(1, 10, 50),
    "Marks": np.random.randint(30, 100, 50),
    "Screen Time": np.random.randint(1, 7, 50),
    "Travelling Time": np.random.randint(4, 10, 50),
}
df = pd.DataFrame(data)
corr = df.corr()
feature1 = "Study Hours"
feature2 = "Marks"
correlation_value = df[feature1].corr(df[feature2])
print(f"Correlation between {feature1} and {feature2}: {correlation_value:.2f}")
plt.figure(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidth=0.5)
plt.title("Feature Correlation Heatmap")
plt.show()