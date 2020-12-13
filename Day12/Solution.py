
def main():
    filehandle = open("./Day12/input.txt")
    lines = []
    for line in filehandle:
        new_line = line.rstrip()
        newinput = [new_line[0], int(new_line[1:])]
        lines.append(newinput)
    ship = buildShipObject()
    waypoint_location = (10,1)
    rotateWaypointRight((10,1), 180)
    for line in lines:
        waypoint_location = handleDirection2(line, ship, waypoint_location)
    coordinates = ship['position']
    print(abs(coordinates[0]) + abs(coordinates[1]))




def handleDirection(line, ship):

    if(line[0] == 'F'):
        ship['position'] = moveShipInDirection(ship, ship['direction'], line[1])
    elif(line[0] == 'N'):
        ship['position'] = moveShipInDirection(ship, 'N', line[1])
    elif(line[0] == 'S'):
        ship['position'] = moveShipInDirection(ship, 'S', line[1])
    elif(line[0] == 'E'):
        ship['position'] = moveShipInDirection(ship, 'E', line[1])
    elif(line[0] == 'W'):
        ship['position'] = moveShipInDirection(ship, 'W', line[1])
    elif(line[0] == 'R'):
        ship['direction'] = rotateShipRight(ship, line[1])
    elif(line[0] == 'L'):
        ship['direction'] = rotateShipLeft(ship, line[1])
        
def handleDirection2(line, ship, waypoint):

    if(line[0] == 'F'):
        ship['position'] = moveShipToWaypoint(ship, waypoint, line[1])
    elif(line[0] == 'N'):
        waypoint = moveWaypoint(waypoint, 'N', line[1])
    elif(line[0] == 'S'):
        waypoint = moveWaypoint(waypoint, 'S', line[1])
    elif(line[0] == 'E'):
        waypoint = moveWaypoint(waypoint, 'E', line[1])
    elif(line[0] == 'W'):
        waypoint = moveWaypoint(waypoint, 'W', line[1])
    elif(line[0] == 'R'):
        waypoint = rotateWaypointRight(waypoint, line[1])
    elif(line[0] == 'L'):
        waypoint = rotateWaypointLeft(waypoint, line[1])
    return waypoint

def moveShipToWaypoint(ship, waypoint, magnitude):
    xposition = waypoint[0] * magnitude
    yposition = waypoint[1] * magnitude

    xposition += ship['position'][0]
    yposition += ship['position'][1]
    return (xposition, yposition)


def moveWaypoint(waypoint, direction, magnitude):
    xposition = waypoint[0]
    yposition = waypoint[1]
    if(direction == 'E'):
        xposition += magnitude
    elif(direction == 'S'):
        yposition -= magnitude
    elif(direction == 'W'):
        xposition -= magnitude
    elif(direction == 'N'):
        yposition += magnitude
    
    return (xposition, yposition)

def rotateWaypointRight(waypoint, degrees):
    rotationAmount = int(degrees/90)
    xposition = waypoint[0]
    yposition = waypoint[1]
    newxposition = xposition
    newyposition = yposition
    for i in range(rotationAmount):
        newxposition = yposition 
        newyposition = xposition * -1
        xposition = newxposition
        yposition = newyposition
    return (newxposition, newyposition)

def rotateWaypointLeft(waypoint, degrees):
    rotationAmount = int(degrees/90)
    xposition = waypoint[0]
    yposition = waypoint[1]
    newxposition = xposition
    newyposition = yposition
    for i in range(rotationAmount):
        newxposition = yposition * -1
        newyposition = xposition 
        xposition = newxposition
        yposition = newyposition
    return (newxposition, newyposition)

def buildShipObject():
    ship = {}
    ship['direction'] = 'E'
    ship['position'] = (0,0)

    return ship

def moveShipInDirection(ship, direction, magnitude):
    xposition = ship['position'][0]
    yposition = ship['position'][1]
    if(direction == 'E'):
        xposition += magnitude
    elif(direction == 'S'):
        yposition -= magnitude
    elif(direction == 'W'):
        xposition -= magnitude
    elif(direction == 'N'):
        yposition += magnitude
    
    return (xposition, yposition)

def rotateShipRight(ship, degrees):
    rotationAmount = int(degrees/90)

    direction = ship['direction']

    for i in range(rotationAmount):
        if(direction == 'E'):
            direction = 'S'
        elif(direction == 'S'):
            direction = 'W'
        elif(direction == 'W'):
            direction = 'N'
        elif(direction == 'N'):
            direction = 'E'
    
    return direction

def rotateShipLeft(ship, degrees):
    rotationAmount = int(degrees/90)

    direction = ship['direction']

    for i in range(rotationAmount):
        if(direction == 'E'):
            direction = 'N'
        elif(direction == 'S'):
            direction = 'E'
        elif(direction == 'W'):
            direction = 'S'
        elif(direction == 'N'):
            direction = 'W'
    
    return direction

main()