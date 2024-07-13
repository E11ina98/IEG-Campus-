def reverse_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as input_file:
            lines = input_file.readlines()
            reversed_lines = reversed(lines)  # Reverse the lines

        with open(output_filename, 'w') as output_file:
            output_file.writelines(reversed_lines)

        print(f"Successfully reversed the content of '{input_filename}' and saved to '{output_filename}'")

    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Input and output filenames
input_filename = "input.txt"
output_filename = "output.txt"

# Call the function to reverse the file
reverse_file(input_filename, output_filename)

