
text = input("type a word:\n")
# getting the index of the element in the middle of the string, converting it to int and dividing it
text_half_index = int((len(text)) / 2)
# accessing the text from the beginning to the middle index but not included and making it uppercase
# concatenating the second half up to the end in lowercase
temp_text = text[:text_half_index].upper() + text[text_half_index:].lower()

print(temp_text)
