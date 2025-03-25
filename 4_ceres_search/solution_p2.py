def calculate_x_mas_matches(grid, row_index, index):
    matches = 0
    if ((len(grid) - 1) - row_index) >= 2 and ((len(grid[row_index]) - 1) - index) >= 2:
        downward_cross_string = grid[row_index][index] + grid[row_index + 1][index + 1] + grid[row_index + 2][index + 2]
        upward_cross_string = grid[row_index + 2][index] + grid[row_index + 1][index + 1] + grid[row_index][index + 2]
        if downward_cross_string in ("MAS", "SAM") and upward_cross_string in ("MAS", "SAM"):
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
            if char == "M" or char == "S":
                total_matches += calculate_x_mas_matches(input_grid, row_index, index)
            index += 1
        row_index += 1
    print(total_matches)
        
main()