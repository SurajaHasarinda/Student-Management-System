from studentdatabaseapp.Student import Student

class StudentDatabaseApp:
    @staticmethod
    def main():
        try:
            num_of_students = int(input("Enter number of students to enroll: "))
            students = [Student() for _ in range(num_of_students)]
            for student in students:
                student.enroll()
                student.pay_tuition()
                print(student.show_info())
        except ValueError:
            print("Error: Please enter a valid number for the number of students.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    StudentDatabaseApp.main()
