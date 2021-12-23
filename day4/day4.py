#!/usr/bin/env python
import os 

dir_path = os.path.dirname(os.path.realpath(__file__)) + "\\"
file = open(dir_path + "example_input.txt", "r")
lines = file.readlines()

class BingoBoard:
    def __init__(self, lines):
        self.board_real = []
        self.board_binary = []
        for line in lines:
            temp_array_real = []
            temp_array_binary = []
            for item in filter(None, line.split(' ')):
                temp_array_real.append(int(item.strip()))
                temp_array_binary.append(0)
            self.board_real.append(temp_array_real)
            self.board_binary.append(temp_array_binary)

    def mark_number(self, num):
        for row_idx, row in enumerate(self.board_real):
            for col_idx, val in enumerate(row):
                if val == num:
                    self.board_binary[row_idx][col_idx] = 1

    def check_horizontal_win(self):
        for row in self.board_binary:
            win = True
            for val in row:
                if val == 0:
                    win = False
            if win:
                return True
        return False

    def check_vertical_win(self):
        length = len(self.board_real)
        for col_idx in range(length):
            win = True
            for row_idx in range(length):
                if self.board_binary[row_idx][col_idx] == 0:
                    win = False
            if win:
                return True
        return False

    # Return true if winning board, false if not
    def check_win(self):
        return self.check_horizontal_win() or self.check_vertical_win()

    def get_sum_of_unmarked_numbers(self):
        for row_idx, row in 
    
# 4.1

def remove_newlines(line):
    return line.replace("\n", "")

def get_bingo_game_info(lines):
    lines = list(map(remove_newlines, lines))
    nums_called = lines[0].split(',')
    lines = lines[2:-1]
    temp_array = []
    boards = []
    for line in lines:
        if line == "":
            boards.append(BingoBoard(temp_array))
            temp_array = []
        else:
            temp_array.append(line.strip())
    boards.append(BingoBoard(temp_array))
    return list(map(int, nums_called)), boards

# 4.1
def get_final_game_state(called, boards):
  for num in called:
    for idx, board in enumerate(boards):
        board.mark_number(num)
        if board.check_win():
            return boards[idx]

called, boards = get_bingo_game_info(lines)
print(get_final_game_state(called, boards))


