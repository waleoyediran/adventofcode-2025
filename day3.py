def jolt(line):
    N = len(line)
    line = list(map(int, list(line)))
    candidate_i = N-2
    for i in reversed(range(N-2)):
        if line[i] >= line[candidate_i]:
            candidate_i = i
    return (line[candidate_i] * 10) + max(line[candidate_i+1:])
def jolt2(line):
    N = len(line)
    line = list(map(int, list(line)))

    result = []
    curr = line
    for i in reversed(range(12)):
        if len(curr) <= i+1:
            result.append(''.join(map(str,curr)))
            break

        num = max(curr[:-i]) if i > 0 else max(curr)
        result.append(str(num))
        index = curr.index(num)
        curr = curr[index+1:]

    return int(''.join(result))

def main():
    with open('input/3.txt', 'r') as file:
        lines = file.readlines()
    result = 0
    for line in lines:
        number = jolt2(line.strip())
        result += number
    print(result)

if __name__ == '__main__':
    main()
