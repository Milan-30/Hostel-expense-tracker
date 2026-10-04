# Hostel Expense Tracker

A Python and MySQL based expense management system designed to track, manage, and analyze hostel expenses.

## Project Overview

Hostel Expense Tracker is a console-based application developed to manage daily hostel expenses.

The application allows users to add, view, search, update, and delete expenses. It also provides category-wise and monthly summaries. Pandas is used for data analysis, and Matplotlib is used to visualize spending patterns through graphs.

MySQL is used as the database for storing expense records.

## Features

* Add new expenses
* View all expenses
* Search expenses by date
* Update existing expenses
* Delete expenses
* Calculate total expenses
* View category-wise expense summaries
* View monthly expense summaries
* Visualize expenses using graphs
* Generate expense insights
* Input validation for amounts, IDs, and dates
* Store expense data using MySQL

## Technologies Used

* Python
* MySQL
* MySQL Connector/Python
* Pandas
* Matplotlib
* Git & GitHub

## Project Structure

```text
Hostel Expense Tracker/
│
├── main.py          # Main application and menu
├── database.py      # MySQL database connection
├── analysis.py      # Pandas analysis and Matplotlib graphs
├── .gitignore       # Files excluded from Git
└── README.md        # Project documentation
```

## Database

The project uses a MySQL database named `expense_tracker`.

The main table is `expenses`.

| Column      | Description                |
| ----------- | -------------------------- |
| ID          | Unique expense ID          |
| CATEGORY    | Expense category           |
| AMOUNT      | Expense amount             |
| DESCRIPTION | Description of the expense |
| DATE        | Date of the expense        |

### Create Database

```sql
CREATE DATABASE expense_tracker;
```

### Create Expenses Table

```sql
CREATE TABLE expenses (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    CATEGORY VARCHAR(50),
    AMOUNT DECIMAL(10,2),
    DESCRIPTION VARCHAR(255),
    DATE DATE);
```

## Expense Categories

The application uses categories such as:

* Food
* Travel
* Snacks
* Recharge
* Stationery
* Entertainment
* Miscellaneous

## Application Menu

```text
1. Add Expense
2. View All Expenses
3. Search Expense
4. Update Expense
5. Delete Expense
6. Total Expense
7. Category-wise Summary
8. Monthly Summary
9. View Graphs
10. Expense Insights
11. Exit
```

## Expense Insights

The application provides additional insights from the stored expense data, including:

* Total expense
* Average expense
* Number of expenses
* Highest individual expense
* Highest spending category
* Highest spending month

## Data Analysis

Pandas is used to load and analyze expense data retrieved from MySQL.

The project performs:

* Total expense calculation
* Category-wise aggregation
* Monthly expense analysis
* Identification of highest spending categories
* Identification of highest spending months

## Visualization

Matplotlib is used to visualize expense data.

The application provides:

* Category-wise expense visualization
* Monthly expense trend visualization

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Milan-30/Hostel-expense-tracker.git
```

### 2. Open the project folder

```bash
cd Hostel-expense-tracker
```

### 3. Install the required Python packages

```bash
py -m pip install mysql-connector-python pandas matplotlib
```

### 4. Set up MySQL

Create the database:

```sql
CREATE DATABASE expense_tracker;
```

Then create the `expenses` table:

```sql
CREATE TABLE expenses (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    CATEGORY VARCHAR(50),
    AMOUNT DECIMAL(10,2),
    DESCRIPTION VARCHAR(255),
    DATE DATE
);
```

### 5. Configure the database connection

Update the MySQL username and password in `database.py`.

**Do not upload your actual MySQL password to GitHub.**

### 6. Run the application

```bash
py main.py
```

## What I Learned

Through this project, I practiced:

* Python functions and modular programming
* MySQL database operations
* SQL queries and aggregation
* Python-MySQL connectivity
* Input validation
* Pandas data analysis
* Matplotlib visualization
* Git and GitHub version control
* Organizing a Python project into multiple files

## Future Improvements

Possible future improvements include:

* Exporting expense reports to CSV or Excel
* Adding a graphical user interface
* Adding budget tracking
* Adding monthly budget alerts
* Improving data visualization

## Author

**Milan Shaji Varkey**

B.Tech CSE Student
