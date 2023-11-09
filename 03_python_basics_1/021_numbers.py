# exploring integer and float datatype and basic arithmatic.

# variable
variable_1: int = 11
variable_2: int = 2

# addition
total = variable_1 + variable_2
print("total 1 & 2 =", total)
print("total:", type(total), "\n")

# difference
difference = variable_1 - variable_2
print("difference 1 & 2 =", difference)
print("difference:", type(difference), "\n")

# product
product = variable_1 * variable_2
print("product 1 & 2 =", product)
print("product:", type(product), "\n")

# division
division = variable_1 / variable_2
print("divide 1 by 2 =", division)
print("divide:", type(division), "\n")

# power of
power_of = variable_1 ** variable_2
print("1 to the power of 2 =", power_of)
print("power_of:", type(power_of), "\n")

# floor division - an interesting one
# floor division divides and then returns the integer value rounded down, for e.g. 4 // 3 = 1 and not 1.33
floor_division = variable_1 // variable_2
print("floor_division 1 by 2 =", floor_division)
print("floor_division:", type(floor_division), "\n")

# modulo operator - returns the remainder of a division
modulo_of = variable_1 % variable_2
print("modulo_of 1 by 2 =", modulo_of)
print("modulo_of:", type(modulo_of), "\n")
