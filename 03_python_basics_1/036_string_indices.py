"""
string[start:stop:step over]
"""

string_1 = "0123456789"
#           0123456789

print(f"string_1[0:2]= {string_1[0:2]}")
print(f"string_1[0:2:]= {string_1[0:2:]}")

# using step over
print(f"string_1[0:2:2]= {string_1[0:2:2]}")
# what happens when I step over more characters than total characters?
print(f"string_1[0:2:4]= {string_1[0:2:4]}")

# using negative index
print(f"string_1[-1]= {string_1[-1]}")
print(f"string_1[-2]= {string_1[-2]}")

# using negative step over
# reversing an iterable
print(f"string_1[::-1]= {string_1[::-1]}")
# I tried the below code using -1 to -11 & and every time it results to an empty string
print(f"string_1[0:2:-1]= {string_1[0:2:-1]}")
# however, the one below works. Why?
print(f"string_1[:2:-1]= {string_1[:2:-1]}")
