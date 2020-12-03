def main():
    filehandle = open("./Day02/input.txt")
    lines = []
    validpw = 0
    for line in filehandle:
        lines.append(line.rstrip())
    for thing in lines:
        validpw += validate2(thing.split(' '))
    print(validpw)

def validate(inputArray):
    range = inputArray[0].split('-')
    importantchar = inputArray[1][0]
    password = inputArray[2]
    occurences = 0

    for char in password:
        if(char == importantchar):
            occurences += 1
    
    if(occurences >= int(range[0]) and occurences <= int(range[1])):
        return 1
    
    return 0


def validate2(inputArray):
    index = inputArray[0].split('-')
    importantchar = inputArray[1][0]
    password = inputArray[2]

    if((password[int(index[0]) - 1] == importantchar and password[int(index[1]) - 1] != importantchar) 
    or (password[int(index[0]) - 1] != importantchar and password[int(index[1]) - 1] == importantchar)):
        return 1
    
    return 0

    



main()
        