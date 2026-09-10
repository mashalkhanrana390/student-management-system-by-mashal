# 🎓 Student Management System by Mashal

A simple **Student Management System** built with **Python**. This beginner-friendly console application allows users to add student information and view stored student records.

The project is designed to practice important Python concepts such as **functions, lists, dictionaries, loops, conditional statements, and user input**.

---

## 📌 Project Overview

The Student Management System provides a simple menu where the user can:

1. Add a student
2. View all students
3. Exit the program

Student information includes:

* Name
* Roll Number
* Department
* GPA
* Semester

---

## ✨ Features

* ✅ Add student records
* ✅ View all student records
* ✅ Store multiple students
* ✅ Store student information using dictionaries
* ✅ Menu-driven console interface
* ✅ Input validation through data conversion
* ✅ Simple and beginner-friendly Python code

---

## 🛠️ Technologies Used

* **Python 3**
* Lists
* Dictionaries
* Functions
* `if / elif / else`
* `while` loop
* `for` loop
* User input
* Type conversion

---

## 📂 Project Structure

```text
student-management-system-by-mashal/
│
├── main.py
└── README.md
```

---

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/student-management-system-by-mashal.git
```

### 2. Open the Project

```bash
cd student-management-system-by-mashal
```

### 3. Run the Program

On Windows:

```bash
py main.py
```

Or:

```bash
python main.py
```

---

## 💻 How It Works

When the program starts, it displays a menu:

```text
==== STUDENT MANAGEMENT SYSTEM ====

1. Add student.
2. View students.
3. Exit.

Enter your choice:
```

### Option 1 — Add Student

The program asks for:

```text
Enter the name:
Enter your roll_no:
Enter the department:
Enter your gpa:
Enter your semester:
```

The information is stored in a dictionary and then added to the `students` list.

### Option 2 — View Students

The program displays all students currently stored in the list.

Example:

```text
------------------------
name: Mashal Khan
roll_no: 46
department: AI
gpa: 3.5
semester: 2nd
```

### Option 3 — Exit

The program closes when the user selects option `3`.

---

## 🧠 Python Concepts Used

### 1. List

```python
students = []
```

A list is used to store multiple student records.

---

### 2. Dictionary

```python
student = {
    "name": name,
    "roll_no": roll_no,
    "department": department,
    "gpa": gpa,
    "semester": semester
}
```

A dictionary stores the information of one student using key-value pairs.

---

### 3. Function

The project uses separate functions to organize the code.

```python
def add_student():
```

```python
def view_student():
```

```python
def main():
```

Functions make the program easier to understand and manage.

---

### 4. `input()`

The `input()` function takes information from the user.

```python
name = input("Enter the name: ")
```

---

### 5. `int()`

The `int()` function converts the roll number into an integer.

```python
roll_no = int(input("Enter your roll_no: "))
```

---

### 6. `float()`

The `float()` function converts GPA into a decimal number.

```python
gpa = float(input("Enter your gpa: "))
```

---

### 7. `append()`

The `append()` method adds the student dictionary to the list.

```python
students.append(student)
```

---

### 8. `if / elif / else`

Conditional statements are used to process the user's menu choice.

```python
if choice == "1":
    add_student()
elif choice == "2":
    view_student()
elif choice == "3":
    break
else:
    print("Invalid choice")
```

---

### 9. `while` Loop

The `while True` loop keeps the menu running until the user selects Exit.

```python
while True:
```

---

### 10. `for` Loop

The `for` loop is used to display each student.

```python
for student in students:
```

---

### 11. `return`

The `return` statement exits the function when there are no students.

```python
if not students:
    print("No student found.")
    return
```

---

### 12. `break`

The `break` statement stops the main loop.

```python
if choice == "3":
    print("Program closed.")
    break
```

---

## 📋 Complete Code

```python
students = []


def add_student():
    name = input("Enter the name: ")
    roll_no = int(input("Enter your roll_no: "))
    department = input("Enter the department: ")
    gpa = float(input("Enter your gpa: "))
    semester = input("Enter your semester: ")

    student = {
        "name": name,
        "roll_no": roll_no,
        "department": department,
        "gpa": gpa,
        "semester": semester
    }

    students.append(student)
    print("Student added successfully!")


def view_student():
    if not students:
        print("No student found.")
        return

    for student in students:
        print("------------------------")
        print("Name:", student["name"])
        print("Roll No:", student["roll_no"])
        print("Department:", student["department"])
        print("GPA:", student["gpa"])
        print("Semester:", student["semester"])


def main():
    while True:
        print("\n==== STUDENT MANAGEMENT SYSTEM ====")
        print("1. Add student")
        print("2. View students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_student()

        elif choice == "3":
            print("Program closed.")
            break

        else:
            print("Invalid choice.")


main()
```

---

## 🎯 Learning Goals

This project helped practice:

* Python functions
* Lists
* Dictionaries
* Loops
* Conditional statements
* User input
* Type conversion
* Basic program structure
* Menu-driven applications

---

## 🚀 Future Improvements

The project can be improved by adding:

* 🔍 Search student by roll number
* ✏️ Update student information
* 🗑️ Delete student
* 💾 Save student records to a file
* 📂 Load records when the program starts
* 📊 Calculate average GPA
* 🔐 Add login system
* 🖥️ Create a graphical user interface
* 🗄️ Connect the system to a database

---

## 👨‍💻 Author

**Mashal Khan**

**Artificial Intelligence Student | Python Developer | Future AI Engineer**

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is created for **learning and educational purposes**.
