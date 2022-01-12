"""Test Bank Account exercise"""

expected_user: str = "Milu"
expected_pwd: str = "1996"
expected_sold: int = 100

# implement the first-case
usr = input("Please enter a valid username : ")
assert usr == expected_user
# print(type(expected_sold))

# implement the second-case
pwd = input("Please enter a valid password : ")
assert pwd == expected_pwd

"""
input("Please enter to log in !")
print(f"Login successful! Your sold is : {expected_sold}")

cashback = int(input("Please enter the amount you want to retrieve : "))
print(f"You have {expected_sold - cashback} euro left in your account ")
"""
