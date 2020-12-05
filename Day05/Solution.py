def main():
    filehandle = open("./Day05/input.txt")
    lines = []
    for line in filehandle:
        lines.append(line.rstrip())


    seats = getAllSeatIds(lines)

    print(max(seats))
    print(getMissingSeat(seats))
    
    

def binarysplit(command, minNumber, maxNumber):
    delta = (maxNumber - minNumber)//2 + 1
    if(command == 'B' or command == 'R'):
        minNumber += delta
    elif(command == 'F' or command == 'L'):
        maxNumber -= delta 
    return (minNumber, maxNumber)

def binarytraversal(commands, minNumber, maxNumber):
    for command in commands:
        (minNumber, maxNumber) = binarysplit(command, minNumber, maxNumber)
        if(minNumber == maxNumber):
            break
    return minNumber

def find_seat_ID(boardingpass):
    row = binarytraversal(boardingpass[:7], 0, 127)
    column = binarytraversal(boardingpass[-3:], 0, 7)

    return row * 8 + column
    
def getAllSeatIds(lines):
    seats = []
    for boardingpass in lines:
        seats.append(find_seat_ID(boardingpass))
    
    return seats

def getMissingSeat(seats):
    seats.sort()    
    previousSeat = seats[0]
    for seat in seats[1:]:
        if(previousSeat + 1 != seat):
            return (previousSeat + 1)
        previousSeat = seat

main()