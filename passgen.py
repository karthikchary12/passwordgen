import random

lower = "qwertyuiopasdfghjklzxcvbnm"
upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
number = "1234567890"
symbol = "!@#$%^&*()_+="

all = lower+upper+number+symbol

just_pass = lower+upper+number

length = int(input("Enter a number for the password length = "))

print("Do you want to include symbols in your password ")
answer = input("Enter Yes/No = ")

if 'Yes':
    password = "".join(random.sample(all,length))

elif 'No':
    password = "".join(random.sample(just_pass,length))

print("Your password can be = ", password)


    