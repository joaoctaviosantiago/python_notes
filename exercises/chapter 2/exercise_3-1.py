
score1 = float(input("Exam 1:\n"))
score2 = float(input("Exam 2:\n"))
score3 = float(input("Exam 3:\n"))
# I'm using parenthesis so that the numbers are summed before dividing.
avg = (score1 + score2 + score3) / 3

print(f"Average: {'%.2f' % avg}")

if avg >= 6:
    print("You've passed! (:")
# elif avg between 4 and 6
elif 4 > avg > 6:
    print("You have summer school")
else:
    print("You've failed.")
