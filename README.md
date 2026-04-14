# 🌸 Iris Flower Statistical Analysis

A complete statistical analysis project built in Python using the famous **Iris Flower Dataset**.  
This project performs data loading, cleaning, statistical computations, outlier detection, visualization, functional programming operations, and report generation.

---

## 📌 Project Overview

The Iris dataset contains **150 flower records** with measurements for:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width
- Species

The dataset includes **three flower species**:

- Setosa
- Versicolor
- Virginica

This project demonstrates practical implementation of:

- Data Analysis
- Statistics
- Python Programming Concepts
- Functional Programming
- Data Visualization

---

## 🚀 Features Implemented

### ✅ CSV File Handling
- Reads dataset using **try-except**
- Handles:
  - FileNotFoundError
  - PermissionError
  - General Exceptions

---

### ✅ Data Display
- Displays:
  - First 10 rows
  - Last 5 rows
  - DataFrame info

- Filters rows where:
  - `sepal_length > 5`

---

### ✅ Manual Outlier Detection
- Converts numeric columns to lists
- Calculates:
  - Q1
  - Q3
  - IQR
- Detects outliers manually using loops and conditions

---

### ✅ Feature Engineering
Creates new columns:

- `petal_area`
- `petal_to_sepal_ratio`
- `combined_score`

---

### ✅ Bitwise Operations
- Encodes species into numeric values
- Performs **Bitwise AND** comparisons

---

### ✅ Set Operations
- Stores unique measurement tuples in a set
- Displays:
  - Total unique combinations
  - 10 random unique tuples

---

### ✅ Manual Statistics
Calculates manually:

- Mean
- Median
- Mode
- Min
- Max

Using:
- Recursion
- Loops
- Lists

---

### ✅ Functional Programming
Uses:

- `filter()`
- `map()`
- `reduce()`

---

### ✅ Data Visualization
Generates graphs:

- Histogram
- Scatter Plot
- Box Plot
- Bar Chart

---

### ✅ Report Generation
Creates:

```txt
iris_analysis_report.txt
```

Containing:
- Dataset Overview
- Statistics
- Outlier Analysis
- Species Distribution

---

## 📂 Project Structure

```plaintext
iris_flower_analysis/
│
├── data/
│   └── iris.csv
│
├── src/
│   ├── main.py
│   ├── data_loader.py
│   ├── analysis.py
│   ├── visualization.py
│   ├── report_generator.py
│   └── utils.py
│
├── outputs/
│   ├── iris_analysis_report.txt
│   └── graphs/
│       ├── histogram.png
│       ├── scatter_plot.png
│       ├── box_plot.png
│       └── bar_chart.png
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Technologies Used

- Python 3
- Pandas
- Matplotlib
- NumPy
- Random Module
- Functools

---

## 📥 Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

Run the project using:

```bash
python src/main.py
```

---

## 📊 Sample Outputs

Generated files:

```plaintext
outputs/
│
├── iris_analysis_report.txt
│
└── graphs/
```

---

## 📚 Learning Outcomes

This project demonstrates understanding of:

- Python File Handling
- Exception Handling
- Loops and Conditional Statements
- Functional Programming
- Data Structures (Sets, Tuples, Lists)
- Statistical Analysis
- Data Visualization

---

## 🎯 Future Improvements

Possible future enhancements:

- Add Machine Learning Classification
- Build Web Dashboard
- Export Reports as PDF
- Interactive Graphs

---

## 👨‍💻 Author

Developed as part of academic statistical analysis project.

---

## ⭐ GitHub Tip

If you like this project, consider starring ⭐ the repository!