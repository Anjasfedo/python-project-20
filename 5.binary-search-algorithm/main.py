def binarySearch(myList, element):
    middle = 0
    start = 0
    end = len(myList) - 1
    steps = 0
    
    while start <= end:
        print(f"Steps {steps}: {str(myList[start:end+1])}")

        steps += 1
        middle = (start + end) // 2

        if element == myList[middle]:
            return middle
        elif element < myList[middle]:
            end = middle - 1
        elif element > myList[middle]:
            start = middle + 1
            
    print("Element not found")
    return -1
        
result = binarySearch(myList=[1,2,3,4,5,6,7,8,9,10], element=6)
print(f"Element found at index: {result}")
