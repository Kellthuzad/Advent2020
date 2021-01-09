def main():
    filehandle = open("./Day25/input.txt")
    lines = []
    for line in filehandle:
        lines.append(int(line.rstrip()))
    pk = calculate_private_key(lines[0], 7)
    print(calculate_encryption_key(pk, lines[1]))

def calculate_encryption_key(loopsize, public_key):
    loops = 1
    value = 1
    while loops <= loopsize:
        value = value * public_key
        value = value % 20201227
        loops += 1
    return value

def calculate_private_key(public_key, subject_number):
    number = 1
    loopsize = 0
    while public_key != number:
        number = number * subject_number
        number = number % 20201227
        loopsize += 1
    
    return loopsize

main() 