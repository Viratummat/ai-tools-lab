def find_max(numbers):
    """Find the maximum number in a list."""
    max_val = float('-inf')
    for i in range(len(numbers)):
        if numbers[i] > max_val:
            max_val = numbers[i]
    return max_val

def reverse_string(s):
    """Reverse a string."""
    result = ""
    for i in range(len(s) - 1, -1, -1):
        result += s[i]
    return result

result1 = find_max([5, 15, 3, 8])
print(f"Max is: {result1}")

result2 = reverse_string("hello")
print(f"Reversed: {result2}")