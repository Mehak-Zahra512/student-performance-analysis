# Student Performance Analysis and Visualization

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Load dataset
try:
    data = pd.read_csv("student_data.csv")
except FileNotFoundError:
    print("Error: student_data.csv file not found.")
    exit()

# Display basic info
print("\nFirst 5 rows of dataset:")
print(data.head())

print("\nBasic Statistics:")
print(data.describe())

print("\nMissing Values:")
print(data.isnull().sum())

# 📊 Correlation Matrix
print("\nCorrelation Matrix:")
corr_matrix = data.corr()
print(corr_matrix)

# 📊 Histogram of current scores
plt.figure()
plt.hist(data['current_score'], bins=5)
plt.title("Distribution of Current Scores")
plt.xlabel("Scores")
plt.ylabel("Number of Students")
plt.show()

# 📊 Scatter Plot: Study Hours vs Current Score
plt.figure()
plt.scatter(data['study_hours'], data['current_score'])
plt.title("Study Hours vs Current Score")
plt.xlabel("Study Hours")
plt.ylabel("Current Score")
plt.show()

# 📊 Highlight highest score using bar chart
colors = ['orange' if x == data['current_score'].max() else 'blue' for x in data['current_score']]
plt.figure()
plt.bar(range(len(data)), data['current_score'], color=colors)
plt.title("Student Performance (Highest Highlighted)")
plt.xlabel("Students")
plt.ylabel("Scores")
plt.show()

# 📊 Pearson Correlation (Main Analysis)
corr, p_value = stats.pearsonr(data['study_hours'], data['current_score'])

print("\nPearson Correlation (Study Hours vs Score):")
print("Correlation coefficient:", round(corr, 2))
print("P-value:", round(p_value, 4))

if p_value < 0.05:
    if corr > 0:
        print("There is a significant positive relationship between study hours and performance.")
    else:
        print("There is a significant negative relationship.")
else:
    print("No significant relationship found.")

# 📊 Additional Correlations
variables = ['sleep_hours', 'attendance_percentage', 'social_media_hours']

for var in variables:
    corr, p_value = stats.pearsonr(data[var], data['current_score'])
    print(f"\n{var} vs Current Score:")
    print("Correlation:", round(corr, 2), "| P-value:", round(p_value, 4))