# https://adventofcode.com/2021/day/1

input_file_path = 'input.txt'

def part_one():
    previous_depth = None
    depth_increase_count = 0
    with open(input_file_path) as file:
        for line in file:
            depth = int(line)
            if previous_depth and previous_depth < depth:
                depth_increase_count += 1
            previous_depth = depth
    print(depth_increase_count)

def part_two():
    increase_count = 0
    
    with open(input_file_path) as file:
        depths = [ int(line) for line in file ]

    window_sums = []
    try:
        for index in range(len(depths)):
            depth_sum = depths[index] + depths[index+1] + depths[index+2]
            window_sums.append(depth_sum)
    except IndexError:
        pass
    
    previous_sum = None
    for sum in window_sums:
        if previous_sum and sum > previous_sum:
            increase_count += 1
        previous_sum = sum

    print(increase_count)

part_two()