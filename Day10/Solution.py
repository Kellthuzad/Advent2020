def main():
    filehandle = open("./Day10/input.txt")
    lines = []
    for line in filehandle:
        lines.append(int(line.rstrip()))
    lines.append(0)
    lines.append(max(lines) +3)
    lines.sort()

    print(getJoltages(lines))
    print(dynamicProgrammingTime(lines, {}, 0))

def getJoltages(lines):
    singleJolts = 0
    tripleJolts = 0
    i = 0
    
    if(lines[i] == 1):
        singleJolts += 1
    elif(lines[i] == 3):
        tripleJolts += 1
    while i < len(lines):
        if(i+1 == len(lines)):
            return singleJolts * tripleJolts
        elif((lines[i+1] - lines[i] )== 1):
            singleJolts += 1
        elif((lines[i+1] - lines[i] )== 3):
            tripleJolts += 1
        i += 1

def dynamicProgrammingTime(lines, already_calculated, i):

    if(i == len(lines) - 1):
        return 1
    if i in already_calculated:
        return already_calculated[i]
    
    answer = 0
    for j in range(i + 1, len(lines)):
        if(lines[j] - lines[i] <= 3):
            answer += dynamicProgrammingTime(lines, already_calculated, j)
    
    already_calculated[i] = answer
    return answer

main()