# https://adventofcode.com/2021/day/2

input_file_path = 'input.txt'

def part_one():  
    depth = 0
    horizontal = 0
    with open(input_file_path) as file:
        for line in file:
            line_content = line.split(' ')
            command, value = line_content[0], int(line_content[1])

            if command == 'down':
                depth += value
            elif command == 'up':
                depth -= value
            elif command == 'forward':
                horizontal += value
    
    print(depth * horizontal)

def part_two():  
    depth = 0
    horizontal = 0
    aim = 0
    with open(input_file_path) as file:
        for line in file:
            line_content = line.split(' ')
            command, value = line_content[0], int(line_content[1])

            if command == 'down':
                aim += value
            elif command == 'up':
                aim -= value
            elif command == 'forward':
                horizontal += value
                depth += aim * value
    
    print(depth * horizontal)

part_two()