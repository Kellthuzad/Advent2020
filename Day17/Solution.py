import time
def main():
    filehandle = open("./Day17/input.txt")
    lines = []
    for line in filehandle:
        lines.append(line.rstrip())
    i_Time = time.time()
    cube_state = initializeState(lines)
    bounds = setBounds(cube_state)
    
    print(setNewState(cube_state, bounds))
    f_Time = time.time()
    print(f_Time - i_Time)

def setBounds(cube_state):
    z_min = 0
    z_max = 0
    y_min = 0
    y_max = 0
    x_min = 0
    x_max = 0
    h_min = 0
    h_max = 0

    for item in cube_state:
        if(item[0] >= x_max):
            x_max = item[0] + 1
        if item[0] <= x_min:
            x_min = item[0] - 1

        if(item[1] >= y_max):
            y_max = item[1] +1
        if item[1] <= y_min:
            y_min = item[1] -1

        if(item[2] >= z_max):
            z_max = item[2] +1
        if item[2] <= z_min:
            z_min = item[2] -1

        if(item[3] >= h_max):
            h_max = item[3] +1
        if item[3] <= h_min:
            h_min = item[3] -1

    return((x_min,x_max), (y_min, y_max), (z_min,z_max), (h_min, h_max))

def setNewState(cube_state, bounds):
    new_cube_state = set()
    for i in range(6):
        for x in range(bounds[0][0],bounds[0][1]+1):
            for y in range(bounds[1][0],bounds[1][1]+1):
                for z in range(bounds[2][0],bounds[2][1]+1):
                    for h in range(bounds[3][0],bounds[3][1]+1):
                        totalNearbyActive = checkSurrounding(cube_state, (x,y,z,h))
                        if((x,y,z,h) in cube_state and 2 <= totalNearbyActive <= 3):
                            new_cube_state.add((x,y,z,h))
                        elif (x,y,z,h) not in cube_state and totalNearbyActive == 3:
                            new_cube_state.add((x,y,z,h))
        cube_state = new_cube_state
        bounds = setBounds(cube_state)
        new_cube_state = set()
    
    return len(cube_state)

def checkSurrounding(cube_state, current_location):
    totalNearbyActive = 0
    for x in range(-1,2):
        for y in range(-1,2):
            for z in range(-1,2):
                for h in range(-1,2):
                    if(x == 0 and y == 0 and z == 0 and h == 0):
                        continue
                    dx = current_location[0] + x
                    dy = current_location[1] + y
                    dz = current_location[2] + z
                    dh = current_location[3] + h
                    if (dx, dy, dz, dh) in cube_state:
                        totalNearbyActive += 1
    return totalNearbyActive


def initializeState(lines):
    cube_state = set()

    for y, line in enumerate(lines):
        for x,char in enumerate(line):
            if(char == '#'):
                cube_state.add((x,y,0,0))

    return cube_state








main()