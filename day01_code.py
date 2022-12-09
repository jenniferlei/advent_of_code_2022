########### PART 1 ###########
def max_calories_carried(file_name):
    """Returns Calories of Elf carrying the most Calories"""
    log_file = open(file_name)
    
    max_calories, current_calories = 0, 0
    
    for line in log_file:
        line = line.rstrip()

        if line != "":
            current_calories += int(line)
        else:
            max_calories = max(current_calories, max_calories)
            current_calories = 0
            
    return max_calories


########### PART 2 ###########
def top_three_calories(file_name):
    """Returns sum of Calories of top three Elves carrying the most Calories"""
    log_file = open(file_name)
    
    top_three_cal = [0]
    current_calories = 0

    for line in log_file:
        line = line.rstrip()

        if line != "":
            current_calories += int(line)
        else:
            min_cal = min(top_three_cal)
            if current_calories > min_cal:
                top_three_cal.append(current_calories)
                if len(top_three_cal) > 3:
                    top_three_cal.remove(min_cal)
            current_calories = 0
            
    return sum(top_three_cal)
