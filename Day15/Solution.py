def main():
    filehandle = open("./Day15/input.txt")
    lines = []
    for line in filehandle:
        lines.append(line.rstrip())
        numbers('1,3,2')


def numbers(line):
    num_array = line.split(',')

    i = 1
    dictionary_of_num = {}
    last_number = ''
    for num in num_array:
        dictionary_of_num[num] = i
        i += 1
        last_number = num
    
    last_number = '0'
    i += 1
    while i <= 2020:
        if(last_number in dictionary_of_num):
            old_number = last_number
            last_number =  f'{(i - 1) - dictionary_of_num[old_number]}'
            dictionary_of_num[old_number] = i - 1
        else:
            dictionary_of_num[last_number] = i - 1
            last_number = '0'
        i += 1

    print(last_number)



main()