# Part1-Python-Basics-Control-Flow

### Theme: Student Grade Tracker

---

## 📌 Overview

This project builds a command-line **Student Grade Tracker** that manages student data, computes results, and provides a summary report — all using core Python concepts like loops, conditionals, string manipulation, and data parsing.

---

## 📁 Repository Structure

```
├── part1_grade_tracker.py      # Main Python script (all 4 tasks)
└── README.md                     # Project documentation
```

---

## 🛠️ Tasks Completed

### ✅ Task 1 — Data Parsing & Profile Cleaning 
- Looped through `raw_students` list containing messy real-world data
- Cleaned each student's name by removing leading/trailing whitespace and converting to **Title Case**
- Converted `roll` from string to **integer**
- Split `marks_str` on `", "` and converted each value to **integer** to produce a `marks` list
- Validated each name — checked every word contains only **alphabetic characters**
- Printed `✓ Valid name` or `✗ Invalid name` for each student
- Printed a **formatted profile card** using f-strings for each student
- Printed the name in **ALL CAPS** and **lowercase** for the student with roll number `103`

### ✅ Task 2 — Marks Analysis Using Loops & Conditionals 
- Used a **for loop** with `zip()` to print each subject alongside its marks and a **grade label** based on this scheme:

| Marks Range | Grade |
|-------------|-------|
| 90 – 100    | A+    |
| 80 – 89     | A     |
| 70 – 79     | B     |
| 60 – 69     | C     |
| Below 60    | F     |

- Calculated and printed:
  - **Total marks** (sum of all subjects)
  - **Average marks** (rounded to 2 decimal places)
  - **Highest scoring subject** (name + marks)
  - **Lowest scoring subject** (name + marks)
- Simulated a **marks-entry system using a while loop**:
  - Asks for a subject name, then marks (0–100) in each iteration
  - Stops when user types `done`
  - Handles **invalid inputs** (non-numeric values, out-of-range numbers) with a warning — does not crash
  - Prints how many new subjects were added and the **updated average** across all subjects

### ✅ Task 3 — Class Performance Summary 
- Looped through `class_data` (list of tuples) for all 5 students
- Computed each student's **average** (rounded to 2 decimal places)
- Assigned **result status**: `Pass` if average ≥ 60, else `Fail`
- Printed a **formatted class report table**:

```
Name                 | Average  | Status
------------------------------------------
Ayesha Sharma        |  78.60   | Pass
Rohit Verma          |  61.00   | Pass
Priya Nair           |  87.40   | Pass
Karan Mehta          |  49.00   | Fail
Sneha Pillai         |  75.60   | Pass
```

- After the table, printed:
  - **Number of students who passed and failed**
  - **Class topper** (name + average)
  - **Class average** (average of all five students' averages)

### ✅ Task 4 — String Manipulation Utility 
- Given a raw essay string with leading/trailing whitespace
- Performed the following operations step by step:
  1. **Stripped** whitespace → stored as `clean_essay`
  2. Converted to **Title Case** and printed
  3. **Counted** occurrences of the word `"python"` (case-insensitive)
  4. **Replaced** every `"python"` with `"Python 🐍"` and printed
  5. **Split** into individual sentences on `". "`
  6. Printed each sentence **numbered from 1**, adding `"."` at the end if missing

---

## ▶️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/bishakhadey882-byte/Part1-Python-Basics-and-Control-Flow.git
cd Part1-Python-Basics-and-Control-Flow
```

### 2. Make sure Python is installed
```bash
python --version
```
> No external libraries needed — this project uses **pure Python only!**

### 3. Run the script
```bash
python "part1_grade_tracker.py"
```

### 4. Interactive Input (Task 2 — While Loop)
When the program reaches Task 2's while loop, it will ask you to enter new subjects interactively:
```
Enter subject name (or 'done' to stop): Hindi
Enter marks for Hindi (0-100): 75
  ✓ Added: Hindi = 75.0
Enter subject name (or 'done' to stop): done
```
Type `done` to exit the loop and continue the program.

---

## 📦 Concepts Used

| Concept | Where Used |
|---------|------------|
| `for` loop | Task 1, Task 2, Task 3 |
| `while` loop | Task 2 — marks entry system |
| String methods (`.strip()`, `.title()`, `.split()`, `.replace()`, `.count()`) | Task 1, Task 4 |
| f-strings | Task 1, Task 2, Task 3, Task 4 |
| List comprehension | Task 1 — parsing marks |
| `try / except` | Task 2 — invalid input handling |
| Conditionals (`if / elif / else`) | Task 2 — grading, Task 3 — pass/fail |
| `zip()` | Task 2 — subject + marks loop |
| `max()` with `lambda` | Task 3 — class topper |
| Dictionary & List operations | Task 1, Task 3 |

---

## 📝 Sample Output Preview

```
============================== TASK 1 ==============================
✓ Valid name   : Ayesha Sharma
===================================
Student  : Ayesha Sharma
Roll No  : 101
Marks    : [88, 72, 95, 60, 78]
===================================

============================== TASK 2 ==============================
Grade Report for: Ayesha Sharma
-----------------------------------
Math         : 88  -->  Grade: A
Physics      : 72  -->  Grade: B
CS           : 95  -->  Grade: A+
English      : 60  -->  Grade: C
Chemistry    : 78  -->  Grade: B

Total Marks   : 393
Average Marks : 78.6
Highest Subject: CS (95)

Lowest Subject : English (60)

============================== TASK 3 ==============================
Name                 | Average  | Status
------------------------------------------
Ayesha Sharma        |  78.60   | Pass
Rohit Verma          |  61.00   | Pass
Priya Nair           |  87.40   | Pass
Karan Mehta          |  49.00   | Fail
Sneha Pillai         |  75.60   | Pass

Students Passed : 4
Students Failed : 1
Class Topper    : Priya Nair (87.4)
Class Average   : 70.32
