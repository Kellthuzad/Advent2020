import urllib.request as Request


def main():
    filehandle = open("./Day01/input.txt")
    lines = []
    numbers = []
    for line in filehandle:
        lines.append(line)
        numbers.append(int(line))
    print(find2020sum(numbers))

def find2020sum(numbers):
    for x in numbers:
       for y in numbers:
           for z in numbers:
                if (x + y + z == 2020):
                    return x*y*z
                    

main()