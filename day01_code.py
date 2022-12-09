log_file = open("day01_input.txt")

# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

# max = 0
# current = 0
# while each line is not blank, add to current.
# update max to current is greater than max
# return max

def most_calories(file_name):
    ''''''
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

print(most_calories("day01_input.txt"))

# Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

# array of top three
# if sum is greater than the min num in array, add to array
# if the array size is greater than 3, remove min num



def top_three(file_name):
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

print(top_three("day01_input.txt"))