import copy
def main():
    filehandle = open("./Day08/input.txt")
    lines = []
    for line in filehandle:
        lines.append(line.rstrip())
    commands = parseInput(lines)
    executeCommands(commands)
    mutations = set()
    while True:
        values = mutateCommands(commands, mutations)
        mutations = values[0]
        if(values[1]):
            print(values[2])
            break

def parseInput(lines):
    commands = []

    for line in lines:
        values = line.split()
        command = values[0]
        magnitude = int(values[1])
        commands.append((command, magnitude))
    
    return commands

def executeCommands(commands):
    accum = 0
    commands_ran = set()
    i = 0
    while True:
        if(i in commands_ran):
            print(accum)
            break
        commands_ran.add(i)

        if(commands[i][0] == 'nop'):
            i += 1
        elif(commands[i][0] == 'acc'):
            accum += commands[i][1]
            i += 1
        elif(commands[i][0] == 'jmp'):
            i += commands[i][1]
        
def mutateCommands(commands, mutations_ran):
    accum = 0
    commands_ran = set()
    new_commands = copy.deepcopy(commands)
    i = 0
    hasMutated = False
    trulyTerminated = True
    while True:
        if(i in commands_ran):
            trulyTerminated = False
            break
        elif(i >= len(new_commands)):
            break
        commands_ran.add(i)
        
        if(new_commands[i][0] == 'nop' and i not in mutations_ran and not hasMutated):
            mutations_ran.add(i)
            new_commands[i] = ('jmp', new_commands[i][1])
            hasMutated = True
        elif(new_commands[i][0] == 'jmp' and i not in mutations_ran  and not hasMutated):
            mutations_ran.add(i)
            new_commands[i] = ('nop', new_commands[i][1])
            hasMutated = True

        if(new_commands[i][0] == 'nop'):
            i += 1
        elif(new_commands[i][0] == 'acc'):
            accum += new_commands[i][1]
            i += 1
        elif(new_commands[i][0] == 'jmp'):
            i += new_commands[i][1]
    
    return(mutations_ran, trulyTerminated, accum)

main()