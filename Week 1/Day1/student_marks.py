student1 = {
    "name": "Uday",
    "marks": [85, 90, 78],
    "total": lambda marks: sum(marks),
    "average": lambda marks: sum(marks) / len(marks),
    "grade": lambda avg: "A" if avg >= 90 else "B" if avg >= 80 else "C" if avg >= 70 else "D" if avg >= 60 else "F"
}
print(f"Student Name: {student1['name']}")
total_marks = student1["total"](student1["marks"]) 
average_marks = student1["average"](student1["marks"])
grade = student1["grade"](average_marks)
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Grade: {grade}")