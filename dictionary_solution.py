def invert_dictionary(d):
    return {v: k for k, v in d.items()}

# Example usage:
print(invert_dictionary({"a": 1, "b": 2, "c": 3}))  # Should return {1: "a", 2: "b", 3: "c"}


# Second Function

def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()  # Start with a copy of dict1 to avoid modifying it
    merged.update(dict2)   # Update the copy with items from dict2
    return merged

# Example usage:
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(merge_dictionaries(dict1, dict2))  # Should return {"a": 1, "b": 3, "c": 4}


#Third Function

from collections import defaultdict

def word_frequencies(text):
    words = text.split()
    frequency = defaultdict(int)
    for word in words:
        frequency[word] += 1
    return dict(frequency)

# Example usage:
text = "the quick brown fox jumps over the lazy dog"
print(word_frequencies(text))
# Should return {"the": 2, "quick": 1, "brown": 1, "fox": 1, "jumps": 1, "over": 1, "lazy": 1, "dog": 1}


#Fourth Function

def add_contact(contacts, name, **details):
    if name not in contacts:
        contacts[name] = {}
    contacts[name].update(details)

# Example usage:
contacts = {}
add_contact(contacts, "Alice", phone="123-456-7890", email="alice@example.com")
add_contact(contacts, "Bob", phone="987-654-3210")
add_contact(contacts, "Alice", address="123 Main St")  # Updates Alice's info

print(contacts)
# Should return:
# {
#   "Alice": {"phone": "123-456-7890", "email": "alice@example.com", "address": "123 Main St"},
#   "Bob": {"phone": "987-654-3210"}
# }

