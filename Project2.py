#

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV file
file_path = "large_sales_data.csv"  # Ensure the file name matches your actual file
data = pd.read_csv(file_path, delimiter=";", usecols=["Month", "Sales"])

# Step 2: Data Preparation
# Convert sales to numeric (in case of bad data like strings)
data["Sales"] = pd.to_numeric(data["Sales"], errors="coerce")
data = data.dropna()  # Remove rows with NaN values

# Step 3: Create a histogram
plt.figure(figsize=(10, 6))
plt.hist(data["Sales"], bins=20, color="blue", edgecolor="black", alpha=0.7)

# Step 4: Customize the plot
plt.title("Distribution of IoT Monthly Sales", fontsize=16)
plt.xlabel("Sales Amount", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)

# Step 5: Show the plot
plt.tight_layout()
plt.show()