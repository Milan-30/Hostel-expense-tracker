import pandas as pd
import matplotlib.pyplot as plt
from database import get_connection
def show_graphs():
    con=get_connection()
    query="select * from expenses"
    df=pd.read_sql(query,con)
    category_expense=df.groupby("CATEGORY")["AMOUNT"].sum().sort_values(ascending=False)
    category_expense.plot(kind="bar")
    plt.title("Category-Wise Expense")
    plt.xlabel("Category")
    plt.ylabel("Amount(₹)")
    plt.show()
    df["DATE"]=pd.to_datetime(df["DATE"])
    monthly_expense=df.groupby(df["DATE"].dt.to_period("M"))["AMOUNT"].sum()
    monthly_expense.plot(kind="line",marker="o")
    plt.title("Monthly-Wise Expense")
    plt.xlabel("Month")
    plt.ylabel("Amount(₹)")
    plt.show()
    con.close()
if __name__ == "__main__":
    show_graphs()