def main():
    filehandle = open("./Day14/input.txt")
    lines = []
    for line in filehandle:
        lines.append(line.rstrip())
    print(initialize(lines))

def convertToBinary(line):
    return int(line, 2)
    
    
def initialize(lines):
    current_mask = []
    memory = {}
    for line in lines:
        if('mask' in line):
            split_line = line.split('=')
            current_mask = getMaskArray(list(split_line[1].strip()))
        elif('mem' in line):
            modifyMemory2(memory, line, current_mask)
    
    current_sum = 0
    for key, value in memory.items():
        current_sum += value

    return current_sum

def modifyMemory(memory, line, current_mask):
    split_line = line.split('=')
    memory_location = split_line[0]
    value_to_place = int(split_line[1])
    binary = f'{value_to_place:036b}'

    for mask in current_mask:
        if mask != 'X':
            binary = binary[:mask[0]] + mask[1] + binary[mask[0] + 1:]

    memory[memory_location] = convertToBinary(binary)

def modifyMemory2(memory, line, current_mask):
    split_line = line.split('=')
    memory_location = int(split_line[0][4:-2])
    value_to_place = int(split_line[1])
    binary = f'{memory_location:036b}'


    allAddresses = getMaskAddress(binary, current_mask)

    for address in allAddresses:
        memory[address] = value_to_place



def getMaskArray(stringarray):
    mask_locations = []
    for i,char in enumerate(stringarray):
        mask_locations.append((i, char))
    return mask_locations

def getMaskAddress(memory_address, current_mask):

    all_memory_addresses = []
    for mask in current_mask:
        if mask[1] == '1':
            memory_address = memory_address[:mask[0]] + mask[1] + memory_address[mask[0] + 1:]

    all_memory_addresses.append(memory_address)
    for mask in current_mask:
        if mask[1] == 'X':
            new_addresses = []
            for address in all_memory_addresses:
                memory_address1 = address[:mask[0]] + '1' + address[mask[0] + 1:]
                memory_address2 = address[:mask[0]] + '0' + address[mask[0] + 1:]
                new_addresses.append(memory_address1)
                new_addresses.append(memory_address2)
            all_memory_addresses = new_addresses
    
    final_addresses = []

    for address in all_memory_addresses:
        final_addresses.append(convertToBinary(address))

    return final_addresses

main()