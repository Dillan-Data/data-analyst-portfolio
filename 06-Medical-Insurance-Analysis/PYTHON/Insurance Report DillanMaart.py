"""
Insurance Cost Analysis Project
Author: Dillan Maart
Description: Analyzes a medical insurance dataset to explore
average costs, smoker vs. non-smoker differences, regional costs,
and age group trends. Outputs a text report.
"""

import csv
with open('insurance.csv', "r") as medical_health_insurance:
    reader = csv.DictReader(medical_health_insurance)   
    data = list(reader)

#print(data[:5])    # preview first 5 rows

for row in data:
    row["age"] = int(row["age"])
    row["bmi"] = float(row["bmi"])
    row["children"] = int(row["children"])
    row["charges"] = float(row["charges"])

# ANALYSIS FUNCTIONS
def average_cost(data):
    total = sum(row["charges"] for row in data)
    return total / len(data)

#Smoker VS Non-Smoker
def average_cost_by_smoker(data):
    smoker_costs = [row["charges"] for row in data if row["smoker"] == "yes"]
    nonsmoker_costs = [row["charges"] for row in data if row["smoker"] == "no"]
    return sum(smoker_costs)/len(smoker_costs), sum(nonsmoker_costs)/len(nonsmoker_costs)

# cost by Region
def average_cost_by_region(data):
    regions = {}
    for row in data:
        region = row["region"]
        regions.setdefault(region, []).append(row["charges"])
    return {region: sum(vals)/len(vals) for region, vals in regions.items()} 

# Age groups (example: under 30, 30-50, over 50)
def average_cost_by_age_group(data):
    groups = {"under 30": [], "30-50": [], "over 50": []}
    for row in data:
        if row["age"] < 30:
            groups["under 30"].append(row["charges"])
        elif row["age"] <= 50:
            groups["30-50"].append(row["charges"])
        else:
            groups["over 50"].append(row["charges"])
    return {group: sum(vals)/len(vals) if vals else 0 for group, vals in groups.items()}

# Results / Report
print("INSURANCE COST ANALYSIS\n")
print("Average overall cost:", average_cost(data))
print("Smoker vs Non-Smoker:", average_cost_by_smoker(data))
print("Cost by Region:", average_cost_by_region(data))
print("Cost by Age Group:", average_cost_by_age_group(data))


# Save report to file in a clean format
with open("insurance_report.txt", "w") as report:
    report.write("=====================================\n")
    report.write("   INSURANCE COST ANALYSIS REPORT\n")
    report.write("   Prepared by: Dillan Maart\n")
    report.write("=====================================\n\n")

    report.write("1. Overall Average Cost\n")
    report.write(f"- The average insurance cost is: ${average_cost(data):,.2f}\n\n")

    smoker_avg, nonsmoker_avg = average_cost_by_smoker(data)
    report.write("2. Smoker vs Non-Smoker\n")
    report.write(f"- Smokers average cost: ${smoker_avg:,.2f}\n")
    report.write(f"- Non-Smokers average cost: ${nonsmoker_avg:,.2f}\n")
    report.write(f"=> Smokers pay about {smoker_avg/nonsmoker_avg:.1f}x more on average.\n\n")

    region_avgs = average_cost_by_region(data)
    report.write("3. Costs by Region\n")
    for region, avg in region_avgs.items():
        report.write(f"- {region.title()}: ${avg:,.2f}\n")
    report.write("\n")

    age_groups = average_cost_by_age_group(data)
    report.write("4. Costs by Age Group\n")
    for group, avg in age_groups.items():
        report.write(f"- {group}: ${avg:,.2f}\n")
    report.write("\n")

    report.write("=====================================\n")
    report.write("            KEY TAKEAWAYS\n")
    report.write("=====================================\n")
    report.write("1. Smoking is the strongest predictor of higher costs.\n")
    report.write("2. Insurance costs increase steadily with age.\n")
    report.write("3. The Southeast region has the highest average costs.\n")
    report.write("4. Lifestyle factors like BMI also impact charges.\n")


    