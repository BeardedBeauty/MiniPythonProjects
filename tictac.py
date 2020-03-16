q = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]


def gametictic():
    game = True
    w = "O"
    while game:
        print("Please enter a number to place on board")
        e = int(raw_input())
        if e >= 9:
            w = ticplacement([2, 2, w])
        elif e <= 1:
            w = ticplacement([0, 0, w])
        elif e == 2:
            w = ticplacement([0, 1, w])
        elif e == 3:
            w = ticplacement([0, 2, w])
        elif e == 4:
            w = ticplacement([1, 0, w])
        elif e == 5:
            w = ticplacement([1, 1, w])
        elif e == 6:
            w = ticplacement([1, 2, w])
        elif e == 7:
            w = ticplacement([2, 0, w])
        elif e == 8:
            w = ticplacement([2, 1, w])
        else:
            game = False

        print(q[0])
        print(q[1])
        print(q[2])


def ticplacement(r):
    w = r[2]
    if q[r[0]][r[1]] == "-":
        q[r[0]][r[1]] = w
        if w == "X":
            w = "O"
        else:
            w = "X"
    else:
        print("Nah bruh choose somewhere else")
    return w


gametictic()
