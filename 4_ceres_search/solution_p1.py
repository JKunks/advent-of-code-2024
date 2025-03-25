def calculate_downward_diagonal_matches(grid, row_index, index):
    matches = 0
    if ((len(grid) - 1) - row_index) >= 3 and ((len(grid[row_index]) - 1) - index) >= 3:
        forward_string = grid[row_index][index] + grid[row_index + 1][index + 1] + grid[row_index + 2][index + 2] + grid[row_index + 3][index + 3]
        if forward_string == "XMAS":
            matches += 1
    if row_index >= 3 and index >= 3:
        backward_string = grid[row_index][index] + grid[row_index - 1][index - 1] + grid[row_index - 2][index - 2] + grid[row_index - 3][index - 3]
        if backward_string == "XMAS":
            matches += 1
    return matches
        
def calculate_upward_diagonal_matches(grid, row_index, index):
    matches = 0
    if  row_index >= 3 and ((len(grid[row_index]) - 1) - index) >= 3:
        forward_string = grid[row_index][index] + grid[row_index - 1][index + 1] + grid[row_index - 2][index + 2] + grid[row_index - 3][index + 3]
        if forward_string == "XMAS":
            matches += 1
    if ((len(grid) - 1) - row_index) >= 3 and index >= 3:
        backward_string = grid[row_index][index] + grid[row_index + 1][index - 1] + grid[row_index + 2][index - 2] + grid[row_index + 3][index - 3]
        if backward_string == "XMAS":
            matches += 1
    return matches

        
def calculate_horizontal_matches(grid, row_index, index):
    matches = 0
    if ((len(grid[row_index]) - 1) - index) >= 3:
        forward_string = grid[row_index][index] + grid[row_index][index + 1] + grid[row_index][index + 2] + grid[row_index][index + 3]
        if forward_string == "XMAS":
            matches += 1
    if index >= 3:
        backward_string = grid[row_index][index] + grid[row_index][index - 1] + grid[row_index][index - 2] + grid[row_index][index - 3]
        if backward_string == "XMAS":
            matches += 1
    return matches

def calculate_vertical_matches(grid, row_index, index):
    matches = 0
    if row_index >= 3:
        forward_string = grid[row_index][index] + grid[row_index - 1][index] + grid[row_index - 2][index] + grid[row_index - 3][index]
        if forward_string == "XMAS":
            matches += 1
    if ((len(grid) - 1) - row_index) >= 3:
        backward_string = grid[row_index][index] + grid[row_index + 1][index] + grid[row_index + 2][index] + grid[row_index + 3][index]
        if backward_string == "XMAS":
            matches += 1
    return matches

def main():
    input = open("input.txt")
    input_grid = []
    for line in input:
        input_row = []
        stripped_line = line.strip()
        for char in stripped_line:
            input_row.append(char)
        input_grid.append(input_row)
    total_matches = 0
    row_index = 0
    for row in input_grid:
        index = 0
        for char in row:
            if char == "X":
                total_matches += calculate_downward_diagonal_matches(input_grid, row_index, index)
                total_matches += calculate_upward_diagonal_matches(input_grid, row_index, index)
                total_matches += calculate_horizontal_matches(input_grid, row_index, index)
                total_matches += calculate_vertical_matches(input_grid, row_index, index)
            index += 1
        row_index += 1
    print(total_matches)
        
main()