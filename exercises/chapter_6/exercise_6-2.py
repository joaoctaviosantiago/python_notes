
words = input("Type a phrase:\n")
# splitting string into list
words = words.split(' ')
# reversing string (get the entire string but in negative steps - from end to the beginning)
words = words[::-1]
# turning list into string separating items by space
words = ' '.join(words)

print(words)