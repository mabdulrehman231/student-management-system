class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.__marks = {"English": 0, "Urdu": 0, "Math": 0}

    def add_marks(self):
        for subject in self.__marks:
            while True:
                try:
                    marks = int(input(f"Enter marks for {subject} (0-100): "))
                    if 0 <= marks <= 100:
                        self.__marks[subject] = marks
                        break
                    else:
                        print("Marks must be between 0 and 100")
                except ValueError:
                    print("Invalid input!")

    # private method
    def __average(self):
        return sum(self.__marks.values()) / len(self.__marks)

    def grade(self):
        avg = self.__average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "Fail"

    def show(self):
        print("\n--- Student Info ---")
        print(f"Name: {self.name}")
        print("Marks:")

        for subject, marks in self.__marks.items():
            print(f"  {subject}: {marks}")

        print(f"Average: {self.__average():.2f}")
        print(f"Grade: {self.grade()}")


students = []

while True:
    print("\n1. Add Student")
    print("2. Show All Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        student = Student(name)
        student.add_marks()
        students.append(student)
        print(f"{name} added successfully!")

    elif choice == "2":
        if not students:
            print("No students yet.")
        for student in students:
            student.show()

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
