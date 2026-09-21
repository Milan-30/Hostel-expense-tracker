from database import get_connection
from datetime import datetime
def get_amount():
    while True:
        try:
            amt=float(input("Enter the amount:"))
            if amt<0:
                print("Amount must be greater than 0")
            else:
                return amt
        except ValueError:
            print("Enter a valid amount")
def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value
        else:
            print("This field cannot be empty.")
def get_date():
    while True:
        date = input("Enter date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("Please enter a valid date.")
def get_id():
    while True:
        try:
            e_id = int(input("Enter expense ID: "))

            if e_id <= 0:
                print("ID must be greater than 0.")
            else:
                return e_id

        except ValueError:
            print("Please enter a valid ID.")
def add_expense():
    con=get_connection()
    cur=con.cursor()
    c=get_non_empty_input("Enter category: ")
    amt=get_amount()
    d=get_non_empty_input("Enter description: ")
    date=get_date()
    q="insert into expenses values(%s,%s,%s,%s)"
    val=(c,amt,d,date)
    cur.execute(q,val)
    con.commit()
    print("Expense added successfully")
    cur.close()
    con.close()
    
def view_expense():
    con=get_connection()
    cur=con.cursor()
    cur.execute("Select * from expenses")
    expenses=cur.fetchall()
    print("ID".ljust(8), "CATEGORY".ljust(15), "AMOUNT".ljust(10), "DESCRIPTION".ljust(20), "DATE")
    print()
    for expense in expenses:
        print(str(expense[0]).ljust(8),expense[1].ljust(15),str(expense[2]).ljust(10),expense[3].ljust(20),str(expense[4]))
    cur.close()
    con.close()

def search_expense():
    con=get_connection()
    cur=con.cursor()
    print("Search By")
    print("1.ID")
    print("2.Category")
    print("3.Date")
    ch=int(input("Enter your choice(1/2/3):"))
    if ch==1:
        e_id=get_id()
        q="Select * from expenses where id=%s"
        val=(e_id,)
    elif ch==2:
        c=input("Enter the category to be searched:")
        q="Select * from expenses where category=%s"
        val=(c,)
    elif ch==3:
        date=input("Enter the date to be searched(YYYY-MM-DD):")
        q="Select * from expenses where date=%s"
        val=(date,)
    else:
        print("Invalid Choice")
        cur.close()
        con.close()
        return
    cur.execute(q,val)
    expenses=cur.fetchall()
    if len(expenses)==0:
        print("No expense found")
    else:
        print("Search Results")
        print("ID".ljust(8), "CATEGORY".ljust(15), "AMOUNT".ljust(10), "DESCRIPTION".ljust(20), "DATE")
    for expense in expenses:
        print(str(expense[0]).ljust(8),expense[1].ljust(15),str(expense[2]).ljust(10),expense[3].ljust(20),str(expense[4])
    )
    cur.close()
    con.close()
def update_expense():
    con=get_connection()
    cur=con.cursor()
    e_id=get_id()
    q="select * from expenses where id=%s"
    val=(e_id,)
    cur.execute(q,val)
    expense=cur.fetchone()
    if expense is None:
        print("Expense not found")
        cur.close()
        con.close()
        return
    print("Current Expense")
    print("Category    :", expense[1])
    print("Amount      :", expense[2])
    print("Description :", expense[3])
    print("Date        :", expense[4])
    print("Enter new details:")
    c=get_non_empty_input("Enter the category: ")
    a= get_amount()
    d=get_non_empty_input("Enter the description: ")
    dat=get_date()
    q="update expenses set category=%s,amount=%s,description=%s,date=%s where id=%s"
    val=(c,a,d,dat,e_id)
    cur.execute(q,val)
    con.commit()
    print("Expense updated successfully.")
    cur.close()
    con.close()
def delete_expense():
    con=get_connection()
    cur=con.cursor()
    e_id=get_id()
    q="select * from expenses where id=%s"
    val=(e_id,)
    cur.execute(q,val)
    expense=cur.fetchone()
    if expense is None:
        print("Expense not found")
        cur.close()
        con.close()
        return
    print("Expense to be deleted:")
    print("Category    :", expense[1])
    print("Amount      :", expense[2])
    print("Description :", expense[3])
    print("Date        :", expense[4])
    c=input("Are you sure you want to delete this?(y/n):")
    if c.lower()=="y":
        q="delete from expenses where id=%s"
        val=(e_id,)
        cur.execute(q,val)
        con.commit()
        print("Expense deleted successfully")
    else:
        print("Deletion cancelled")
    cur.close()
    con.close()
def total_expense():
    con=get_connection()
    cur=con.cursor()
    q="select sum(amount) from expenses"
    cur.execute(q)
    total=cur.fetchone()[0]
    print("Total Expense:",total)
    cur.close()
    con.close()
def category_expense():
    con=get_connection()
    cur=con.cursor()
    q="select category,sum(amount) from expenses group by category order by sum(amount) desc"
    cur.execute(q)
    expense=cur.fetchall()
    print("CATEGORY-WISE EXPENSES")
    for row in expense:
        print(str(row[0]).ljust(15), "\t", row[1])
    cur.close()
    con.close()
def monthly_expense():
    import calendar
    con=get_connection()
    cur=con.cursor()
    q="select year(date),month(date),sum(amount) from expenses group by year(date),month(date) order by year(date),month(date)"
    cur.execute(q)
    expense=cur.fetchall()
    print("MONTHLY EXPENSES")
    for row in expense:
        month=calendar.month_name[row[1]]
        print(month.ljust(15),row[2])
    cur.close()
    con.close()
def main():
    while True:
        print()
        print("       HOSTEL EXPENSE TRACKER")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search Expense")
        print("4. Update Expense")
        print("5. Delete Expense")
        print("6. Total Expense")
        print("7. Category-wise Summary")
        print("8. Monthly Summary")
        print("9. Exit")
        ch= int(input("Enter your choice: "))
        print()
        if ch==1:
            add_expense()
        elif ch==2:
            view_expense()
        elif ch==3:
            search_expense()
        elif ch==4:
            update_expense()
        elif ch==5:
            delete_expense()
        elif ch==6:
            total_expense()
        elif ch==7:
            category_expense()
        elif ch==8:
            monthly_expense()
        elif ch==9:
            print("Exiting...")
            break
        else:
            print("Invalid choice")
if __name__=="__main__":
    main()


    

    







