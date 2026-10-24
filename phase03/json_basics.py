"""Phase 03 - JSON basics: objects, arrays and Python data structures."""

import json

# Task 11 - a JSON object is equivalent to a Python dictionary.
STUDENT_JSON = """
{
    "name": "Ali",
    "marks": 85,
    "program": "BSCS"
}
"""

student = json.loads(STUDENT_JSON)
print("Task 11 - JSON object -> Python dictionary")
print(f"Python type : {type(student).__name__}")
print(f"Name        : {student['name']}")
print(f"Marks       : {student['marks']}")
print(f"Program     : {student['program']}")

# Task 12 - a JSON array is equivalent to a Python list of dictionaries.
STUDENTS_JSON = """
[
    {"id": 1, "name": "Ali"},
    {"id": 2, "name": "Sara"},
    {"id": 3, "name": "Hamza"}
]
"""

students = json.loads(STUDENTS_JSON)
print("\nTask 12 - JSON array -> Python list of dictionaries")
print(f"Python type : {type(students).__name__}")
print(f"Records     : {len(students)}")
for item in students:
    print(f"Student ID: {item['id']} | Student name: {item['name']}")
