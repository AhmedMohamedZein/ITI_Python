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
        



mysql = MysqlConnection()
e1 = Employee('Ahmed', 'Zein' , 23 , 'SBG' , 12000)
