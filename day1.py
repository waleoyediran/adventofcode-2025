def main():
    with open('day1/test.txt', 'r') as file:
        lines = file.readlines()
    current = 50
    count = 0

    for line in lines:
        ch = line[0]
        original_number = int(line[1:])

        number = original_number % 100
        rotations = original_number // 100
        count += rotations

        if ch == 'L':
            current -= number
        else:
            current += number

        if current < 0:
            current += 100
            count += 1
        elif current >= 100:
            current -= 100
            count += 1
        # elif current == 0:
        #     count += 1    # I'm not sure why this doesnt count

    print(count)


def zero_hits_from_file():
    with open("day1/test.txt", "r") as file:
        lines = [line.rstrip("\n") for line in file]


    startpoint = 50
    count = 0

    for line in lines:
        if not line:
            continue
        direction = line[0].upper()
        distance = int(line[1:])

        startnumber = distance % 100
        rotations = distance // 100

        if direction == 'L':
            startpoint -= startnumber
        elif direction == 'R':
            startpoint += startnumber

        if startpoint < 0:
            startpoint += 100
            rotations += 1
        elif startpoint >= 100:
            startpoint -= 100
            rotations += 1

        count += rotations

    print(count)

if __name__ == '__main__':
    # main()
    zero_hits_from_file()
