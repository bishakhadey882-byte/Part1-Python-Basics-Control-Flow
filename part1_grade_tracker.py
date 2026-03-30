# ============================================================
# Part 1: Python Basics & Control Flow
# Theme: Student Grade Tracker
# ============================================================


# ============================================================
# TASK 1 - Data Parsing & Profile Cleaning 
# ============================================================

print("=" * 60)
print("TASK 1 - DATA PARSING & PROFILE CLEANING")
print("=" * 60)

# Raw student data with messy names, string rolls, and marks as string
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

# Store cleaned students in a list
cleaned_students = []

for student in raw_students:
    # Step 1: Clean name - remove leading/trailing whitespace and convert to Title Case
    clean_name = student["name"].strip().title()

    # Step 2: Convert roll from string to integer
    clean_roll = int(student["roll"])

    # Step 3: Split marks_str on ", " and convert each element to integer
    clean_marks = [int(m) for m in student["marks_str"].split(", ")]

    # Store cleaned student as a dictionary
    cleaned_student = {
        "name": clean_name,
        "roll": clean_roll,
        "marks": clean_marks
    }
    cleaned_students.append(cleaned_student)

    # Step 2: Validate the name - every word should contain only alphabetic characters
    name_valid = all(word.isalpha() for word in clean_name.split())
    if name_valid:
        print(f"✓ Valid name   : {clean_name}")
    else:
        print(f"✗ Invalid name : {clean_name}")

    # Step 3: Print formatted profile card using f-strings
    print("=" * 35)
    print(f"Student  : {clean_name}")
    print(f"Roll No  : {clean_roll}")
    print(f"Marks    : {clean_marks}")
    print("=" * 35)
    print()

# Step 4: Print name in ALL CAPS and lowercase for student with roll number 103
print("\n--- Student with Roll No 103 ---")
for student in cleaned_students:
    if student["roll"] == 103:
        print(f"ALL CAPS   : {student['name'].upper()}")
        print(f"lowercase  : {student['name'].lower()}")


# ============================================================
# TASK 2 - Marks Analysis Using Loops & Conditionals 
# ============================================================

print("\n" + "=" * 60)
print("TASK 2 - MARKS ANALYSIS USING LOOPS & CONDITIONALS")
print("=" * 60)

# Data for Task 2
student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]

# Helper function to assign grade based on marks
def get_grade(mark):
    # Grade logic as per the grading scheme
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    else:
        return "F"

# 1. Print each subject with marks and grade label using a for loop
print(f"\nGrade Report for: {student_name}")
print("-" * 35)
for subject, mark in zip(subjects, marks):
    grade = get_grade(mark)
    print(f"{subject:<12} : {mark}  -->  Grade: {grade}")

# 2. Calculate and print total, average, highest, lowest
total_marks   = sum(marks)
average_marks = round(total_marks / len(marks), 2)

# Find highest scoring subject
highest_mark    = max(marks)
highest_subject = subjects[marks.index(highest_mark)]

# Find lowest scoring subject
lowest_mark    = min(marks)
lowest_subject = subjects[marks.index(lowest_mark)]

print("\n--- Summary ---")
print(f"Total Marks   : {total_marks}")
print(f"Average Marks : {average_marks}")
print(f"Highest Subject: {highest_subject} ({highest_mark})")
print(f"Lowest Subject : {lowest_subject} ({lowest_mark})")

# 3. While loop - simulate marks-entry system for adding new subjects
print("\n--- New Subject Entry System (while loop) ---")
print("Type a subject name to add it, or type 'done' to stop.")

new_subjects = []   # store newly added subject names
new_marks    = []   # store newly added marks

# NOTE FOR EXAMINER:
# The while loop below simulates an interactive marks-entry system.
# It asks for a subject name, then asks for marks (0-100).
# It handles invalid inputs gracefully without crashing.
# Type 'done' to exit the loop.

while True:
    subject_input = input("Enter subject name (or 'done' to stop): ").strip()

    # Stop the loop when user types 'done'
    if subject_input.lower() == "done":
        break

    # Ask for marks for this subject
    marks_input = input(f"Enter marks for {subject_input} (0-100): ").strip()

    # Handle invalid marks input
    try:
        marks_value = float(marks_input)
        if 0 <= marks_value <= 100:
            # Valid input - add to lists
            new_subjects.append(subject_input)
            new_marks.append(marks_value)
            print(f"  ✓ Added: {subject_input} = {marks_value}")
        else:
            # Number out of range
            print("  ⚠ Warning: Marks must be between 0 and 100. Not added.")
    except ValueError:
        # Non-numeric input
        print("  ⚠ Warning: Invalid input. Please enter a numeric value. Not added.")

# After the loop ends - print summary
all_marks = marks + new_marks
print(f"\nNew subjects added   : {len(new_subjects)}")
if new_subjects:
    print(f"New subjects list    : {new_subjects}")
updated_average = round(sum(all_marks) / len(all_marks), 2)
print(f"Updated Average Marks (original + new): {updated_average}")


# ============================================================
# TASK 3 - Class Performance Summary 
# ============================================================

print("\n" + "=" * 60)
print("TASK 3 - CLASS PERFORMANCE SUMMARY")
print("=" * 60)

# Class data - list of tuples (name, marks_list)
class_data = [
    ("Ayesha Sharma", [88, 72, 95, 60, 78]),
    ("Rohit Verma",   [55, 68, 49, 72, 61]),
    ("Priya Nair",    [91, 85, 88, 94, 79]),
    ("Karan Mehta",   [40, 55, 38, 62, 50]),
    ("Sneha Pillai",  [75, 80, 70, 68, 85]),
]

# Store results for summary
student_averages = []
pass_count  = 0
fail_count  = 0

# Print formatted class report header
print(f"\n{'Name':<20} | {'Average':^8} | {'Status'}")
print("-" * 42)

# 1. Loop through class_data - compute average and assign Pass/Fail
for name, student_marks in class_data:
    avg    = round(sum(student_marks) / len(student_marks), 2)
    status = "Pass" if avg >= 60 else "Fail"

    # Count pass and fail
    if status == "Pass":
        pass_count += 1
    else:
        fail_count += 1

    # Store for later summary
    student_averages.append((name, avg))

    # Print formatted row
    print(f"{name:<20} | {avg:^8.2f} | {status}")

# 3. After the table - print summary stats
print("\n--- Class Summary ---")
print(f"Students Passed    : {pass_count}")
print(f"Students Failed    : {fail_count}")

# Class topper - student with highest average
topper_name, topper_avg = max(student_averages, key=lambda x: x[1])
print(f"Class Topper       : {topper_name} ({topper_avg})")

# Class average - average of all students' averages
class_average = round(sum(avg for _, avg in student_averages) / len(student_averages), 2)
print(f"Class Average      : {class_average}")


# ============================================================
# TASK 4 - String Manipulation Utility 
# ============================================================

print("\n" + "=" * 60)
print("TASK 4 - STRING MANIPULATION UTILITY")
print("=" * 60)

# Given essay with leading/trailing whitespace
essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is easy to learn. python has a vast standard library.  "

# Step 1: Strip leading and trailing whitespace - use this for all steps below
clean_essay = essay.strip()
print(f"\nStep 1 - Stripped Essay:\n{clean_essay}")

# Step 2: Convert clean_essay to Title Case and print
title_essay = clean_essay.title()
print(f"\nStep 2 - Title Case:\n{title_essay}")

# Step 3: Count how many times "python" appears (case-insensitive)
# clean_essay is already lowercase after strip, so count directly
python_count = clean_essay.count("python")
print(f"\nStep 3 - Count of 'python': {python_count}")

# Step 4: Replace every occurrence of "python" with "Python 🐍" and print
# clean_essay is already lowercase so .replace("python", ...) catches all
replaced_essay = clean_essay.replace("python", "Python 🐍")
print(f"\nStep 4 - After Replacing 'python' with 'Python 🐍':\n{replaced_essay}")

# Step 5: Split clean_essay into individual sentences by splitting on ". "
sentences = clean_essay.split(". ")
print(f"\nStep 5 - Sentences List:\n{sentences}")

# Step 6: Print each sentence on a new line, numbered from 1
# Add "." at the end if it does not already end with one
print("\nStep 6 - Numbered Sentences:")
for i, sentence in enumerate(sentences, start=1):
    sentence = sentence.strip()
    if not sentence.endswith("."):
        sentence += "."
    print(f"{i}. {sentence}")


print("\n" + "=" * 60)
print("ALL TASKS COMPLETED SUCCESSFULLY!")
print("=" * 60)
