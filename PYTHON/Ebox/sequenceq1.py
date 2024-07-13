def delete_character(string, index):
  
    if index < 0 or index >= len(string):
        return "Index is out of range."
    # Use slicing to remove the character at the specified index
    return string[:index] + string[index + 1:]

# Input: string and integer index
string = input().strip()
index = int(input().strip())

    # Adjust index to be zero-based
adjusted_index = index - 1

    # Output: string with the character deleted at the specified index
result = delete_character(string, adjusted_index)
print(result)