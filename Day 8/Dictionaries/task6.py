# Task 6: Track a mapping of 5 students and marks. Implement algorithm 
# logic to evaluate and show the Highest and Lowest Marks.

students = {
    "Shagun": 85,
    "Aman": 92,
    "Riya": 78,
    "Karan": 95,
    "Priya": 88
}

highest_student = max(students, key=students.get)
lowest_student = min(students, key=students.get)
print("Student with the highest marks:", highest_student, "with marks:", students[highest_student])
print("Student with the lowest marks:", lowest_student, "with marks:", students[lowest_student])