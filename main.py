from database import get_connection
def add_expense():
    con=get_connection()
    cur=con.cursor()
    c=input("Enter the category:")
    amt=float(input("Enter the amount:"))
    d=input("Enter the description:")
    date=input("Enter the date(YYYY-MM-DD):")
    q="insert from expenses values(%s,%s,%s,%s)"
    val=(c,amt,d,date)
    cur.execute(q,val)
    con.commit()
    print("Expense added successfully")
    cur.close()
    con.close()
    
def view_expenses():
    con=get_connection()
    cur=con.cursor()
    cur.execute("Select * from expenses")
    expenses=cur.fetchall()
    for row in expenses:
        print(row)
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
        e_id=int(input("Enter the ID to be searched:"))
        q="Select * from expenses where id=%s"
        val=(e_id,)
    elif ch==2:
        c=input("Enter the category to be searched:")
        q="Select * from expenses where category=%s"
        val=(c,)
    elif ch==3:
        d=input("Enter the date to be searched(YYYY-MM-DD):")
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
        printf("No expense found")
    else:
        print("Search Results")
        print("ID\tCATEGORY\tAMOUNT\tDESCRIPTION\tDATE)
        for row in expenses:
            print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4])
    cur.close()
    con.close()
def update_expense():
    s
