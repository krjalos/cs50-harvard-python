#Ask user for their name, strip and title
name = input("What's your name? ").strip().title()

#Remove whitespace from string
# name = name.strip()

#Capitalize title() & strip whitespace
# name = name.strip().title()


#Split user's name into first and last names

firstname, lastname = name.split(" ")

#Say hello to user
# print("Hello, " + name)
# print("Hello,", name, sep=" - ", end="\n\n")
# print("Hello,", name)

print(f"Hello, {firstname}")
