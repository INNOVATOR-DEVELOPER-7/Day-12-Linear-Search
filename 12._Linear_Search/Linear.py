def linear_search(array, target):
    # Traverse through all elements in the array
    for i in range(len(array)):
        # If the current element is the target, return its index
        if array[i] == target:
            return i
    # If the target is not present in the array
    return -1

# Get list of numbers from the user
user_input = input("Enter numbers separated by space: ")
array = list(map(int, user_input.split()))

# Get the target number to search for from the user
target = int(input("Enter the target number to search for: "))

# Perform linear search
result = linear_search(array, target)

# Print the result
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found in array")
