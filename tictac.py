q = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]


def gametictic():
    print(q)
    w = "X"
    game = 1
    while game:
        print("Please enter a number to place on board")
        e = int(raw_input())
        if e >= 9:
            q[2][2] = w
        elif e <= 1:
            q[0][0] = w
        elif e == 2:
            q[0][1] = w
        elif e == 3:
            q[0][2] = w
        elif e == 4:
            q[1][0] = w
        elif e == 5:
            q[1][1] = w
        elif e == 6:
            q[1][2] = w
        elif e == 7:
            q[2][0] = w
        elif e == 8:
            q[2][1] = w
        game = 0


gametictic()
