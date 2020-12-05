def main():
    filehandle = open("./Day05/input.txt")
    lines = []
    for line in filehandle:
        lines.append(line.rstrip())

    seats = []
    highestSeatid = -5
    for boardingpass in lines:
        currentSeatId = find_seat_ID(boardingpass)
        seats.append(currentSeatId)
        if(highestSeatid < currentSeatId):
            highestSeatid = currentSeatId
    print(highestSeatid)

    seats.sort()

    previousSeat = seats[0]
    for seat in seats[1:]:
        if(previousSeat + 1 != seat):
            print(previousSeat + 1)
            break
        previousSeat = seat


def binarysplit(command, minNumber, maxNumber):
    delta = int((maxNumber - minNumber)/2) + 1

    if(command == 'B' or command == 'R'):
        minNumber += delta
    elif(command == 'F' or command == 'L'):
        maxNumber -= delta 
    return (minNumber, maxNumber)

def find_seat_ID(boardingpass):

    minNumber = 0
    maxNumber = 127
    for command in boardingpass[:7]:
        (minNumber, maxNumber) = binarysplit(command, minNumber, maxNumber)
        if(minNumber == maxNumber):
            break
    row = minNumber

    minNumber = 0
    maxNumber = 7
    for newCommand in boardingpass[-3:]:
        (minNumber, maxNumber) = binarysplit(newCommand, minNumber, maxNumber)
        if(minNumber == maxNumber):
            break
    column = minNumber

    return row * 8 + column
    

main()