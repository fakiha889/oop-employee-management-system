# oop-employee-management-system
# 💼 Employee Management and Payroll System

## 📌 Project Overview

The Employee Management and Payroll System is a Python-based project developed using Object-Oriented Programming (OOP) concepts. The system manages different employee roles and calculates bonuses according to their responsibilities.

This project demonstrates the practical implementation of Inheritance, Encapsulation, Method Overriding, and Polymorphism in a real-world business environment.

---

## 🚀 Features

### Employee (Parent Class)

* Store employee information

  * Name
  * Salary
  * Employee ID
* Display employee details
* Generate employee reports

### Manager

* Inherits from Employee
* Calculates a 20% bonus

### Developer

* Inherits from Employee
* Calculates a 15% bonus

### Designer

* Inherits from Employee
* Calculates a 10% bonus

---

## 💡 OOP Concepts Implemented

### Inheritance

Manager, Developer, and Designer classes inherit common properties and methods from the Employee class.

### Encapsulation

Employee IDs and internal reports are protected using private variables and private methods.

### Method Overriding

Each employee role overrides the bonus calculation method according to its own business rules.

### Polymorphism

Different employee objects respond differently to the same method calls while sharing a common interface.

---

## 🛠 Technologies Used

* Python 3
* Object-Oriented Programming (OOP)

---

## 📂 Project Structure

```text
Employee
│
├── Manager
├── Developer
└── Designer
```

---

## ▶️ How to Run

1. Install Python 3.
2. Clone or download the repository.
3. Open the project folder.
4. Run the Python file:

```bash
python employee_management_system.py
```

---

## 🎯 Learning Outcomes

This project demonstrates:

* Classes and Objects
* Constructors
* Inheritance
* Encapsulation
* Public, Protected, and Private Members
* Method Overriding
* Polymorphism
* Real-world Payroll System Design

---

## 📈 Business Scenario

A software company employs Managers, Developers, and Designers. Each employee has common information such as name, salary, and employee ID, while each role follows different bonus policies. The system manages employee records and payroll calculations efficiently using OOP principles.

---

## 👩‍💻 Author

Fakiha Abdul Jabbar

Computer Science Student

Python Developer | OOP Learner
