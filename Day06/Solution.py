def main():
    filehandle = open("./Day06/input.txt")
    lines = []
    for line in filehandle:
        lines.append(line.rstrip())
    output = parseInput(lines)
    print(countAll(output))

    parseInputForSimilar(lines)


def parseInput(lines):
    list_of_sets = []
    s = set()
    for line in lines:
        if(len(line) is 0):
            list_of_sets.append(s)
            s = set()
        else:
            for char in line:
                s.add(char)
    list_of_sets.append(s)
    return list_of_sets

def countAll(list_of_sets):
    total = 0
    for answers in list_of_sets:
        total += len(answers)

    return total

def parseInputForSimilar(lines):
    total = 0
    currentList = []
    makeNewList = True
    for line in lines:
        if(len(line) == 0):
            total += len(currentList)
            currentList = []
            makeNewList = True
        elif(makeNewList):
            currentList = line
            makeNewList = False
        else:
            currentList = set(currentList).intersection(line)
    total += len(currentList)

    print(total)




main()
