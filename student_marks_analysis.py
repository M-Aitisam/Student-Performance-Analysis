import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

# Page Config
st.set_page_config(page_title="Student Performance Analysis", layout="wide")

# Title
st.title("📊 Student Performance Analysis (ML Project)")
st.markdown("Analyze gender, parental education, lunch, and preparation course impact on scores.")

# Load Dataset
@st.cache_data
def load_data():
    df = pd.read_csv("StudentsPerformance.csv")
    return df

df = load_data()

# Show raw data
if st.checkbox("Show raw data"):
    st.dataframe(df)

# Preprocessing
df['gender'] = df['gender'].map({'male': 0, 'female': 1})
df['lunch'] = df['lunch'].map({'free/reduced': 0, 'standard': 1})
df['test preparation course'] = df['test preparation course'].map({'completed': 0, 'none': 1})
df['race/ethnicity'] = df['race/ethnicity'].map({'group A': 0, 'group B': 1, 'group C': 2, 'group D': 3, 'group E': 4})
df['parental level of education'] = df['parental level of education'].map({
    'high school': 0,
    'some high school': 0,
    'some college': 1,
    'associate\'s degree': 2,
    'bachelor\'s degree': 3,
    'master\'s degree': 4
})

# Score columns
score_columns = ['math score', 'reading score', 'writing score']

# Gender-Based Average Scores
st.subheader("1️⃣ Average Scores by Gender")
gender_scores = df.groupby('gender')[score_columns].mean().T
gender_scores.columns = ['Boys', 'Girls']

fig1, ax1 = plt.subplots(figsize=(8, 5))
gender_scores.plot(kind='bar', ax=ax1)
plt.title("Average Scores by Gender")
plt.ylabel("Score")
plt.xticks(rotation=0)
st.pyplot(fig1)

# Race/Ethnicity vs Average Score
st.subheader("2️⃣ Average Scores by Race/Ethnicity")
race_labels = ['Group A', 'Group B', 'Group C', 'Group D', 'Group E']
race_scores = df.groupby('race/ethnicity')[score_columns].mean()

fig2, ax2 = plt.subplots(figsize=(10, 5))
race_scores.plot(kind='line', marker='o', ax=ax2)
plt.title("Average Scores by Race/Ethnicity")
plt.ylabel("Score")
plt.xlabel("Race/Ethnicity Group (0=A, 4=E)")
st.pyplot(fig2)

# Max & Min Scores by Race
st.subheader("3️⃣ Max and Min Scores by Race/Ethnicity")
for i in range(5):
    group_data = df[df['race/ethnicity'] == i]
    st.markdown(f"**Group {race_labels[i]}**")
    st.write({
        'Math': {'Max': group_data['math score'].max(), 'Min': group_data['math score'].min()},
        'Reading': {'Max': group_data['reading score'].max(), 'Min': group_data['reading score'].min()},
        'Writing': {'Max': group_data['writing score'].max(), 'Min': group_data['writing score'].min()}
    })

# Parental Education vs Average Score
st.subheader("4️⃣ Parental Education Level vs Average Score")
ped_labels = ["High School", "Some College", "Associate", "Bachelor", "Master"]
ped_scores = df.groupby('parental level of education')[score_columns].mean()

fig3, ax3 = plt.subplots(figsize=(10, 5))
for subject in score_columns:
    ax3.plot(ped_labels, ped_scores[subject], label=subject, marker='o')
plt.legend()
plt.title("Average Score vs Parental Education Level")
plt.xticks(rotation=45)
plt.ylabel("Score")
st.pyplot(fig3)

# Lunch vs Scores
st.subheader("5️⃣ Lunch Type vs Average Score")
lunch_scores = df.groupby('lunch')[score_columns].mean()
lunch_labels = ['Free/Reduced', 'Standard']

fig4, ax4 = plt.subplots(figsize=(8, 5))
for subject in score_columns:
    ax4.plot(lunch_labels, lunch_scores[subject], label=subject, marker='o')
plt.title("Lunch Type vs Average Score")
plt.legend()
st.pyplot(fig4)

# Test Preparation Course vs Scores
st.subheader("6️⃣ Test Preparation Course vs Average Score")
prep_scores = df.groupby('test preparation course')[score_columns].mean()
prep_labels = ['Completed', 'None']

fig5, ax5 = plt.subplots(figsize=(8, 5))
for subject in score_columns:
    ax5.plot(prep_labels, prep_scores[subject], label=subject, marker='o')
plt.title("Test Preparation Course vs Average Score")
plt.legend()
st.pyplot(fig5)

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
