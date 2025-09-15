import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Task 1: Load and Explore Dataset
# -----------------------------
try:
    # Load dataset
    df = pd.read_csv("Employee.csv")
    print("✅ Dataset loaded successfully!\n")
except FileNotFoundError:
    print("❌ Error: Dataset file not found. Please ensure 'Employee.csv' is in the same directory.")
    exit()

# Display first 5 rows
print("--- First 5 rows of the dataset ---")
print(df.head())

# Dataset info
print("\n--- Dataset Info ---")
print(df.info())

# Check for missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# -----------------------------
# Task 2: Basic Data Analysis
# -----------------------------
print("\n--- Summary Statistics ---")
print(df.describe())

# Group by Education and compute average Age
print("\n--- Average Age by Education ---")
print(df.groupby("Education")["Age"].mean())

# Group by City and compute average Experience
print("\n--- Average Experience by City ---")
print(df.groupby("City")["ExperienceInCurrentDomain"].mean())

# Interesting Finding: Employees who left vs stayed
print("\n--- Leave vs Stay Counts ---")
print(df["LeaveOrNot"].value_counts())

# -----------------------------
# Task 3: Data Visualizations
# -----------------------------

# Line Chart: Number of employees joining each year
plt.figure(figsize=(8,5))
df.groupby("JoiningYear").size().plot(kind="line", marker="o")
plt.title("Employees Joined per Year")
plt.xlabel("Year")
plt.ylabel("Number of Employees")
plt.grid(True)
plt.show()

# Bar Chart: Average Age by Education
plt.figure(figsize=(7,5))
df.groupby("Education")["Age"].mean().plot(kind="bar", color="skyblue")
plt.title("Average Age by Education")
plt.xlabel("Education Level")
plt.ylabel("Average Age")
plt.show()

# Histogram: Age Distribution
plt.figure(figsize=(7,5))
df["Age"].plot(kind="hist", bins=20, color="orange", edgecolor="black")
plt.title("Age Distribution of Employees")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot: Age vs Experience
plt.figure(figsize=(7,5))
plt.scatter(df["Age"], df["ExperienceInCurrentDomain"], alpha=0.5, c="green")
plt.title("Age vs Experience in Current Domain")
plt.xlabel("Age")
plt.ylabel("Experience (Years)")
plt.show()

print("\n✅ Analysis and visualizations complete!")