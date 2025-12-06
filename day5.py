def horrible_fresh(ranges, numbers):
    fresh_ids = set()
    for n_range in ranges:
        left, right = n_range.split('-')
        start, stop = int(left), int(right)
        for i in range(start, stop + 1):
            fresh_ids.add(i)

    count = 0
    for number in numbers:
        num = int(number)
        if num in fresh_ids:
            count += 1
    return count

def range_string_to_tuple(range_str):
    left, right = range_str.split('-')
    start, stop = int(left), int(right)
    return start, stop

def fresh(ranges, numbers):
    range_list = list(map(range_string_to_tuple , ranges))
    numbers_list = list(map(int, numbers))

    range_list.sort()
    numbers_list.sort()

    count = 0
    range_index = 0
    number_index = 0

    while range_index < len(range_list) and number_index < len(numbers_list):
        current_range = range_list[range_index]
        current_number = numbers_list[number_index]

        if current_range[0] <= current_number <= current_range[1]:
            count += 1
            number_index += 1
        elif current_number < current_range[0]:
            number_index += 1
        else:  # current_number > current_range[1]
            range_index += 1

    return count

def fresh2(ranges):
    range_list = list(map(range_string_to_tuple , ranges))
    range_list.sort()
    count = 0

    new_ranges = []
    current_range = range_list[0]
    for i in range(1, len(range_list)):
        new_range = range_list[i]
        if current_range[1] >= new_range[0]:
            current_range = current_range[0], max(current_range[1], new_range[1])
        else:
            new_ranges.append(current_range)
            current_range = new_range
    new_ranges.append(current_range)

    for r in new_ranges:
        count += r[1] - r[0] + 1

    print(new_ranges)

    return count

def main():
    with open('input/5.txt', 'r') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    divider = lines.index('')
    ranges = lines[:divider]
    numbers = lines[divider+1:]

    print(fresh2(ranges))




if __name__ == '__main__':
    main()
