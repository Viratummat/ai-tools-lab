"""
Binary search implementation in Python.
"""

def binary_search(arr, target):
    """
    Find target in sorted array using binary search.
    
    Args:
        arr (list): Sorted list of numbers
        target: Value to find
    
    Returns:
        int: Index of target, or -1 if not found
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


# Test it
if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
    print(f"Searching for 7: {binary_search(numbers, 7)}")      # Should print 3
    print(f"Searching for 1: {binary_search(numbers, 1)}")      # Should print 0
    print(f"Searching for 19: {binary_search(numbers, 19)}")    # Should print 9
    print(f"Searching for 10: {binary_search(numbers, 10)}")    # Should print -1