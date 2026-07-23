import csv
import sys
import os

def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists,
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")

    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)

    assignments = []

    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric fields to floats for calculations
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    """
    'data' is a list of dictionaries containing the assignment records.
    """
    print("\n--- Processing Grades ---")

    # Refuse to work with an empty file
    if len(data) == 0:
        print("Error: the file has no grade records to process.")
        return

    # a) Check every score is between 0 and 100
    bad_scores = []
    for row in data:
        if row['score'] < 0 or row['score'] > 100:
            bad_scores.append(row)

    if len(bad_scores) > 0:
        print("Invalid scores found (must be 0-100):")
        for row in bad_scores:
            print(f"  {row['assignment']}: {row['score']}")
        return
    print("All scores are valid.")

    # b) Validate the weights: total 100, Formative 60, Summative 40
    total_weight = 0
    formative_weight = 0
    summative_weight = 0
    for row in data:
        total_weight += row['weight']
        if row['group'] == 'Formative':
            formative_weight += row['weight']
        else:
            summative_weight += row['weight']

    if abs(total_weight - 100) > 0.01:
        print(f"Error: total weight must be 100, but it is {total_weight}.")
        return
    if abs(formative_weight - 60) > 0.01:
        print(f"Error: Formative weights must total 60, but they total {formative_weight}.")
        return
    if abs(summative_weight - 40) > 0.01:
        print(f"Error: Summative weights must total 40, but they total {summative_weight}.")
        return
    print("Weight distribution is valid (100 total, 60/40 split).")

    # c) Calculate the final grade, GPA, and category percentages
    total_grade = 0
    formative_earned = 0
    summative_earned = 0
    for row in data:
        contribution = row['score'] * row['weight'] / 100
        total_grade += contribution
        if row['group'] == 'Formative':
            formative_earned += contribution
        else:
            summative_earned += contribution

    gpa = (total_grade / 100) * 5.0
    formative_percent = formative_earned / formative_weight * 100
    summative_percent = summative_earned / summative_weight * 100

    print(f"\nFinal Grade: {total_grade:.2f} / 100")
    print(f"GPA: {gpa:.3f} / 5.0")
    print(f"Formative category: {formative_earned:.2f} / {formative_weight:.0f} ({formative_percent:.2f}%)")
    print(f"Summative category: {summative_earned:.2f} / {summative_weight:.0f} ({summative_percent:.2f}%)")

if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()

    # 2. Process the features
    evaluate_grades(course_data)
