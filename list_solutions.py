def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

# Example usage:
print(filter_even_numbers([1, 2, 3, 4, 5, 6]))  # Should return [2, 4, 6]
print(filter_even_numbers([1, 3, 5]))           # Should return []


# Second Function

def merge_sorted_lists(list1, list2):
    return sorted(list1 + list2)

# Example usage:
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # Should return [1, 2, 3, 4, 5, 6]
print(merge_sorted_lists([1, 2, 3], [4, 5, 6]))  # Should return [1, 2, 3, 4, 5, 6]


#Third Function

def generate_matrix(n, m):
    return [[i * j for j in range(m)] for i in range(n)]

# Example usage:
print(generate_matrix(3, 3))
# Output:
# [
#   [0, 0, 0],
#   [0, 1, 2],
#   [0, 2, 4]
# ]


#Fourth Function

def transpose_matrix(matrix):
    if not matrix or not matrix[0]:
        return []
    return [list(col) for col in zip(*matrix)]

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose_matrix(matrix))
# Output:
# [
#   [1, 4],
#   [2, 5],
#   [3, 6]
# ]
