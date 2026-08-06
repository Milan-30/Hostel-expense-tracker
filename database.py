import mysql.connector as f
def get_connection():
    con=f.connect(host="localhost",user="root",password="1234",database="expense_tracker")
    return con