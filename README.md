# 🎓 Student Performance Analysis 📊

This project performs a complete **Exploratory Data Analysis (EDA)** and visualization on a dataset of **students' academic performance**. It aims to uncover meaningful insights and trends related to gender, ethnicity, parental education, lunch types, and test preparation, and how these factors influence scores in **Math**, **Reading**, and **Writing**.

---

## 📂 Dataset Overview

The dataset is stored in a file called `StudentsPerformance.csv`.

Each row in the dataset represents **one student**, with demographic data and exam scores. The dataset allows us to investigate potential correlations between background factors and academic achievement.

### 📊 Dataset Columns:

| Column                     | Description                                      | Example Values                   |
|----------------------------|--------------------------------------------------|----------------------------------|
| `gender`                   | Gender of the student                           | `male`, `female`                 |
| `race/ethnicity`           | Ethnic group or social background               | `group A`, `group B`, ..., `group E` |
| `parental level of education` | Highest education level of the parents     | `high school`, `associate's degree`, `master's degree` |
| `lunch`                    | Type of lunch program                           | `standard`, `free/reduced`       |
| `test preparation course`  | Whether a test prep course was completed        | `none`, `completed`              |
| `math score`               | Math score (0–100)                              | `82`, `49`, `100`, etc.          |
| `reading score`            | Reading score (0–100)                           | `75`, `58`, `95`, etc.           |
| `writing score`            | Writing score (0–100)                           | `80`, `73`, `91`, etc.           |

---

## 🎯 Project Goals & Analysis Objectives

This project focuses on answering the following key questions:

1. **How does gender affect exam scores?**
2. **Do students from certain ethnic groups perform better than others?**
3. **Is there a correlation between parental education and student performance?**
4. **Do students who complete test preparation courses perform better?**
5. **What is the impact of lunch type (standard vs free/reduced) on scores?**

By answering these, we aim to:
- Understand disparities in education.
- Visualize trends using charts and graphs.
- Provide data-backed insights for educators and policy makers.

---

## 🧰 Tools & Technologies Used

The project is built using Python and several data science libraries:

- **Python 3.x** – core programming language  
- **NumPy** – for numerical computations  
- **Pandas** – for data manipulation and analysis  
- **Matplotlib** – for creating static plots  
- **Seaborn** – for advanced and beautiful data visualizations  
- **Scikit-learn** – used optionally for preprocessing (e.g., encoding)

---

## 🛠️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/M-Aitisam/Student-Performance-Analysis.git
cd student-performance-analysis
