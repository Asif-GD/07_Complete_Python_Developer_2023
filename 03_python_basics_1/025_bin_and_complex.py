"""
bin() - used to retrieve the binary representation of an integer.
"""
print(bin(7))  # only works on integers
print(int("0b111", 2))

"""
complex - a datatype used to represent a complex number in Python
"""
a_complex_number = 6 + 2j  # only 'j' can be used to represent the imaginary part
print(f"complex number = {a_complex_number}")
print(f"real = {a_complex_number.real}")
print(f"imaginary = {a_complex_number.imag}")
