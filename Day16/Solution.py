def main():
    filehandle = open("./Day16/input.txt")
    lines = []
    for line in filehandle:
        lines.append(line.rstrip())
    parseMeDaddy(lines)

def parseMeDaddy(lines):
    rules = phase1(lines)
    my_ticket_values = phase2(lines, rules[0])
    all_other_tickets = phase3(lines, my_ticket_values[0])
    totalError = calculateErrorRate(rules[1], my_ticket_values[1], all_other_tickets)

    populated_rules = phase1part2(lines)
    value_by_column = phase3part2(totalError[1]) 
    column_map = findAttributes(populated_rules, value_by_column, {})
    getAnswer(column_map, my_ticket_values[1])

def getAnswer(map, my_ticket):
    num = 1
    for k,v in map.items():
        if('departure' in k):
            num *= my_ticket[v]
    print(num)


def findAttributes(rules, value_by_column, column_map):
    
    while len(column_map) != len(rules):
        new_value_list = {}
        for i, values in value_by_column.items():
            potentials = []
            for rule_name, rule in rules.items():
                if rule_name not in column_map:
                    is_correct = True
                    for value in values:
                        if (rule[0][0] <= value <= rule[0][1]) or (rule[1][0] <= value <= rule[1][1]):
                            continue
                        else:
                            is_correct = False
                            break
                    if is_correct:
                        potentials.append(rule_name)
            if(len(potentials) == 1):
                column_map[potentials[0]] = i
            else:
                new_value_list[i] = (values)
        value_by_column = new_value_list

    return column_map



def calculateErrorRate(rules, my_ticket_values, all_other_tickets):
    totalError = 0
    bad_ticket_indexes = list()
    new_all_other_ticket = []

    for i,ticket in enumerate(all_other_tickets):
        for value in ticket:
            isValid = False
            for rule in rules:
                if (rule[0][0] <= value <= rule[0][1]) or (rule[1][0] <= value <= rule[1][1]):
                    isValid = True
                    break
            if(not isValid):
                bad_ticket_indexes.append(i)
                break
    
    for i,ticket in enumerate(all_other_tickets):
        if i not in bad_ticket_indexes:
            new_all_other_ticket.append(ticket)

            
    return totalError, new_all_other_ticket

def phase1(lines):
    rules = []
    i = 0
    for line in lines:
        if( 'your ticket' in line or len(line) == 0):
            break

        split_rules = line.split(':')[1]
        ranges = []
        for rule in split_rules.strip().split(' or '):
            nums = rule.split('-')
            ranges.append((int(nums[0]), int(nums[1])))
        rules.append(ranges)
        i += 1
    return i, rules

def phase1part2(lines):
    rules = {}
    i = 0
    for line in lines:
        if( 'your ticket' in line or len(line) == 0):
            break
        rule_attributes = line.split(':')
        rule_name = rule_attributes[0]
        split_rules = rule_attributes[1]
        ranges = []
        for rule in split_rules.strip().split(' or '):
            nums = rule.split('-')
            ranges.append((int(nums[0]), int(nums[1])))
        rules[rule_name] = ranges
        i += 1
    return rules

def phase2(lines, starting_index):
    ticket_values = []
    i = 0
    for line in lines[starting_index:]:
        if('nearby tickets:' in line):
            break
        if(',' in line):
            values = line.split(',')
            for value in values:
                ticket_values.append(int(value))
        i += 1
    return i + starting_index, ticket_values

def phase3(lines, starting_index):
    all_other_tickets = []
    for line in lines[starting_index:]:
        if(',' in line):
            current_ticket = []
            values = line.split(',')
            for value in values:
                current_ticket.append(int(value))
            all_other_tickets.append(current_ticket)
    return all_other_tickets

def phase3part2(all_other_tickets):
    values_by_column = {}

    for i in range(len(all_other_tickets[0])):
        current_column = []
        for line in all_other_tickets:
            current_column.append(line[i])
        values_by_column[i] = current_column
    
    return values_by_column



main()