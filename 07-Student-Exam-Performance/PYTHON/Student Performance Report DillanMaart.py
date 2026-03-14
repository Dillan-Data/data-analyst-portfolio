import csv
from statistics import mean

# ---------------------------
# Helper utilities
# ---------------------------
def safe_avg(nums):
    """Average ignoring None values. Returns 0 if no valid numbers."""
    vals = [n for n in nums if n is not None]
    return sum(vals) / len(vals) if vals else 0

def to_int_safe(val):
    """Try to convert to int; return None on failure."""
    try:
        return int(float(val))
    except Exception:
        return None

# ---------------------------
# 1) Load and NORMALIZE headers
# ---------------------------
data = []
with open("StudentsPerformance.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    # Create mapping of normalized header -> original header to be safe
    field_map = {}
    for field in reader.fieldnames:
        # normalize: strip, lower, remove quotes
        norm = field.strip().lower().replace('"', '')
        field_map[norm] = field

    for row in reader:
        # create normalized-row dict with normalized keys
        norm_row = {}
        for norm_key, orig_key in field_map.items():
            val = row.get(orig_key, "").strip()
            norm_row[norm_key] = val
        data.append(norm_row)

# quick sanity check (uncomment to debug)
# print("Fields:", list(field_map.keys()))

# ---------------------------
# 2) Convert numeric columns safely
#    We expect keys like 'math score', 'reading score', 'writing score'
# ---------------------------
for row in data:
    row['math score'] = to_int_safe(row.get('math score', None))
    row['reading score'] = to_int_safe(row.get('reading score', None))
    row['writing score'] = to_int_safe(row.get('writing score', None))

# ---------------------------
# 3) Grouping function (safe)
# ---------------------------
def group_average(data_rows, group_by_key):
    """
    group_by_key must be the normalized header name, e.g. 'gender' or 'race/ethnicity'
    returns dict: group_value -> {'math': avg, 'reading': avg, 'writing': avg}
    """
    groups = {}
    for row in data_rows:
        key = row.get(group_by_key) or "Unknown"
        if key == "":
            key = "Unknown"
        if key not in groups:
            groups[key] = {'math': [], 'reading': [], 'writing': []}
        # only add numeric values
        if row.get('math score') is not None:
            groups[key]['math'].append(row['math score'])
        if row.get('reading score') is not None:
            groups[key]['reading'].append(row['reading score'])
        if row.get('writing score') is not None:
            groups[key]['writing'].append(row['writing score'])

    # compute averages (safe_avg handles empty lists)
    result = {}
    for k, subj in groups.items():
        result[k] = {
            'math': round(safe_avg(subj['math'])) if subj['math'] else None,
            'reading': round(safe_avg(subj['reading'])) if subj['reading'] else None,
            'writing': round(safe_avg(subj['writing'])) if subj['writing'] else None
        }
    return result

# ---------------------------
# 4) Compute overall averages
# ---------------------------
math_vals = [r['math score'] for r in data if r['math score'] is not None]
reading_vals = [r['reading score'] for r in data if r['reading score'] is not None]
writing_vals = [r['writing score'] for r in data if r['writing score'] is not None]
total_avgs_per_student = []
for r in data:
    scores = [s for s in (r['math score'], r['reading score'], r['writing score']) if s is not None]
    if scores:
        total_avgs_per_student.append(sum(scores) / len(scores))

overall_math = round(safe_avg(math_vals))
overall_reading = round(safe_avg(reading_vals))
overall_writing = round(safe_avg(writing_vals))
overall_total = round(safe_avg(total_avgs_per_student))

# ---------------------------
# 5) Grouped comparisons
# Note: use normalized keys: 'gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course'
# ---------------------------
gender_avgs = group_average(data, 'gender')
race_avgs = group_average(data, 'race/ethnicity')
education_avgs = group_average(data, 'parental level of education')
lunch_avgs = group_average(data, 'lunch')
testprep_avgs = group_average(data, 'test preparation course')

# ---------------------------
# 6) Write the summary report (rounded whole numbers)
# ---------------------------
with open("student_performance_summary.txt", "w", encoding="utf-8") as report:
    report.write("STUDENT PERFORMANCE REPORT\n")
    report.write("="*50 + "\n\n")
    report.write(f"Total Students (rows): {len(data)}\n")
    report.write(f"Overall Math Average: {overall_math}\n")
    report.write(f"Overall Reading Average: {overall_reading}\n")
    report.write(f"Overall Writing Average: {overall_writing}\n")
    report.write(f"Overall Total Average: {overall_total}\n\n")

    report.write("Average Scores by Gender:\n")
    for gender, scores in gender_avgs.items():
        report.write(f"  {gender.title()}: {scores}\n")

    report.write("\nAverage Scores by Race/Ethnicity:\n")
    for race, scores in race_avgs.items():
        report.write(f"  {race}: {scores}\n")

    report.write("\nAverage Scores by Parental Education Level:\n")
    for level, scores in education_avgs.items():
        report.write(f"  {level.title()}: {scores}\n")

    report.write("\nAverage Scores by Lunch Type:\n")
    for lunch, scores in lunch_avgs.items():
        report.write(f"  {lunch.title()}: {scores}\n")

    report.write("\nAverage Scores by Test Preparation Course:\n")
    for prep, scores in testprep_avgs.items():
        report.write(f"  {prep.title()}: {scores}\n")

    report.write("\nReport generated successfully.\n")

# ---------------------------
# 7) Append individual student reports
# ---------------------------
with open("student_performance_summary.txt", "a", encoding="utf-8") as report:
    report.write("\n" + "="*60 + "\n")
    report.write("INDIVIDUAL STUDENT PERFORMANCE\n")
    report.write("="*60 + "\n\n")

    for i, student in enumerate(data, start=1):
        name = f"Student {i}"
        gender = student.get('gender', 'Unknown')
        race = student.get('race/ethnicity', 'Unknown')
        parent_edu = student.get('parental level of education', 'Unknown')
        lunch = student.get('lunch', 'Unknown')
        test_prep = student.get('test preparation course', 'Unknown')

        # show "N/A" for missing scores, otherwise whole number
        math_score_raw = student.get('math score')
        reading_score_raw = student.get('reading score')
        writing_score_raw = student.get('writing score')

        math_score = str(round(math_score_raw)) if math_score_raw is not None else "N/A"
        reading_score = str(round(reading_score_raw)) if reading_score_raw is not None else "N/A"
        writing_score = str(round(writing_score_raw)) if writing_score_raw is not None else "N/A"

        # compute average if at least one score exists
        scores_present = [v for v in (math_score_raw, reading_score_raw, writing_score_raw) if v is not None]
        avg_score = round(sum(scores_present) / len(scores_present)) if scores_present else "N/A"

        if isinstance(avg_score, (int, float)):
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
        else:
            performance = "N/A"

        report.write(f"Student: {name}\n")
        report.write(f"Gender: {gender} | Race: {race}\n")
        report.write(f"Parental Education: {parent_edu}\n")
        report.write(f"Lunch: {lunch} | Test Prep: {test_prep}\n")
        report.write(f"Scores → Math: {math_score} | Reading: {reading_score} | Writing: {writing_score}\n")
        report.write(f"Average Score: {avg_score}\n")
        report.write(f"Performance: {performance}\n")
        report.write("-" * 60 + "\n\n")

print("Report generation complete: student_performance_summary.txt")
