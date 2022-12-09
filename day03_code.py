import string

from input_helper import convert_data_to_list


PRIORITIES = list(string.ascii_lowercase + string.ascii_uppercase)


########### PART 1 ###########
def split_compartment(rucksack):
    compartment1 = rucksack[:len(rucksack)//2]
    compartment2 = rucksack[len(rucksack)//2 if len(rucksack)%2 == 0
                                 else ((len(rucksack)//2)+1):]
    return [compartment1, compartment2]


def shared_item(compartments):
    compartments = [set(compartment) for compartment in compartments]
    item = set.intersection(*compartments)
    return list(item)


def priority_total_1(file_name):
    total = 0
    
    rucksacks = convert_data_to_list(file_name)
    
    for rucksack in rucksacks:
        item = shared_item(split_compartment(rucksack))[0]
        total += PRIORITIES.index(item) + 1

    return total


########### PART 2 ###########
def priority_total_2(file_name):
    total = 0
    
    rucksacks = convert_data_to_list(file_name)
    
    for i in range(0, len(rucksacks), 3):
        rucksack_trio = [set(rucksacks[i]), set(rucksacks[i+1]), set(rucksacks[i+2])]
        item = shared_item(rucksack_trio)[0]
        total += PRIORITIES.index(item) + 1

    return total