def main():
    filehandle = open("./Day13/input.txt")
    lines = []
    for line in filehandle:
        lines.append(line.rstrip())
    the_input = parseInput(lines)

    #print(waitTimeAndBusId(the_input[0], the_input[1]))
    print(getTimestamp(the_input[1]))
        
def parseInput(lines):
    timestamp = int(lines[0])
    string_busses = lines[1].split(',')
    buses = []
    for i in string_busses:
        if(i == 'x'):
            buses.append(i)
        else:
            buses.append(int(i))
    return (timestamp, buses)
        

def waitTimeAndBusId(timestamp, buses):
    lowest = 9999999999
    lowest_bus = 0
    for bus in buses:
        if bus != 'x':
            remainder = getRemainder(timestamp, bus)
            if(remainder < lowest):
                lowest = remainder
                lowest_bus = bus

    return lowest_bus * lowest

def getRemainder(timestamp, bus):
    multiplier = timestamp//bus
    if(timestamp == (bus * multiplier)):
        return 0
    multiplier += 1
    return (bus * multiplier) - timestamp

def getTimestamp(buses):
    numbers = []
    indexes = []
    for i,bus in enumerate(buses):
        if(bus != 'x'):
            numbers.append(bus)
            indexes.append(bus - i)

    answer = (chinese_remainder(numbers,indexes))
    return answer



from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


main()