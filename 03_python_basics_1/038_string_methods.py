"""
playing around with string methods.
- It's important to remember that strings are IMMUTABLE.
- No matter what methods we use to act on the strings, the original string remains unchanged.
"""

string_1 = "Asif Iqbal"

# for example
print(f"although, string_1.upper() is {string_1.upper()}")
print(f"string_1 is still {string_1}; because strings are immutable.")

string_2 = string_1.upper()
print(f"string_2 - {string_2}")

# does this work? It does.
# string_1 = string_1.upper()
# print(f"string_1 - {string_1}")
