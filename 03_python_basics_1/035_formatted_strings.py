"""
formatted strings or simply f-strings
"""

string_1 = "Asif Iqbal"
string_2 = 32

print(f"Hi {string_1}; you are {string_2} years old.")  # python 3's way

# python 2's way
print("Hi {}; you are {} years old.".format("Ram", 31))
print("Hi {1}; you are {0} years old.".format(31, "Ram"))
print("Hi {name}; you are {age} years old.".format(name="Ram", age=31))
