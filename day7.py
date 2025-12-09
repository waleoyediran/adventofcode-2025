def print_grid(grid):
    for row in grid:
        print(row)

def cound_splitters(grid, s_index):
    count = 0
    rows, cols = len(grid), len(grid[0])
    beams = {s_index}
    g_0 = [0]*cols
    g_0[s_index] = 1
    path_count_grid = [g_0]

    for row in range(1, rows):
        g_r = [n for n in path_count_grid[-1]]

        for beam_col in list(beams):
            if grid[row][beam_col] == '^':
                g_r[beam_col] = 0
                count += 1
                beams.remove(beam_col)
                new_beams = [i for i in [beam_col - 1, beam_col + 1] if 0 <= i < cols]
                for b in new_beams:
                    beams.add(b)
                    g_r[b] += path_count_grid[-1][beam_col]
        path_count_grid.append(g_r)
    return count, path_count_grid
    # return count


def main():
    with open('input/7.txt', 'r') as file:
        lines = file.readlines()
    grid = [list(line.strip()) for line in lines]

    s_index = grid[0].index('S')
    result, path_count_grid = cound_splitters(grid, s_index)

    # print_grid(path_count_grid)
    print(sum(path_count_grid[-1]))

if __name__ == '__main__':
    main()
