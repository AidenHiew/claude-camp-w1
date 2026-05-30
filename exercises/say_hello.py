#Say Hello
print("Hello")

#Say Hello to User

#input user name
name = input("what is your name?")

name = name.strip()
name = name.capitalize()
name = name.title()


#print name
print("Hello, ", end="")

print(name)

print(f"Good Morning, {name}", sep="")

