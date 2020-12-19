def main():
    filehandle = open("./Day19/input.txt")
    lines = []
    for line in filehandle:
        lines.append(line.rstrip())
        print(line)

main()
