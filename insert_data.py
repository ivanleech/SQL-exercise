import pandas as pd
import mysql.connector
from mysql.connector import Error

# Database config
host = "localhost"
database = "manu"
user = "root"
password = "super secret password"


def import_data(df, table_name):
    try:
        connection = mysql.connector.connect(
            host=host, database=database, user=user, password=password
        )
        if connection.is_connected():
            cursor = connection.cursor()

            for _, row in df.iterrows():
                sql = f"INSERT INTO {table_name} VALUES ({','.join(['%s']*len(row))})"
                cursor.execute(sql, tuple(row))
            connection.commit()
    except Error as e:
        print(f"Error importing data: {e}")
    finally:
        # Close connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


if __name__ == "__main__":
    # Import employee data to DB
    data = {
        "ID": [1, 2, 3, 4, 5, 6, 7],
        "Name": ["Joe", "Henry", "Sam", "Max", "Janet", "Randy", "Will"],
        "Salary": [85000, 80000, 60000, 90000, 69000, 85000, 70000],
        "DepartmentId": [1, 2, 2, 1, 1, 1, 1],
    }
    employee_df = pd.DataFrame(data)
    table_name = "employee"
    import_data(employee_df, table_name)

    # Import department data to DB
    data = {
        "ID": [1, 2],
        "Name": ["IT", "Sales"],
    }
    department_df = pd.DataFrame(data)
    table_name = "department"
    import_data(department_df, table_name)

    # Import stock data to DB
    data = {
        "id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "stock_name": ["Bottles", "Corona masks", "Bottles", "Handbags", "Corona masks", "Corona masks", "Corona masks", "Corona masks", "Handbags", "Corona masks"],
        "operation": ["buy", "buy", "sell", "buy", "sell", "buy", "sell", "buy", "sell", "sell"],
        "operation_day": [1, 2, 5, 17, 3, 4, 5, 6, 29, 10],
        "price": [1000, 10, 9000, 30000, 1010, 1000, 500, 1000, 7000, 10000],
    }
    stock_df = pd.DataFrame(data)
    table_name = "stock"
    import_data(stock_df, table_name)

    # import salesman, customer, and orders data to DB
    salesman_data = {
        'salesman_id': [5001, 5002, 5005, 5006, 5007, 5003],
        'name': ['James Hoog', 'Nail Knite', 'Pit Alex', 'Mc Lyon', 'Paul Adam', 'Lauson Hen'],
        'city': ['New York', 'Paris', 'London', 'Paris', 'Rome', 'San Jose'],
        'commission': [0.15, 0.13, 0.11, 0.14, 0.13, 0.12]
    }

    customer_data = {
        'customer_id': [3002, 3007, 3005, 3008, 3004, 3009, 3003],
        'cust_name': ['Nick Rimando', 'Brad Davis', 'Graham Zusi', 'Julian Green', 'Fabian Johnson', 'Geoff Cameron', 'Jozy Altidor'],
        'city': ['New York', 'New York', 'California', 'London', 'Paris', 'Berlin', 'Moscow'],
        'grade': [100, 200, 200, 300, 300, 100, 200],
        'salesman_id': [5001, 5001, 5002, 5002, 5006, 5003, 5007]
    }

    orders_data = {
        'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008],
        'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760],
        'ord_date': ['2012-10-05', '2012-09-10', '2012-10-05', '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10'],
        'customer_id': [3005, 3001, 3002, 3009, 3005, 3007, 3002],
        'salesman_id': [5002, 5005, 5001, 5003, 5002, 5001, 5001]
    }

    salesman_df = pd.DataFrame(salesman_data)
    customer_df = pd.DataFrame(customer_data)
    orders_df = pd.DataFrame(orders_data)
    import_data(salesman_df, 'salesman')
    import_data(customer_df, 'customer')
    import_data(orders_df, 'orders')
