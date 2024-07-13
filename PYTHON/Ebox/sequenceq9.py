def find_second_highest_mark(n, records, student_name):
    # Initialize a dictionary to store student records
    student_records = {}

    # Read each student record and store it in the dictionary
    for record in records:
        parts = record.split()
        name = parts[0]
        marks = list(map(int, parts[1:]))
        student_records[name] = marks
    
    # Retrieve marks of the specified student
    if student_name in student_records:
        marks = student_records[student_name]
        
        # Find the second highest mark
        unique_marks = list(set(marks))
        unique_marks.sort(reverse=True)
        
        if len(unique_marks) >= 2:
            second_highest = unique_marks[1]
            print(f"Second Highest mark of {student_name}: {second_highest}")
        else:
            print(f"{student_name} scored same marks in all subjects: {marks[0]:.0f}") 
    else:
        print("Student doesn't exist")

# Main function to handle input and output
def main():
    # Read number of students
    n = int(input().strip())
    
    # Read each student record
    records = []
    for _ in range(n):
        records.append(input().strip())
    
    # Read the student name to find the second-highest mark
    student_name = input().strip()
    
    # Find and print the second-highest mark
    find_second_highest_mark(n, records, student_name)

# Run the main function
if __name__ == "__main__":
    main()
