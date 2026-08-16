class student:
    def __init__(self, std_name, roll_no, age, marks1, marks2, marks3):
        self.std_name = std_name
        self.roll_no = roll_no
        self.age = age
        self.marks = [marks1, marks2, marks3]

    def display_details(self):
        print("\nName of Student:", self.std_name)
        print("Roll number of student:", self.roll_no)
        print("Age of student:", self.age)
        print("Marks of student:", self.marks)

    def calculate_total(self):
        return sum(self.marks)

    def calculate_percentage(self):
        total = self.calculate_total()
        return total / 3

    def check_result(self):
        for mark in self.marks:
            if mark < 35:
                return "FAIL"
        return "PASS"

    def update_marks(self, subject, newmarks):
        if subject == 1:
            self.marks[0] = newmarks
        elif subject == 2:
            self.marks[1] = newmarks
        elif subject == 3:
            self.marks[2] = newmarks   
        else:
            print("Invalid subject number")


std_name = input("Enter student name: ")
roll_no = int(input("Enter roll number: "))
age = int(input("Enter age: "))
marks1 = int(input("Enter marks of subject 1: "))
marks2 = int(input("Enter marks of subject 2: "))
marks3 = int(input("Enter marks of subject 3: "))

obj = student(std_name, roll_no, age, marks1, marks2, marks3)


while True:
    print(" MENU ")
    print("1. Display Details")
    print("2. Calculate Total")
    print("3. Calculate Percentage")
    print("4. Check Result")
    print("5. Update Marks")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            obj.display_details()

        case 2:
            print("Total Marks:", obj.calculate_total())

        case 3:
            print("Percentage:", obj.calculate_percentage(), "%")

        case 4:
            print("Result:", obj.check_result())

        case 5:
            subject = int(input("Enter subject number (1-3): "))
            newmarks = int(input("Enter new marks: "))
            obj.update_marks(subject, newmarks)
            print("Updated student marks:", obj.marks)

        case 6:
            print("Exit program")
            break





