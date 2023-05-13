import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


class MysqlConnection:
    def __init__(self) :
        try:
            self.connection = mysql.connector.connect(
                host= os.getenv("DB_HOST"),
                user= os.getenv("DB_USER_NAME"),
                password= os.getenv("DB_PASSWORD"),
                database= os.getenv("DB_NAME")
            )

            if self.connection.is_connected():
                print("Connected to MySQL database.")

            # Close the cursor and connection when done
            print("Connection closed.")
            
        except mysql.connector.Error as e:
            print("Error connecting to MySQL:", e)

    def add(self, employee):
        cursor = self.connection.cursor()
        query = "INSERT INTO employees (first_name, last_name, age, department, salary) VALUES (%s, %s, %s, %s, %s)"
        values = (employee.first_name, employee.last_name, employee.age, employee.department, employee.salary)
        cursor.execute(query, values)
        self.connection.commit()
        print("Employee added successfully.")
        cursor.close()
        
    def update(self, employee):
        cursor = self.connection.cursor()
        query = "UPDATE employees SET first_name = %s, last_name = %s, age = %s, department = %s, salary = %s WHERE id = %s"
        values = (
            employee.first_name,
            employee.last_name,
            employee.age,
            employee.department,
            employee.salary,
            employee.id
        )
        cursor.execute(query, values)
        self.connection.commit()
        print("Employee updated successfully.")
        cursor.close()

    def delete(self, employee_id):
        cursor = self.connection.cursor()
        query = "DELETE FROM employees WHERE id = %s"
        values = (employee_id,)
        cursor.execute(query, values)
        self.connection.commit()
        print("Employee deleted successfully.")
        cursor.close()


