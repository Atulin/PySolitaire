
boardx = 8
boardy = 8

Matrix = [[" " for x in range(boardx)] for y in range(boardy)]
Letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
History = []
Run = True

# Make matrix

for y in range(0, 8):
    for x in range(0, 8):
        if x in {3, 4, 5} or y in {3, 4, 5}:
            Matrix[x][y] = "X"
        if x == 4 and y == 4:
            Matrix[x][y] = " "
        if y == 0:
            Matrix[x][0] = Letters[x - 1]
        if x == 0 and y == 0:
            Matrix[0][0] = "x"

        Matrix[0][y] = str(y)

while Run:
    History.append(Matrix)

    for y in range(0, 8):
        row = ""
        for x in range(0, 8):
            row += Matrix[x][y] + " "
        print(row)

    Command = input("> Next move: ")
    print()

    Start = Command.split(">")[0]
    Target = Command.split(">")[1]

    StartArr = list(Start)
    TargetArr = list(Target)

    StartCoords = [0, 0]
    TargetCoords = [0, 0]

    StartCoords[0] = int(Letters.index(StartArr[0]))+1
    StartCoords[1] = int(StartArr[1])

    TargetCoords[0] = int(Letters.index(TargetArr[0]))+1
    TargetCoords[1] = int(TargetArr[1])

    if Matrix[StartCoords[0]][StartCoords[1]] == "X":
        if Matrix[TargetCoords[0]][TargetCoords[1]] == " ":
            movex = abs(StartCoords[0] - TargetCoords[0]) == 2 and abs(StartCoords[1] - TargetCoords[1]) == 0
            movey = abs(StartCoords[0] - TargetCoords[0]) == 0 and abs(StartCoords[1] - TargetCoords[1]) == 2

            if movex or movey:
                Matrix[StartCoords[0]][StartCoords[1]] = " "
                Matrix[TargetCoords[1]][TargetCoords[1]] = "X"

                removey = (StartCoords[0] + StartCoords[1]) / 2
                removex = (TargetCoords[0] + TargetCoords[1]) / 2

                Matrix[int(removex)][int(removey)] = " "
            else:
                print("You can't move the pawn that far\n")
        else:
            print("The target spot is occupied\n")
    else:
        print("No pawn exists there\n")
