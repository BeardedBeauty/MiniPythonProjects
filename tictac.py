q = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]


def gametictic():
    w = "X"
    game = 1
    while game:
        print("Please enter a number to place on board")
        e = int(raw_input())
        if e >= 9:
            ticplacement([2, 2, w])
        elif e <= 1:
            ticplacement([0, 0, w])
        elif e == 2:
            ticplacement([0, 1, w])
        elif e == 3:
            ticplacement([0, 2, w])
        elif e == 4:
            ticplacement([1, 0, w])
        elif e == 5:
            ticplacement([1, 1, w])
        elif e == 6:
            ticplacement([1, 2, w])
        elif e == 7:
            ticplacement([2, 0, w])
        elif e == 8:
            ticplacement([2, 1, w])
        else:
            game = 0

        if w == "X":
            w = "O"
        else:
            w = "X"

        print(q[0])
        print(q[1])
        print(q[2])


def ticplacement(r):
    if q[r[0]][r[1]] == "-":
        q[r[0]][r[1]] = r[2]


gametictic()
