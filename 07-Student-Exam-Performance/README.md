# 🎓 Student Performance Report

## 📄 Overview
This project analyzes and reports on student performance data using Python.  
The dataset contains demographic and academic information for students, including gender, race/ethnicity, parental education level, lunch type, test preparation course, and scores in math, reading, and writing.

The goal of this project is to:
- Understand how various demographic and socio-economic factors affect academic performance.
- Automate a full analysis and generate a professional-style summary report.
- Demonstrate the end-to-end workflow of **data cleaning → analysis → reporting → visualization**.

---

## 🧠 Project Objectives
1. **Data Cleaning**  
   - Import and process real-world CSV data.  
   - Handle missing or inconsistent values.  
   - Convert numeric fields and standardize categorical ones.

2. **Exploratory Analysis**  
   - Compute class-wide averages for Math, Reading, and Writing.  
   - Compare performance by:
     - Gender  
     - Race/Ethnicity  
     - Parental Education Level  
     - Lunch Type  
     - Test Preparation Course  

3. **Automated Reporting**  
   - Generate a complete text report (`student_performance_summary.txt`).  
   - Create an exportable, multi-page PDF (`Student_Performance_Report_DillanMaart.pdf`) with:
     - Page 1: Executive Summary  
     - Following Pages: Individual Student Reports  

4. **Portfolio Demonstration**  
   - Showcase Python proficiency, structured reporting, and clean presentation.

---

## 🧰 Tools & Technologies
- **Python 3**  
- **Libraries:**  
  - `csv` — data import  
  - `statistics` — mean calculations  
  - `fpdf2` — PDF generation  
- **Dataset:**  
  [Students Performance in Exams (Kaggle)](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)

---

## 📂 File Structure
Student Performance Report/
├── StudentsPerformance.csv # Raw dataset
├── Student Performance Report DillanMaart.py # Main analysis script
├── student_performance_summary.txt # Raw text summary
├── Student_Performance_Report_DillanMaart.pdf # Final professional PDF
└── README.md # Project documentation


---

## 📊 Key Insights
- **Gender:** Females tend to outperform males in reading and writing, while males slightly lead in math.  
- **Parental Education:** Higher parental education levels correlate with higher average scores.  
- **Lunch Type:** Students with standard lunch generally perform better across all subjects.  
- **Test Preparation:** Students who completed the prep course score significantly higher in all subjects.  

---

## 🧩 Future Improvements
- Add **visualization layer** (Power BI / Tableau) for interactive dashboards.  
- Extend analysis to **predict student outcomes** using Pandas and Scikit-learn.  
- Generate **individual PDF reports** for each student automatically.  

---

## 👨‍💻 Author
**Dillan Maart**  
Data Analyst | Python Enthusiast | Storyteller of Data  
*Cape Town, South Africa*  

📧 Contact: dillan.maart@gmail.com 
🌐 Linkedin: https://www.linkedin.com/in/dillan-maart-091976171   

![Project Visual](<IMAGES/Student Performance Dashboard Dillan Maart_page-0001.jpg>)
