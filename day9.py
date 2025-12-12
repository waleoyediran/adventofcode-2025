from collections import defaultdict

def largest_rectangle_area(coords):
    dictionary = defaultdict(int)
    for coord in coords:
        for other_coord in coords:
            if coord != other_coord:
                area = (abs(coord[0] - other_coord[0]) + 1) * (abs(coord[1] - other_coord[1]) + 1)
                if area > dictionary[coord]:
                    dictionary[coord] = area

    largest_area = max(dictionary.values())
    return largest_area

def main():
    with open('input/9.txt', 'r') as file:
        lines = file.readlines()
    coords_list = [tuple(map(int, line.strip().split(','))) for line in lines]

    area = largest_rectangle_area(coords_list)
    print(area)



if __name__ == '__main__':
    main()
