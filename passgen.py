import random

lower = "qwertyuiopasdfghjklzxcvbnm"
upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
number = "1234567890"
symbol = "@#_"

all = lower+upper+number+symbol

length = int(input("Enter a number for the password length = "))

password = "".join(random.sample(all,length))
print("Your password can be = ", password)
