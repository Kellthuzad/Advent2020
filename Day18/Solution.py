def main():
    filehandle = open("./Day18/input.txt")
    lines = []
    for line in filehandle:
        lines.append(line.rstrip())

    runningTotal = 0
    for line in lines:
        runningTotal += int(dealWithParens(line))
    print(runningTotal)


def calulate(line):

    arguments = line.split(' ')    
    currentValue = int(arguments[0])
    i = 1
    while True:
        if(len(arguments) <= i):
            break
        if('*' in arguments[i]):
            i += 1
            currentValue *= int(arguments[i])
        elif '+' in arguments[i]:
            i += 1
            currentValue += int(arguments[i])
        i += 1

    return currentValue


def calulate2(line):
    additive_args = line.split('*')
    newArgs = []
    for arg in additive_args:
        newArg = arg.strip().split(' ')    
        currentValue = int(newArg[0])
        i = 1
        while True:
            if(len(newArg) <= i):
                break
            elif '+' in newArg[i]:
                i += 1
                currentValue += int(newArg[i])
            i += 1
        newArgs.append(currentValue)

    finalValue = 1
    for product in newArgs:
        finalValue *= product

    return finalValue

def dealWithParens(line):

    openingParen = -1
    closingParen = -1
    nestedCount = 0
    for i,char in enumerate(line):
        if('(' == char):
            openingParen = i
            nestedCount += 1
        elif(')' == char and openingParen != -1):
            closingParen = i
            break

            
    
    if(openingParen == -1 and closingParen == -1):
        value = calulate2(line)
        return f'{value}'
    else:
        len(line) - closingParen
        substring = line[openingParen + 1:closingParen]
        value = dealWithParens(substring)
        line = line[:openingParen] + value + line[closingParen + 1:]

    return dealWithParens(line)


main()