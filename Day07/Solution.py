import time
def main():
    filehandle = open("./Day07/input.txt")
    lines = []
    for line in filehandle:
        lines.append(line.rstrip())
    initial = time.time()
    all_bags = build_bag_dependencies(lines)

    all_applicable_bags = findAllBagsThatCanHoldCertainColor('shiny gold', all_bags, set())
    nested_bags = findHowManyBagsACertainColorBagHolds('shiny gold', all_bags)
    final = time.time()
    print(len(all_applicable_bags))
    print(nested_bags)
    print(final - initial)

def build_bag_dependencies(lines):
    all_bags = []

    for line in lines:
        all_bags.append(defineBag(line))
    
    return all_bags

def defineBag(line):
    bag_defenition = {}

    bags = line.split('contain')

    bag_color = bags[0].replace(' bags', '').strip()
    bag_defenition['bag_color'] = bag_color
    
    bags_that_fit_within = bags[1].split(',')
    bag_dependencies = []
    for bag in bags_that_fit_within:
        if(' no ' in bag):
            continue
        values = bag.strip().split(' ')
        new_bag_value = {'number': values[0], 'color': f"{values[1]} {values[2]}"}
        bag_dependencies.append(new_bag_value)

    bag_defenition['bags_within'] = bag_dependencies
    
    return bag_defenition

def findAllBagsThatCanHoldCertainColor(bag_color, all_bags, already_found_bags):
    for bag in all_bags:
        has_bag = False
        for containerbags in bag['bags_within']:
            if(containerbags['color'] == bag_color):
                has_bag = True
                break
        if(has_bag):
            already_found_bags.add(bag['bag_color'])
            already_found_bags = findAllBagsThatCanHoldCertainColor(bag['bag_color'], all_bags, already_found_bags)

    return already_found_bags

def findHowManyBagsACertainColorBagHolds(bag_color, all_bags):
    total_amount = 0
    for bag in all_bags:
        if(bag['bag_color'] == bag_color):
            for container_bag in bag['bags_within']:
                amount = int(container_bag['number'])
                total_amount += amount + amount * (findHowManyBagsACertainColorBagHolds(container_bag['color'], all_bags))
    
    return total_amount
    

main()