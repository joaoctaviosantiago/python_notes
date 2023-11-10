# if you are having trouble understanding how this works, visualize it here:
# https://pythontutor.com/render.html#code=for%20row%20in%20range%281,%206%29%3A%0A%20%20%20%20for%20column%20in%20range%20%281,%206%29%3A%0A%20%20%20%20%20%20%20%20if%20column%20%3C%3D%20row%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22%23%22,%20end%3D''%29%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20continue%0A%0A%20%20%20%20print%28%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false

for row in range(1, 6):
    for column in range(1, 6):
        if column <= row:
            print("#", end='')
        else:
            continue

    print()
