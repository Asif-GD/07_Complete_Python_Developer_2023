"""
A program to calculate the user's age
"""
import datetime
from datetime import date

user_year_of_birth = int(input("What is your year of birth? "))
current_year = date.today().year
# print(current_year)

user_age = current_year - user_year_of_birth
print(f"You are {user_age} years old.")
