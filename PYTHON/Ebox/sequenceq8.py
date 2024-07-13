def main():
    n = int(input("Enter total Number of sheets: "))
    attendance_sheets = []

    # Read each sheet and store it as a tuple
    for _ in range(n):
        sheet = tuple(map(int, input().split()))
        attendance_sheets.append(sheet)

    # Create a set to store unique register numbers
    unique_registers = set()

    # Process each sheet and add register numbers to the set
    for sheet in attendance_sheets:
        unique_registers.update(sheet)

    # Display the initial attendance sheets
    print("Attendance Sheets with Register Number:", attendance_sheets)

    # Display the final unique register numbers
    print("Final sheet:", tuple(sorted(unique_registers)))

if __name__ == "__main__":
    main()
