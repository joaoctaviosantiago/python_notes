
numbers = [6, 2, 5, 6, 2, 7, 1, 9, 1, 7, 6, 4, 2, 6]
most_repeated_number = 0
count = 0

for number in numbers:
    # checks if the amount of times a number appears in the list is higher than the value of count
    if numbers.count(number) > 0:
        count = numbers.count(number)
        most_repeated_number = number

print(f"Most common number: {most_repeated_number}")
print(f"Occurs {count} times")