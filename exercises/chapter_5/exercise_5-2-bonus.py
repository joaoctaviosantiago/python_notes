
numbers = [191, 78, 67, 195, 51, 154, 28, 45, 186, 106]

largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number
    elif number < smallest:
        smallest = number

print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")
