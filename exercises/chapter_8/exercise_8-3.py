
votes = {"pizza": 0, "sushi": 0}

for user in range(1, 11):
    # using a while loop so that if something other than pizza or sushi is typed, it will ask for a valid answer
    # if answer is correct, break the loop
    while True:
        answer = input("What do you prefer, pizza or sushi?\n").lower()

        if answer == "pizza":
            votes["pizza"] += 1
            break
        elif answer == "sushi":
            votes["sushi"] += 1
            break
        else:
            print('Not a valid answer. Type "pizza" or "sushi".')

winner = ''
winner_votes = 0

for key, value in votes.items():
    if value > winner_votes:
        winner = key
        winner_votes = value

print(f"Winner: {winner.title()}")
print(f"Votes: {winner_votes}/10")
