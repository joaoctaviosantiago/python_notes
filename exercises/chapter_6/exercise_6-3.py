
# get input, make it all lower case and remove spaces
phrase = input("Type a word:\n").lower().replace(" ", "")
# make a new variable that contains the reversed input
phrase_reversed = phrase[::-1]

# if they're the same, they're a palindrome
if phrase == phrase_reversed:
    print("Palindrome")
else:
    print("Not palindrome")
