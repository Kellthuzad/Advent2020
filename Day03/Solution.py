def main():
    filehandle = open("./Day03/input.txt")
    lines = []
    for line in filehandle:
        lines.append(line.rstrip())
    
    print(slidedown(lines))

def slidedown(slope):
    trees_encountered = 0
    x_position = 0
    width = len(slope[0])
    angles = [1,3,5,7]
    trees = []
    for num in angles:

        for row in slope:
            if(row[x_position] == '#'):
                trees_encountered += 1

            x_position += num 
            x_position = x_position % width

        trees.append(trees_encountered)
        print(trees_encountered)
        x_position = 0
        trees_encountered = 0
    
    
    i = 0
    while i < len(slope):
        if(slope[i][x_position] == '#'):
            trees_encountered += 1

        x_position += 1 
        x_position = x_position % width
        i += 2
    print(trees_encountered)
    trees.append(trees_encountered)

    total = 1
    for count in trees:
        total = total * count
    
    return total

main()