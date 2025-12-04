def next_repeating_number(number):
    number_string = str(number)
    digit_count = len(number_string)
    if digit_count % 2 == 0:
        #2L = digit_count
        L = digit_count // 2

        S_str = number_string[:L]
        S = int(S_str)

        power_of_10_plus_1 = 10 ** L + 1
        C = S * power_of_10_plus_1

        if C > number:
            return C

        S_prime = S + 1
        if len(str(S_prime)) == L:
            C_prime = S_prime * power_of_10_plus_1
            return C_prime

    L_prime = (digit_count // 2) + 1
    S_min = 10 ** (L_prime - 1)

    power_of_10_plus_1_prime = 10 ** L_prime + 1
    C_min = S_min * power_of_10_plus_1_prime

    return C_min

def next_repeating_number_2(number, N):
    # print(number, N)
    number_string = str(number)
    digit_count = len(number_string)
    if digit_count % N == 0:
        L = digit_count // N

        S_str = number_string[:L]
        S = int(S_str)

        C_str = S_str * max(L,2)
        C = int(C_str)

        if C > number:
            return C

        S_prime = S + 1
        if len(str(S_prime)) == L:
            C_prime = int(str(S_prime) * max(2,L))
            return C_prime


    L_prime = (digit_count // N) + 1
    S_min_str = str(10 ** (N-1))
    C_min = S_min_str * L_prime

    return int(C_min)


def main():
    with open('day2/test.txt', 'r') as file:
        line = file.readline()
    ranges = line.split(',')
    results = []
    for range in ranges:
        left, right = range.split('-')
        start,stop = int(left)-1,int(right)
        current = start
        while(True):
            next_number = next_repeating_number(current)
            if next_number <= stop:
                results.append(next_number)
            else:
                break
            current = next_number
    print(sum(results))

import re
pattern = re.compile(r'(\d+)(\1)+')

def main3():
    with open('day2/test.txt', 'r') as file:
        line = file.readline()
    ranges = line.split(',')
    results = set()
    for r in ranges:
        left, right = r.split('-')
        start, stop = int(left) - 1, int(right)

        for i in range(start, stop + 1):
            # check that i matches the regex pattern "(\d+)(\1)+"
            if pattern.fullmatch(str(i)):
                results.add(i)

    print(sum(results))




if __name__ == '__main__':
    main3()
