def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Example usage:
print(calculate_average([5, 10, 15, 20]))  # Should return 12.5
print(calculate_average([]))              # Should return 0


#Second Function

def greet_user(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Example usage:
print(greet_user("Alice"))           # Should return "Hello, Alice!"
print(greet_user("Bob", "Hi"))       # Should return "Hi, Bob!"


#Third Function

def calculate_total(*prices, discount=0):
    total = sum(prices)
    if discount:
        total -= total * (discount / 100)
    return total

# Example usage:
print(calculate_total(10, 20, 30))                    # Should return 60
print(calculate_total(10, 20, 30, discount=10))       # Should return 54


#Fourth Function

def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

# Example usage:
double = create_multiplier(2)
triple = create_multiplier(3)
print(double(5))  # Should return 10
print(triple(5))  # Should return 15