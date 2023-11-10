
phrase = input("Type a phrase:\n")
# turn input into a list split by spaces and append word if len of word <= 3
small_words = [word for word in phrase.split(' ') if len(word) <= 3]
print(small_words)
