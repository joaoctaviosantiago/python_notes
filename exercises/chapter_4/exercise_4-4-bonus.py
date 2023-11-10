
for row in range(1, 6):
    for column in range(1, 6):
        if column >= (6 - row):
            print("#", end="")
        else:
            print(" ", end="")

    print()
