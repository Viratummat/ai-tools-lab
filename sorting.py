def bubble_sort(values: list[int]) -> list[int]:
    """Return a sorted copy of *values* using bubble sort."""
    sorted_values = values.copy()

    for end in range(len(sorted_values) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if sorted_values[index] > sorted_values[index + 1]:
                sorted_values[index], sorted_values[index + 1] = (
                    sorted_values[index + 1],
                    sorted_values[index],
                )
                swapped = True
        if not swapped:
            break

    return sorted_values
