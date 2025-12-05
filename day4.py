def print_grid(grid):
    for row in grid:
        print(''.join(row))

def count_grid(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    for row in range(rows):
        for col in range(cols):
            ch = grid[row][col]
            if ch == '.':
                continue
            nearby_tissue_count = 0
            for d_row, d_col in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
                n_row, n_col = row + d_row, col + d_col
                if 0 <= n_row < rows and 0 <= n_col < cols:
                    if grid[n_row][n_col] == '@':
                        nearby_tissue_count += 1
            if nearby_tissue_count < 4:
                count += 1
    return count

def explore_direction(grid, row, col):
    rows, cols = len(grid), len(grid[0])
    nearby_tissue_count = 0
    nearby_tissues = []
    for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        n_row, n_col = row + d_row, col + d_col

        if 0 <= n_row < rows and 0 <= n_col < cols:
            if grid[n_row][n_col] == '@':
                nearby_tissue_count += 1
                nearby_tissues.append([n_row, n_col])
    count = 0
    if nearby_tissue_count < 4:
        count += 1
        grid[row][col] = '.'
        for n_row, n_col in nearby_tissues:
            explore_direction(grid, n_row, n_col)


def count_grid_2(grid):
    rows, cols = len(grid), len(grid[0])
    for row in range(rows):
        for col in range(cols):
            ch = grid[row][col]
            if ch == '.':
                continue
            explore_direction(grid, row, col)

    print_grid(grid)

def count_tissue(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    for row in range(rows):
        for col in range(cols):
            ch = grid[row][col]
            if ch == '@':
                count += 1
    return count

def main():
    with open('input/4.txt', 'r') as file:
        lines = file.readlines()
    grid = []
    for line in lines:
        grid.append(list(line.strip()))
    before = count_tissue(grid)
    count_grid_2(grid)
    after = count_tissue(grid)
    print(before - after)


if __name__ == '__main__':
    main()
