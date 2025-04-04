import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn import preprocessing
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

# Reading data and visualization
df = pd.read_csv('StudentsPerformance.csv')
print("Shape of the dataframe:", df.shape)

# Checking for missing values
for col in df.columns:
    print(f"{col}: Missing values = {df[col].isnull().sum()}")

# Pre-processing categorical data
df['gender'] = df['gender'].map({'male': 0, 'female': 1})
df['lunch'] = df['lunch'].map({'free/reduced': 0, 'standard': 1})
df['test preparation course'] = df['test preparation course'].map({'completed': 0, 'none': 1})

# Race numeration (group A-E)
df['race/ethnicity'] = df['race/ethnicity'].map({'group A': 0, 'group B': 1, 'group C': 2, 'group D': 3, 'group E': 4})

# Parental education numeration
education_map = {
    'high school': 0, 'some high school': 0, 'some college': 1, 'associate\'s degree': 2,
    'master\'s degree': 4, 'bachelor\'s degree': 3
}
df['parental level of education'] = df['parental level of education'].map(education_map)

# EDA: Average score per subject by gender
sub = ['math', 'reading', 'writing']
boy_scores = df[df['gender'] == 0][sub].mean()
girl_scores = df[df['gender'] == 1][sub].mean()

# Plot gender vs average scores
plt.figure(figsize=(8, 6))
plt.title('Average Score per Subject by Gender')
plt.xlabel('Subjects')
plt.ylabel('Average Score')
plt.plot(sub, boy_scores, label='Boy', marker='o')
plt.plot(sub, girl_scores, label='Girl', marker='o')
plt.legend()
plt.show()

# EDA: Average score per race/ethnicity group
race_groups = ['group A', 'group B', 'group C', 'group D', 'group E']
math_scores = df.groupby('race/ethnicity')['math score'].mean()
reading_scores = df.groupby('race/ethnicity')['reading score'].mean()
writing_scores = df.groupby('race/ethnicity')['writing score'].mean()

# Plot race vs average scores
plt.figure(figsize=(10, 6))
plt.title('Average Score vs Race/Ethnicity')
plt.xlabel('Group')
plt.ylabel('Average Score')
plt.plot(race_groups, math_scores, label='Math', marker='o')
plt.plot(race_groups, reading_scores, label='Reading', marker='o')
plt.plot(race_groups, writing_scores, label='Writing', marker='o')
plt.legend()
plt.show()

# EDA: Max and Min Scores per Race/Ethnicity
for i, group in enumerate(race_groups):
    data = df[df['race/ethnicity'] == i]
    print(f"Group {group}:")
    print(f" - Max Math Score: {data['math score'].max()}, Min Math Score: {data['math score'].min()}")
    print(f" - Max Reading Score: {data['reading score'].max()}, Min Reading Score: {data['reading score'].min()}")
    print(f" - Max Writing Score: {data['writing score'].max()}, Min Writing Score: {data['writing score'].min()}")

# Parental Education vs Average Score
ped = ["high school", "some college", "associate's degree", "bachelor's degree", "master's degree"]
ped_scores = df.groupby('parental level of education')[sub].mean()

# Plot parental education vs average score
plt.figure(figsize=(10, 6))
plt.title('Average Score vs Parental Education Level')
plt.xlabel('Parental Education Level')
plt.ylabel('Average Score')
for i, subject in enumerate(sub):
    plt.plot(ped, ped_scores[subject], label=subject, marker='o')
plt.legend()
plt.xticks(rotation=45)
plt.show()

# Lunch vs Average Score
lunch_groups = ['No/less lunch', 'Standard lunch']
lunch_scores = df.groupby('lunch')[sub].mean()

# Plot lunch vs average scores
plt.figure(figsize=(8, 6))
plt.title('Lunch vs Average Score')
plt.xlabel('Lunch Condition')
plt.ylabel('Average Score')
for i, subject in enumerate(sub):
    plt.plot(lunch_groups, lunch_scores[subject], label=subject, marker='o')
plt.legend()
plt.show()

# Test preparation course vs Average Score
preparation_groups = ['No Preparation', 'Preparation']
prep_scores = df.groupby('test preparation course')[sub].mean()

# Plot test preparation course vs average scores
plt.figure(figsize=(8, 6))
plt.title('Test Preparation vs Average Score')
plt.xlabel('Test Preparation Course')
plt.ylabel('Average Score')
for i, subject in enumerate(sub):
    plt.plot(preparation_groups, prep_scores[subject], label=subject, marker='o')
plt.legend()
plt.show()
