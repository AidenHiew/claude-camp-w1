#Simple password generator
#User to enter the length of the password
#then this program will generate a random password of that length

import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))    
    return password

# Get length from user and generate password
print("Suggest the length to be more than 8 characters for better security.")
length = int(input("Enter the Length of the Password you want to generate: "))

password = generate_password(length)

print()
print(f"Your generated password is: \033[1m{password}\033[0m")


print()
print ("a long and strong password is important for security, so make sure to use a unique password for each of your account !")
print("Thank you for using the simple password generator!")