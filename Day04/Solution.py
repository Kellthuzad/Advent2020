def main():
    filehandle = open("./Day04/input.txt")
    lines = []
    for line in filehandle:
        lines.append(line.rstrip())
    
    passports = breakupByPassport(lines)
    totalValid = 0
    for passp in passports:
        totalValid += validatePassport(passp)
    print(totalValid)

def breakupByPassport(lines):
    passports = []
    currentPassport = ''

    for line in lines:
        if (len(line) == 0):
            passports.append(currentPassport)
            currentPassport = ''
        else:
            currentPassport += ' ' + line
    
    passports.append(currentPassport)
    return passports

def validatePassport(passport):

    attributes = {'byr': 0, 'iyr': 0, 'eyr': 0, 'hgt': 0, 'hcl': 0, 'ecl': 0, 'pid':0}
    keyvalues = passport.split(' ')

    for item in keyvalues:
        keyvalue = item.split(':')
        att = keyvalue[0]
        value = keyvalues[1]

        if(len(item) > 0 and att in attributes.keys() and validateValue(keyvalue)):
            attributes[att] = 1
    
    for att in attributes:
        if(attributes[att] == 0):
            return 0
    return 1

def validateValue(keyvalue):
    eyecolors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    hexvalues = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    if(keyvalue[0] == 'byr' and len(keyvalue[1]) == 4 and int(keyvalue[1]) >= 1920 and int(keyvalue[1]) <= 2002):
        return True
    elif(keyvalue[0] == 'iyr' and len(keyvalue[1]) == 4 and int(keyvalue[1]) >= 2010 and int(keyvalue[1]) <= 2020):
        return True
    elif(keyvalue[0] == 'eyr' and len(keyvalue[1]) == 4 and int(keyvalue[1]) >= 2020 and int(keyvalue[1]) <= 2030):
        return True
    elif(keyvalue[0] == 'hgt' and ('cm' in keyvalue[1] or 'in' in keyvalue[1])):
        value = keyvalue[1]
        if('cm' in value and int(value[:-2]) >= 150 and int(value[:-2]) <= 193):
            return True
        elif('in' in value and int(value[:-2]) >= 59 and int(value[:-2]) <= 76):
            return True
    elif(keyvalue[0] == 'hcl' and keyvalue[1][0] == '#' and len(keyvalue[1]) == 7):
        for char in keyvalue[1][1:]:
            if(char not in hexvalues):
                return False
        return True
    elif(keyvalue[0] == 'ecl' and keyvalue[1] in eyecolors):
        return True
    elif(keyvalue[0] == 'pid' and len(keyvalue[1]) == 9):
        try:
            int(keyvalue[1])
            return True
        except ValueError:
            return False
    return False
          



main()