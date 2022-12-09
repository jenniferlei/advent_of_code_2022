from day01_code import max_calories_carried, top_three_calories
from day02_code import your_total_score_strategy_1, your_total_score_strategy_2
from day03_code import priority_total_1, priority_total_2

day_1_file = "inputs/day01_input.txt"
print("🎄 Day 1 🎄")
print("-------------")
print(f"Part 1: {max_calories_carried(day_1_file)}")
print(f"Part 2: {top_three_calories(day_1_file)}")
print()

day_2_file = "inputs/day02_input.txt"
print("🎄 Day 2 🎄")
print("-------------")
print(f"Part 1: {your_total_score_strategy_1(day_2_file)}")
print(f"Part 2: {your_total_score_strategy_2(day_2_file)}")
print()

day_3_file = "inputs/day03_input.txt"
print("🎄 Day 3 🎄")
print("-------------")
print(f"Part 1: {priority_total_1(day_3_file)}")
print(f"Part 2: {priority_total_2(day_3_file)}")
print()

