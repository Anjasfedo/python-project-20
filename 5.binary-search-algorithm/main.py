# Binary Search Function
def binarySearch(myList, element):
    # Initialize variables
    middle = 0
    start = 0
    end = len(myList) - 1
    steps = 0

    # Iterate while the search range is valid
    while start <= end:
        # Display the current search range
        print(f"Steps {steps}: {str(myList[start:end+1])}")

        # Update step count and calculate middle index
        steps += 1
        middle = (start + end) // 2

        # Check if the element is found
        if element == myList[middle]:
            return middle
        # If the element is less than the middle, update the end
        elif element < myList[middle]:
            end = middle - 1
        # If the element is greater than the middle, update the start
        elif element > myList[middle]:
            start = middle + 1

    # If the element is not found
    print("Element not found")
    return -1

# Example Usage
result = binarySearch(myList=[1,2,3,4,5,6,7,8,9,10], element=6)
print(f"Element found at index: {result}")
