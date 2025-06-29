def find_second_largest(numbers):
    # Step 1: Remove duplicates if any (optional)
    unique_numbers = list(set(numbers))
    
    # Step 2: Check if we have at least 2 numbers
    if len(unique_numbers) < 2:
        return "There is no second largest number"
    
    # Step 3: Sort the numbers in descending order
    unique_numbers.sort(reverse=True)
    
    # Step 4: The second largest is at position 1 (after the largest at 0)
    return unique_numbers[1]

# Example usage
my_numbers = [5, 2, 8, 1, 9, 3, 9, 7]
result = find_second_largest(my_numbers)
print("The second largest number is:", result)  # Output: 8