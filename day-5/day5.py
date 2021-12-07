
from collections import defaultdict

input_file_path = 'input.txt'

def parse_line(line):
    segment_parts = line.split(' -> ')
    start_point = tuple(map(int, segment_parts[0].split(',')))
    end_point = tuple(map(int, segment_parts[1].split(',')))
    return (start_point, end_point)

with open(input_file_path) as file:
    lines = [
        parse_line(line)
        for line in file
    ]

horizontal_and_vertical_lines  = list(filter(
    lambda line : line[0][0] == line[1][0] or line[0][1] == line[1][1],
    lines
))

line_points = defaultdict(lambda: 0)

for line in lines:
    start_line, end_line = line
    start_x, start_y = start_line
    end_x, end_y = end_line
    vertical = start_x == end_x
    horizontal = start_y == end_y
    
    if vertical:
        if start_y > end_y:
            end_y, start_y = start_y, end_y
        for y in range(start_y, end_y + 1):
            line_points[(start_line[0], y)] += 1
    elif horizontal:
        if start_x > end_x:
            end_x, start_x = start_x, end_x
        for x in range(start_x, end_x + 1):
            line_points[(x, start_line[1])] += 1
    else:
        steps = abs(end_y - start_y) # since its always 45 degrees either x or y would work
        x_variation = 1 if start_x < end_x else -1
        y_variation = 1 if start_y < end_y else -1
        for k in range(0, steps + 1):
            line_points[(start_x + (k * x_variation), start_y + (k * y_variation))] += 1

for j in range(10):
    print(*[ line_points[(i,j)] if line_points[(i,j)] else '.' for i in range(10) ])
print(len([ k for k,v in dict(line_points).items() if v > 1 ]))

        


        
        

