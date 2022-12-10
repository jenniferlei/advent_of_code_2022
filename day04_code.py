import re

from input_helper import convert_data_to_list


########### PART 1 ###########
def split_assignments(assignment):
    assignment1_start, assignment1_end, assignment2_start, assignment2_end = re.split("-|,", assignment)
    return [int(assignment1_start), int(assignment1_end), int(assignment2_start), int(assignment2_end)]


def full_overlap(file_name):
    total = 0
    
    assignments = convert_data_to_list(file_name)
    
    for assignment in assignments:
        assignment1_start, assignment1_end, assignment2_start, assignment2_end = split_assignments(assignment)

        if ((assignment1_start >= assignment2_start and assignment1_end <= assignment2_end)
            or (assignment2_start >= assignment1_start and assignment2_end <= assignment1_end)):
            total += 1
    
    return total


########### PART 2 ###########
def partial_overlap(file_name):
    total = 0
    
    assignments = convert_data_to_list(file_name)
    
    for assignment in assignments:
        assignment1_start, assignment1_end, assignment2_start, assignment2_end = split_assignments(assignment)
        
        if ((assignment1_start >= assignment2_start and assignment1_start <= assignment2_end)
           or (assignment2_start >= assignment1_start and assignment2_start <= assignment1_end)):
            total += 1
    
    return total