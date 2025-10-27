# 💸 Personal Finance Manager (Command-Line App in Python)

A beautiful and functional command-line application to help users manage their personal finances by tracking income, expenses, budgets, and generating financial reports.

---

## 🚀 Features

- 🔐 **User Registration & Login**  
  Secure authentication with hashed passwords using `bcrypt`.

- 💰 **Income & Expense Tracking**  
  Add, update, and delete transactions with category and date.

- 📊 **Financial Reports**  
  Monthly and yearly summaries with total income, expenses, and savings.

- 📉 **Budgeting**  
  Set monthly budgets per category and get alerts when exceeded.

- 💾 **Data Persistence**  
  All data stored in a local SQLite database with backup/restore support.

- 🧪 **Unit Testing**  
  Basic tests included to validate database setup and core functions.

- 🎨 **Aesthetic CLI Interface**  
  Styled using the `rich` library for a pleasant user experience.

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/finance-manager.git
cd finance-manager


### 2. Install Dependencies:
pip install rich bcrypt

### 3. Usage:
python main.py


🛠️ Technologies Used
Python 3.10+

SQLite

Rich (for CLI styling)

Bcrypt (for password hashing)


### Menu Options
Register: Create a new user account

Login: Access your dashboard

Dashboard:

Add Income

Add Expense

Delete Transaction

View Report

Set Budget

Check Budget

Logout