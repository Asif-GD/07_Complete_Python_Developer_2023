"""
variable - best practices

1. snake_cases
2. must start with a lower case or underscores but NOT numbers
3. composed on letters, numbers, and/or underscores
4. DO NOT overwrite keywords
5. they are case-sensitive
"""

# a variable starting with an _ is reserved as the best practise for creating private variables in classes
_user_iq = 170
print(f"_user_iq = {_user_iq}")

# a variable starting with __ (double underscores) is reserved the best practise creating dunder variables.
__user = "Asif"
print(f"__user = {__user}")

# a shorthand form
variable_1, variable_2, variable_3 = 1, 2, 3
print(f"variable_1 = {variable_1}")
print(f"variable_2 = {variable_2}")
print(f"variable_3 = {variable_3}")

"""
expression vs. statement
expression - any calculation that evaluates to a value
statement - a line of code
"""
# this line below is a statement.
variable_4 = variable_1 + variable_2 + variable_3  #  the code after the assignment operator = is an expression.
print(f"variable_4 = {variable_4}")
