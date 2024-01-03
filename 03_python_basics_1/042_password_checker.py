"""
A script to check the size of user's password
"""

username = input("Your username please? ")
user_password = input("Please enter your password: ")

length_user_password = len(user_password)
hide_password = "*" * length_user_password

print(f"Hi {username}; your password {hide_password} is {length_user_password} characters long.")
