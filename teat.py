import pandas as pd

# Define the data for 10 programming languages with a mix of binary and scalar features.
data = {
    "Language": ["Python", "Java", "C++", "C#", "JavaScript", "Go", "Rust", "Ruby", "Swift", "Haskell"],
    "Object-Oriented": [1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    "Functional": [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    "Procedural": [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    "Static Typing": [0, 1, 1, 1, 0, 1, 1, 0, 1, 1],
    "Dynamic Typing": [1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    "Memory Management": ["Garbage Collected", "Garbage Collected", "Manual", "Garbage Collected", "Garbage Collected", "Garbage Collected", "Garbage Collected", "Garbage Collected", "Garbage Collected", "Garbage Collected"],
    "Multi-Threading": [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    "Standard Library": ["Extensive", "Extensive", "Moderate", "Extensive", "Moderate", "Moderate", "Moderate", "Extensive", "Extensive", "Moderate"],
    "Cross-Platform": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    "Community Size": ["Large", "Large", "Large", "Large", "Large", "Medium", "Medium", "Medium", "Medium", "Small"],
    "IDE Support": ["High", "High", "High", "High", "High", "Medium", "Medium", "Medium", "High", "Low"]
}

# Create a DataFrame.
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file.
csv_file_path = 'programming_languages_features.csv'
df.to_csv(csv_file_path, index=False)

csv_file_path
