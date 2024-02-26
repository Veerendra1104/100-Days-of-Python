import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','w','x','y','z'
           ,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

symbols = ['!','@','#','$','%','^','&','*','(',')','-']
numbers =['0','1','2','3','4','5','6','7','8','9']
print("Wel come to the password genarator !!")
ns_letters = int(input("Enter the number of leetters you Like "))
ns_symbol = int(input("Enter the number of symbols"))
ns_numbers = int(input("Enter the number of numbers "))

password_list = []

for char in range(1,ns_letters+1):
    password_list.append(random.choice(letters))

for char in range(1 , ns_symbol+1):
    password_list.append(random.choice(symbols))

for char in range(1,ns_numbers+1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""

for char in password_list:
    password += char

print(f"Your Password is {password}")