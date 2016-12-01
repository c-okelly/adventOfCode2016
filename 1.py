# Author Conor O'Kelly

def main():

    movementList = "R3, L2, L2, R4, L1, R2, R3, R4, L2, R4, L2, L5, L1, R5, R2, R2, L1, R4, R1, L5, L3, R4, R3, R1, L1, L5, L4, L2, R5, L3, L4, R3, R1, L3, R1, L3, R3, L4, R2, R5, L190, R2, L3, R47, R4, L3, R78, L1, R3, R190, R4, L3, R4, R2, R5, R3, R4, R3, L1, L4, R3, L4, R1, L4, L5, R3, L3, L4, R1, R2, L4, L3, R3, R3, L2, L5, R1, L4, L1, R5, L5, R1, R5, L4, R2, L2, R1, L5, L4, R4, R4, R3, R2, R3, L1, R4, R5, L2, L5, L4, L1, R4, L4, R4, L4, R1, R5, L1, R1, L5, R5, R1, R1, L3, L1, R4, L1, L4, L4, L3, R1, R4, R1, R1, R2, L5, L2, R4, L1, R3, L5, L2, R5, L4, R5, L5, R3, R4, L3, L3, L2, R2, L5, L5, R3, R4, R3, R4, R3, R1"

    moveArray = movementList.split(',')

    north = 0
    east = 0
    direction = 0

    visitedlocs = []
    visitedTwice = []
    for i in moveArray:
        i = i.strip(" ")
        direc = i[0]
        movement = int(i[1:])
        if direc == "R":
            direction += 90
        else:
            direction -= 90

        # print(abs(direction % 360), movement, " Direction and movment", i)

        for subMove in range(0,movement):
            if (direction % 360) == 0:
                north += 1
            elif (direction % 360) == 90:
                east += 1
            elif (direction % 360) == 180:
                north -= 1
            elif (direction % 360) == 270:
                east -= 1
            else:
                print("Error")

            currentLoc = [north,east]
            if currentLoc in visitedlocs:
                visitedTwice.append(currentLoc)
            visitedlocs.append(currentLoc)

    print("Locations visited twice", visitedTwice)
    print("Distance from start", (abs(north)+abs(east)))

if (__name__ == "__main__"):

    main()
