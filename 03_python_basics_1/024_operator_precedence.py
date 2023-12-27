"""
PEMDAS - Parenthesis, Exponent, Multiplication / Division, Addition / Subtraction
()
**
* /
+ -
"""
print((10 - 4) + 2 ** 2)

# exercise

print((5 + 4) * 10 / 2)  # 45.0

print(((5 + 4) * 10) / 2)  # 45.0

print((5 + 4) * (10 / 2))  # 45.0

print(5 + (4 * 10) / 2)  # 25.0

print(5 + 4 * 10 // 2)  # 25
