def main():
    filehandle = open("./Day19/input.txt")
    lines = []
    for line in filehandle:
        lines.append(line.rstrip())
    isPartTwo = True
    ruleDict = buildDepChain(lines, isPartTwo)
    input_lines = getInput(lines)
    #print(calculateRuleZero(ruleDict, input_lines))
    print((SPECIALCASETIMEBABY(8, ruleDict, 88)))


def calculateRuleZero(ruleDict, input_lines):
    longest = 0
    for line in input_lines:
        if len(line) > longest:
            longest = len(line)
    
    ruleset = ruleCalculator(0,ruleDict[0],ruleDict, longest)
    totalCorrect = 0
    for line in input_lines:
        if(line in ruleset):
            totalCorrect += 1

    return totalCorrect


def ruleCalculator(rule_number, or_ruleset, ruleDict, longest):
    if(or_ruleset == 'a' or or_ruleset == 'b'):
        return {or_ruleset}
    if(rule_number == 8 or rule_number == 11):
        SPECIALCASETIMEBABY(rule_number, ruleDict, longest)
    potentialStrings = set()
    
    for and_ruleset in or_ruleset:
        currentRules = ['']
        for rule in and_ruleset:
            values = ruleCalculator(rule, ruleDict[rule], ruleDict, longest)
            newRules = []
            for value in values:
                for string in currentRules:
                    string += value
                    newRules.append(string)
            currentRules = newRules
        
        for rule in currentRules:
            potentialStrings.add(rule)

    return potentialStrings
        
def SPECIALCASETIMEBABY(rule_number, ruleDict, longest):

    looptimes = longest//8
    ruleArray = []

    if rule_number == 8:
        ruleArray = [42]
    if rule_number == 11:
        ruleArray = [42,31]

    potentialStrings = set()
    currentRules = {''}
    for loop in range(looptimes):
        for rule in ruleArray:
            values = ruleCalculator(rule, ruleDict[rule], ruleDict, longest)
            newRules = set()
            for value in values:
                for string in currentRules:
                    string += value
                    newRules.add(string)
            currentRules = newRules
            for rule in currentRules:
                potentialStrings.add(rule)
    
    return potentialStrings



def buildDepChain(lines, isPartTwo):
    ruleDict = {}
    for line in lines:
        if len(line) == 0:
            break
        
        rule_breakdown = line.split(':')
        if('a' in rule_breakdown[1] or 'b' in rule_breakdown[1]):
            ruleDict[int(rule_breakdown[0])] = rule_breakdown[1].strip(' "')
            continue
        if(int(rule_breakdown[0]) == 8 and isPartTwo):
            ruleDict[8] = [[42], [42,8]]
            continue
        elif(int(rule_breakdown[0]) == 11 and isPartTwo):
            ruleDict[11] = [[42, 31], [42,11,31]]
            continue

        rules = rule_breakdown[1].split('|')
        or_rules = []
        for rule in rules:
            and_rules = []
            nums = rule.strip().split(' ')
            for num in nums:
                and_rules.append(int(num))
            or_rules.append(and_rules)
        
        ruleDict[int(rule_breakdown[0])] = or_rules

    return ruleDict

def getInput(lines):
    startCollecting = False
    input_lines = []
    for line in lines:
        if len(line) == 0:
            startCollecting = True
            continue
        if startCollecting:
            input_lines.append(line)

    return input_lines
        



main()
