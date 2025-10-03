import pandas as pd

# Load the large metadata.csv
df = pd.read_csv("metadata.csv")

# Show size of the full dataset
print("Original shape:", df.shape)

# Take a random sample of 5000 rows (you can use 1000 or 2000 if GitHub complains about file size)
sample = df.sample(5000, random_state=42)

# Save the smaller dataset
sample.to_csv("metadata_sample.csv", index=False)

print("Sample saved! Shape:", sample.shape)
