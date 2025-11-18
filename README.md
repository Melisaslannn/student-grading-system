# Student Grading & Information System (CLI)

A Python-based Command Line Interface (CLI) application that simulates a university grading and student management system.

This project demonstrates the use of object-based logic, control flow (match-case), and data structures (dictionaries) to manage academic processes without a database.

## Features
The system supports two distinct user roles: **Staff** and **Student**.

### Staff Capabilities
* **Course Management:** Create new courses and set credit hours/exam dates.
* **Grade Entry:** Input Midterm, Final, and Attendance records.
* **Calculation Engine:** Automatically calculates Letter Grades based on 40% Midterm + 60% Final.
* **Appeals:** Review and Approve/Reject grade appeals from students.

### Student Capabilities
* **View Results:** Access detailed grade reports, GPA, and pass/fail status.
* **Appeals:** Submit formal appeals for specific grades.

### System Rules & Logic
* **Automatic Failure:** The system automatically assigns a failing grade if:
    * Final Grade is below 50.
    * Attendance is below 70%.
* **Runtime Data:** Data is stored in memory (dictionaries) and resets when the program closes.

## 🛠️ Requirements
* **Python 3.10 or higher** is required

## 🔐 Demo Credentials
You can use these pre-defined accounts to test the system:
**Staff `staff` , `pass123` 
**Student `melisa` , `cs123` 

## 🔮 Future Plans (To-Do)
* [ ] **Database Integration:** Implement SQLite for persistent data storage.
* [ ] **Security:** Hash user passwords instead of storing them as plain text.
* [ ] **GUI:** Add a Graphical User Interface using Tkinter or PyQt.
