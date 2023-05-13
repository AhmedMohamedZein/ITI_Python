from database import MysqlConnection

class Employee:
    employees = [] # works like static list 
    def __init__ (self , first_name , last_name , age , department , salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary
        Employee.employees.append(self)
        mysql.add(self)
        # insert a new record in the database

    def transfer(self, department):
        self.department = department
        mysql.update(self)
        return self
        # Update the database

    @classmethod
    def fire (cls , employee):
        cls.employees.remove(employee)
        # delete from database
        mysql.delete(employee)
        Employee.list_employees()
    
    @classmethod
    def list_employees(cls):
        for employee in cls.employees:
            print(f"first_name: {employee.first_name}", end="  ")
            print(f"last_name: {employee.last_name}", end="  ")
            print(f"age: {employee.age}", end="  ")
            print(f"department: {employee.department}", end="  ")
            print(f"salary: {employee.salary}")
        

class Manager(Employee):
    def __init__(self, first_name, last_name, age, department, salary, managed_department):
        super().__init__(first_name, last_name, age, department, salary)
        self.managed_department = managed_department

    def show(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print("Salary: Confidential")

    @staticmethod
    def get_input():
        return input("Please insert data:\nName: "), input("Age: "), input("Department: "), input("Salary: ")


# Example usage
while True:
    print("Menu:")
    print("1. Add new employee (e)")
    print("2. Add new manager (m)")
    print("3. Quit (q)")

    choice = input("Enter your choice: ")

    if choice == "e":
        name, age, department, salary = Employee.get_input()
        employee = Employee(name, age, department, salary)
        print("Employee added successfully.")
        Employee.list_employees()

    elif choice == "m":
        name, age, department, salary = Manager.get_input()
        managed_department = input("Managed Department: ")
        manager = Manager(name, age, department, salary, managed_department)
        print("Manager added successfully.")
        manager.show()

    elif choice == "q":
        print("Exiting the program...")
        break

    else:
        print("Invalid choice. Please try again.")


mysql = MysqlConnection()
e1 = Employee('Ahmed', 'Zein' , 23 , 'SBG' , 12000)
