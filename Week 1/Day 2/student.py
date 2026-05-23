class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")
    def grade(self):
        return "A" if self.marks>=90 else "B" if self.marks>=80 else "C" if self.marks>=70 else "D" if self.marks>=60 else "F"

s1 = Student("Alice", 95)
s2 = Student("Bob", 85)
s1.display()
print(f"Grade: {s1.grade()}")
s2.display()
print(f"Grade: {s2.grade()}")