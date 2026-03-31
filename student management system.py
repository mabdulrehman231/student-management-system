
class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name):
        super().__init__(name)  # call parent constructor
        self.marks = {"English": 0, "Urdu": 0, "Math": 0}

    def add_marks(self):
        for subject in self.marks:
            while True:
                try:
                    m = int(input(f"Enter marks for {subject} (0-100): "))
                    if 0 <= m <= 100:
                        self.marks[subject] = m
                        break
                    else:
                        print("Marks must be 0-100")
                except:
                    print("Invalid input!")

    def average(self):
        return sum(self.marks.values()) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "Fail"

    def show(self):
        print(f"\nName: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.average():.2f}")
        print(f"Grade: {self.grade()}")



students = []

while True:
    print("\n1. Add Student")
    print("2. Show All Students")
    print("3. Exit")

    choice = input("Enter choice: ")
    if choice == "1":
        name = input("Enter name: ")
        s = Student(name)
        s.add_marks()
        students.append(s)
        print(f"{name} added successfully!")
    elif choice == "2":
        if not students:
            print("No students yet.")
        for s in students:
            s.show()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
