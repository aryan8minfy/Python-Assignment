def swap_pairs(t):
    swapped = []
    i = 0
    while i < len(t) - 1:
        swapped.extend([t[i + 1], t[i]])
        i += 2
    if len(t) % 2 != 0:
        swapped.append(t[-1])
    return tuple(swapped)

# Example usage:
print(swap_pairs((1, 2, 3, 4)))  # Should return (2, 1, 4, 3)
print(swap_pairs((1, 2, 3)))     # Should return (2, 1, 3)


#Second Function

def get_stats(numbers):
    if not numbers:
        return (None, None, 0, 0.0)
    min_num = min(numbers)
    max_num = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)
    return (min_num, max_num, total, average)

# Example usage:
print(get_stats([1, 2, 3, 4, 5]))  # Should return (1, 5, 15, 3.0)


#third function

from collections import namedtuple

# Define the Student named tuple
Student = namedtuple('Student', ['name', 'age', 'grades'])

def top_student(students):
    return max(students, key=lambda student: sum(student.grades) / len(student.grades))

# Example usage:
alice = Student("Alice", 20, (85, 90, 95))
bob = Student("Bob", 19, (70, 80, 90))
charlie = Student("Charlie", 21, (90, 92, 93))

print(top_student([alice, bob, charlie]))  # Should return the charlie Student tuple


#fourth function

from collections import defaultdict

def count_coordinate_occurrences(coords):
    occurrences = defaultdict(int)
    for coord in coords:
        occurrences[coord] += 1
    return dict(occurrences)

# Example usage:
coords = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4), (1, 2)]
print(count_coordinate_occurrences(coords))  # Should return {(1, 2): 3, (3, 4): 2, (5, 6): 1}
