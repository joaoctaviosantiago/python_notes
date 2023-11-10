
people = {
    'James': 30,
    'Mary': 23,
    'Robert': 83,
    'Patricia': 42,
    'John': 19,
    'Jennifer': 27,
    'Michael': 36,
    'Linda': 65,
    'David': 76
}

name = ''
age = 0

for key, value in people.items():
    if value > age:
        age = value
        name = key

print(name, age)
