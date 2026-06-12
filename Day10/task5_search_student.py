students = [
    {"name":"aksha", "marks": 80},
    {"name":"aaysha","marks":70},
    {"name":"shana","marks":85}
]
search_name = input("Enter studen name serch:")
found = False

for student in students:
    # We use .lower() to make the search case-insensitive
    if student["Name"].lower() == search_name.lower():
        print("Student Found")
        print(f"Marks: {student['Marks']}")
        found = True
        break # Exit loop once found

if not found:
    print("Student Not Found")