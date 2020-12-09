def main():
    filehandle = open("./Day09/input.txt")
    lines = []
    for line in filehandle:
        lines.append(int(line.rstrip()))
    print(findVulnerability(lines, 25))
    #findHighAndLow(lines, 144381670)

def findVulnerability(values, preambleSize: int):
    rolling_preamble = values[:preambleSize]
    allCurrentlyValid = True
    i = preambleSize
    while allCurrentlyValid:
        allCurrentlyValid = sum_checker(rolling_preamble, values[i])
        if(allCurrentlyValid):
            rolling_preamble.remove(rolling_preamble[0])
            rolling_preamble.append(values[i])
            i += 1
        else:
            return values[i]
            
def sum_checker(preamble, value):

    for num in preamble:
        if((value - num) in preamble):
            return True
    return False

def findHighAndLow(values, target_value):
    values = findRange(values, target_value)
    values.sort()
    print(values[0] + values[-1])

def findRange(values, target_value):

    for i, value in enumerate(values):
        running_value = value
        running_list = [value]
        while running_value <= target_value:
            if(running_value == target_value):
                return running_list
            else:
                i += 1
                running_value += values[i]
                running_list.append(values[i])



main()