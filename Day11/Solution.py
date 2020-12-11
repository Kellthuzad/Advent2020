import copy
def main():
    filehandle = open("./Day11/input.txt")
    lines = []
    for line in filehandle:
        lines.append(list(line.rstrip()))

    conway(lines)
        
def conway(lines):
    new_lines = copy.deepcopy(lines)

    x = 0
    y = 0
    while True:
        currentState = lines[y][x]
        totalOccupied = checkForOccupancy(lines, x, y)
        if(currentState == 'L' and totalOccupied == 0):
            new_lines[y][x] = '#'
        elif(currentState == '#' and totalOccupied > 4):
            new_lines[y][x] = 'L'

        if(x + 1 >= len(lines[0]) and y + 1 >= len(lines)):
            is_same = True
            for (i, line) in enumerate(lines):
                if("".join(line) != "".join(new_lines[i])):
                    is_same = False
                    break
            
            if(is_same):
                totalCount = 0
                for line in lines:
                    for char in line:
                        if char == '#':
                            totalCount +=1
                print(totalCount)
                break
            else:
                lines = copy.deepcopy(new_lines)
                x = 0
                y = 0
        else:
            if(x+1 >= len(lines[0])):
                x = 0
                y += 1
            else:
                x += 1
    
            
def checkForOccupancy(lines, x, y):
    totalOccupancy = 0
    valid_x_values = []
    valid_y_values = []
    valid_x_values.append(x)
    valid_y_values.append(y)
    if(x+1 >= len(lines[0])):
        valid_x_values.append(x-1)
    elif(x == 0):
        valid_x_values.append(x+1)
    else:
        valid_x_values.append(x+1)
        valid_x_values.append(x-1)

    if(y+1 >= len(lines)):
        valid_y_values.append(y-1)
    elif(y == 0):
        valid_y_values.append(y+1)
    else:
        valid_y_values.append(y+1)
        valid_y_values.append(y-1)

    for horizontal in valid_x_values:
        for vertical in valid_y_values:
            if(vertical == y and horizontal == x):
                continue
            new_horizontal = horizontal
            new_vertical = vertical
            while(lines[new_vertical][new_horizontal] == '.'):
                
                if(new_horizontal > x):
                    new_horizontal += 1
                elif new_horizontal < x:
                    new_horizontal -= 1
                
                if new_vertical > y:
                    new_vertical += 1
                elif new_vertical < y:
                    new_vertical -= 1
                
                if(new_horizontal > x and new_horizontal + 1 > len(lines[0])) or (new_vertical > y and new_vertical + 1 > len(lines)) or new_vertical < 0 or new_horizontal < 0:
                    new_horizontal = horizontal
                    new_vertical = vertical
                    break
            if(lines[new_vertical][new_horizontal] == '#'):
                totalOccupancy += 1
    return totalOccupancy
main()