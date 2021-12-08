from collections import Counter, defaultdict

input_file_path = 'input.txt'

with open(input_file_path) as file:
    input = list(map(int,file.readline().strip().split(',')))

example = list(map(int,'16,1,2,0,4,2,7,1,2,14'.split(',')))

# Part 1
minimal_fuel_consumption_1 = min([ 
    sum(map(lambda crab_position : abs(final_position - crab_position), input))
    for final_position in range(min(input), max(input) + 1) 
])
    
print(f"{minimal_fuel_consumption_1=}")

# Part 2
def sum_one_to_n(value):
    return value * (value + 1) // 2

minimal_fuel_consumption_2 = min([ 
    sum(map(lambda crab_position : sum_one_to_n(abs(final_position - crab_position)), input))
    for final_position in range(min(input), max(input) + 1) 
])

print(f"{minimal_fuel_consumption_2=}")