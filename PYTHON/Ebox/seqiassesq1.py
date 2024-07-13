def check_subset_superset(set1, set2):
    # Convert input strings to sets
    set1 = set(set1.split(','))
    set2 = set(set2.split(','))

    # Check subset relationships
    is_subset_set1_to_set2 = set1.issubset(set2)
    is_subset_set2_to_set1 = set2.issubset(set1)

    # Check superset relationships
    is_superset_set1_to_set2 = set1.issuperset(set2)
    is_superset_set2_to_set1 = set2.issuperset(set1)

    # Format the output
    output = []
    output.append(str(is_subset_set1_to_set2))
    output.append(str(is_subset_set2_to_set1))
    output.append(str(is_superset_set1_to_set2))
    output.append(str(is_superset_set2_to_set1))

    return output

# Example usage
set1_input = "1,2,3,4,5,6"
set2_input = "1,2,3"

result = check_subset_superset(set1_input, set2_input)

# Print the results as per the specified format
print(result[0])  # set1 is a subset of set2
print(result[1])  # set2 is a subset of set1
print(result[2])  # set1 is a superset of set2
print(result[3])  # set2 is a superset of set1
