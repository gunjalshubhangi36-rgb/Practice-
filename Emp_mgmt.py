# 3. Create a simple Employee Management System using Class and Object in Python.
# What to Do
# 1. Create a class named Employee.
# 2. Create a constructor __init__() to initialize:
# o Employee name
# o Employee ID
# o Department
# o Basic salary
# 3. Create a display_details() method to display employee information.
# 4. Create a calculate_salary() method:
# o Add a fixed bonus of ₹5,000.
# o Calculate and display the final salary.
# 5. Create a check_salary() method:
# o If salary is ₹30,000 or above, display "Good Salary".
# o Otherwise, display "Average Salary".
# 6. Create a menu-driven program:
# o 1 → Display Details
# o 2 → Calculate Salary
# o 3 → Check Salary
# o 4 → Exit




class Employee:
    def __init__(self, emp_name, emp_id, dept, salary):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.dept = dept
        self.salary = salary

    def display(self):
        print("\nName of Employee:", self.emp_name)
        print("Id of Employee:", self.emp_id)
        print("Department:", self.dept)
        print("Salary:", self.salary)

    def calculate_salary(self):
        bonus = 5000
        final_salary = bonus + self.salary

        print("\nSalary Details:")
        print("Basic Salary:", self.salary)
        print("Bonus:", bonus)
        print("Final Salary:", final_salary)

    def check_salary(self):
        if self.salary >= 30000:
            print("Good Salary")
        else:
            print("Average Salary")


emp_name = input("Enter Name: ")
emp_id = input("Enter Id: ")
dept = input("Enter Department: ")
salary = int(input("Enter Salary: "))

obj = Employee(emp_name, emp_id, dept, salary)

while True:

    print("\n  Employee Management System ")
    print("1. Display Details")
    print("2. Calculate Salary")
    print("3. Check Salary")
    print("4. Exit")

    choice = input("Enter your choice: ")

    match choice:

        case "1":
            obj.display()

        case "2":
            obj.calculate_salary()

        case "3":
            obj.check_salary()

        case "4":
            print("Thank you")
            break

       