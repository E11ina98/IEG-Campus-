def sort_hyphen_separated_words(sequence):
    # Split the sequence into a list of words
    words = sequence.split('-')
    
    # Sort the list of words alphabetically
    sorted_words = sorted(words)
    
    # Join the sorted words back into a hyphen-separated string
    sorted_sequence = '-'.join(sorted_words)
    
    return sorted_sequence

# Example usage:
sample_items = "green-red-yellow-black-white"
result = sort_hyphen_separated_words(sample_items)
print("Sorted Result:", result)