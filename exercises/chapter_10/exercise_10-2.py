
names1 = ['Rachel', 'Augusto', "Giorgio"]
names2 = ['Pedro', 'Conan', 'Rachel',]
names3 = ['Conan', 'Giorgio', 'Rodrigo']

# type casting all the lists to sets
names1, names2, names3 = set(names1), set(names2), set(names3)

all_names = names1.union(names2, names3)

print(all_names)

