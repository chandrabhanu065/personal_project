def count_duplicates(arr):
    # Create an empty dictionary to store the frequency of each element
    element_frequency = {}

    # Count the frequency of each element in the array
    for element in arr:
        if element in element_frequency:
            element_frequency[element] += 1
        else:
            element_frequency[element] = 1

    # Count the number of elements with frequency greater than 1 (duplicates)
    #duplicate_count = sum(1 for frequency in element_frequency.values() if frequency > 1)

    #return duplicate_count
    return element_frequency

# Example usage:
array = [1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 7, 8]

duplicate_count = count_duplicates(array)

print(f"Number of duplicate elements in the array: {duplicate_count}")
