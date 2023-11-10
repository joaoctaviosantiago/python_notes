

name = input("Type your name:\n")
birth_year = int(input("Type the year you were born:\n"))

# instead of making a variable, I'm calculating the age within the f string.
print(f"Hi, {name}. This year you are or will be {2023 - birth_year}.")
