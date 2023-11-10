
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

sum_age = 0

for age in people.values():
    sum_age += age

avg = sum_age / len(people)

print("%.2f" % avg)
