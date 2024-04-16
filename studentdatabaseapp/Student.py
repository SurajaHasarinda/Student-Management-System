class Student:
    id = 1000
    cost_of_course = 600

    def __init__(self):
        self.first_name = input("Enter Student first name: ")
        self.last_name = input("Enter Student last name: ")
        self.grade_year = self.get_grade_year()
        self.set_student_id()
        self.courses = []
        self.tuition_balance = 0

    def get_grade_year(self):
        while True:
            try:
                grade_year = int(input("Enter Student class level (1-4): "))
                if 1 <= grade_year <= 4:
                    return grade_year
                else:
                    print("Error: Grade level must be between 1 and 4.")
            except ValueError:
                print("Error: Please enter a valid integer.")

    def set_student_id(self):
        Student.id += 1
        self.student_id = str(self.grade_year) + str(Student.id)

    def enroll(self):
        while True:
            course = input("Enter course to enroll (Q to quit): ")
            if course.lower() != "q":
                self.courses.append(course)
                self.tuition_balance += Student.cost_of_course
            else:
                break

    def view_balance(self):
        print("Your balance is: $", self.tuition_balance)

    def pay_tuition(self):
        self.view_balance()
        while True:
            try:
                payment = int(input("Enter your payment: $"))
                if payment < 0:
                    print("Error: Payment amount cannot be negative.")
                elif payment > self.tuition_balance:
                    print("Error: Payment amount exceeds tuition balance.")
                else:
                    self.tuition_balance -= payment
                    print("Thank you for your payment of $", payment)
                    break
            except ValueError:
                print("Error: Please enter a valid integer.")

    def show_info(self):
        return f"Name: {self.first_name} {self.last_name}\nGrade Level: {self.grade_year}\nCourses Enrolled: {', '.join(self.courses)}\nBalance: ${self.tuition_balance}"
