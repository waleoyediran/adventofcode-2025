def print_grid(grid):
    for row in grid:
        print(row)

def multiply(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


def operations(grid):
    rows, cols = len(grid), len(grid[0])
    result = 0
    for col in range(cols):
        symbol = grid[-1][col]
        # print(rows)
        operands = []
        for row in range(rows-1):
            operands.append(grid[row][col])
        numbers = list(map(int, operands))

        if symbol == '+':
            operation = sum
        else:
            operation = multiply

        result += operation(numbers)

    return result

def get_operation_ranges(ops_row):
    ranges = dict()
    current_op, start = ops_row[0], 0
    for i in range(1,len(ops_row)):
        char = ops_row[i]
        if char == ' ': continue
        ranges[(start,i-2)] = current_op
        current_op, start = ops_row[i], i
    ranges[(start,len(ops_row)-1)] = current_op

    return ranges

def grid_transpose(grid):
    rows, cols = len(grid), len(grid[0])
    new_grid = []
    for col in range(cols):
        new_row = []
        for row in range(rows-1):
            new_row.append(grid[row][col])
        new_grid.append(''.join(new_row))
    return new_grid

def operations_2(grid):
    grid_transposed = grid_transpose(grid)
    print(grid_transposed)
    result = 0
    ops_row = grid[-1]

    op_ranges = get_operation_ranges(ops_row)
    print(op_ranges)
    for op_range, symbol in op_ranges.items():
        start, end = op_range
        if symbol == '+':
            operation = sum
        else:
            operation = multiply
        operands = []
        for i in range(start, end+1):
            operands.append(int(grid_transposed[i]))
        result += operation(operands)

    return result


def main():
    with open('input/day6.txt', 'r') as file:
        lines = file.readlines()
    grid = []
    for line in lines:
        grid.append(line.strip('\n'))

    result = operations_2(grid)
    print(result)




if __name__ == '__main__':
    main()
