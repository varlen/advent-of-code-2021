# https://adventofcode.com/2021/day/4
import itertools
input_file_path = 'input.txt'

is_assembling_board = False
board_index = 0
boards = []

# Read input data into convenient format
with open(input_file_path) as file:
    for line_number, line_content in enumerate(file):
        if line_number == 0:
            draws = line_content.strip().split(',')
        else:
            stripped_content = line_content.strip()
            if stripped_content:
                if not is_assembling_board:
                    boards.append([])
                    is_assembling_board = True
                boards[-1].append(list(filter(lambda n : n != '', stripped_content.split(' '))))
            else:
                if is_assembling_board:
                    is_assembling_board = False

def column(board, index):
    return list(map(lambda x : x[index], board))

def transpose_board(board):
    return [ column(board, i) for i in range(len(board))]

transposed_boards = list(map(
    transpose_board,
    boards
))

def board_score(board, winning_draw, current_draws):
    board_set = set()
    for row in board:
        board_set.update(set(map(int, row)))
    unmarked_numbers = board_set.difference(set(map(int,current_draws)))
    return sum(unmarked_numbers) * int(winning_draw)

current_draws = set()
boards_that_won = []
try:
    for draw in draws:
        current_draws.add(draw)
        for index, board in enumerate(boards):
            if index in boards_that_won:
                continue
            for row in board:
                if set(row).issubset(current_draws):
                    print(repr(row))
                    print(repr(current_draws))
                    print("BINGO!")
                    print(board_score(board, draw, current_draws))
                    boards_that_won.append(index)
            for col in transposed_boards[index]:
                if set(col).issubset(current_draws):
                    print(repr(col))
                    print(repr(current_draws))
                    print("BINGO!")
                    print(board_score(board, draw, current_draws))
                    boards_that_won.append(index)
                    
except IndexError:
    print("done")