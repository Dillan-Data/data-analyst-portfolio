from fpdf import FPDF
import csv
from statistics import mean

# Helper functions
def safe_avg(nums):
    vals = [n for n in nums if n is not None]
    return sum(vals) / len(vals) if vals else 0

def to_int_safe(val):
    try:
        return int(float(val))
    except:
        return None

# Load data
data = []
with open("StudentsPerformance.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append({
            "gender": row["gender"],
            "race": row["race/ethnicity"],
            "parent_edu": row["parental level of education"],
            "lunch": row["lunch"],
            "test_prep": row["test preparation course"],
            "math": to_int_safe(row["math score"]),
            "reading": to_int_safe(row["reading score"]),
            "writing": to_int_safe(row["writing score"]),
        })

# Class-wide averages
avg_math = round(safe_avg([r["math"] for r in data]))
avg_reading = round(safe_avg([r["reading"] for r in data]))
avg_writing = round(safe_avg([r["writing"] for r in data]))
avg_total = round(safe_avg([(r["math"] + r["reading"] + r["writing"]) / 3 for r in data]))

# PDF setup
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Define fonts
pdf.set_font("Helvetica", size=12)

# 1️⃣ PAGE ONE - SUMMARY
pdf.add_page()
pdf.set_font("Helvetica", style="B", size=16)
pdf.cell(0, 10, "Student Performance Report", ln=True, align="C")
pdf.ln(10)

pdf.set_font("Helvetica", size=12)
pdf.multi_cell(0, 8, f"""
This report summarizes class-wide and individual student performance across
Math, Reading, and Writing. All values are rounded to the nearest whole number.
""")

pdf.ln(5)
pdf.set_font("Helvetica", style="B", size=12)
pdf.cell(0, 8, "Class Summary", ln=True)
pdf.set_font("Helvetica", size=12)

pdf.cell(0, 8, f"Total Students: {len(data)}", ln=True)
pdf.cell(0, 8, f"Average Math Score: {avg_math}", ln=True)
pdf.cell(0, 8, f"Average Reading Score: {avg_reading}", ln=True)
pdf.cell(0, 8, f"Average Writing Score: {avg_writing}", ln=True)
pdf.cell(0, 8, f"Overall Average: {avg_total}", ln=True)
pdf.ln(5)

pdf.multi_cell(0, 8, "See following pages for individual student breakdowns.")

# 2️⃣ PAGES TWO+ - INDIVIDUAL REPORTS
for i, s in enumerate(data, start=1):
    pdf.add_page()
    pdf.set_font("Helvetica", style="B", size=14)
    pdf.cell(0, 10, f"Student {i} Report", ln=True)
    pdf.set_font("Helvetica", size=12)
    pdf.cell(0, 8, f"Gender: {s['gender']} | Race: {s['race']}", ln=True)
    pdf.cell(0, 8, f"Parental Education: {s['parent_edu']}", ln=True)
    pdf.cell(0, 8, f"Lunch: {s['lunch']} | Test Prep: {s['test_prep']}", ln=True)
    pdf.ln(3)
    pdf.cell(0, 8, f"Math: {s['math']} | Reading: {s['reading']} | Writing: {s['writing']}", ln=True)

    avg_score = round(safe_avg([s["math"], s["reading"], s["writing"]]))
    pdf.cell(0, 8, f"Average Score: {avg_score}", ln=True)

    if avg_score >= 80:
        performance = "Excellent"
    elif avg_score >= 70:
        performance = "Good"
    elif avg_score >= 60:
        performance = "Average"
    elif avg_score >= 50:
        performance = "Below Average"
    else:
        performance = "Poor"
    pdf.cell(0, 8, f"Performance: {performance}", ln=True)

# Save PDF
pdf.output("Student_Performance_Report_DillanMaart.pdf")
print("PDF successfully created: Student_Performance_Report_DillanMaart.pdf")
