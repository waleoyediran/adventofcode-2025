import collections
import math
from collections import deque

N,INPUT = 10, 'input/8.txt'
# N,INPUT = 1000, 'input/day8.txt'

class UnionFind:
    def __init__(self, n):
        # the constructor method takes the place of the makeset(x) procedure
        self.pi = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def union(self, u, v):
        """
            u & v are two vertices, each is in a different component
            build union of 2 components
            Be sure to maintain self.rank as needed to
            make sure your algorithm is optimal.
        """
        ru, rv = self.find(u), self.find(v)
        if ru == rv:
            return
        if self.rank[ru] > self.rank[rv]:
            self.pi[rv] = ru
        else:
            self.pi[ru] = rv
            if self.rank[ru] == self.rank[rv]: self.rank[rv] += 1


    def find(self, p):
        """
            find the root of the set containing the
            passed vertex p - Must use path compression!
        """
        if p != self.pi[p]: self.pi[p] = self.find(self.pi[p])
        return self.pi[p]

class JunctionBox:
    def __init__(self, coords):
        self.coords = coords
        self.neighbors = []

    def distance(self, other_coords):
        return math.dist(self.coords, other_coords.coords)

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def __repr__(self):
        return str(self.coords)

    def get_neighbors(self):
        sorted_neighbors = sorted(self.neighbors, key=lambda x: self.distance(x))
        return map(lambda n: (self.distance(n), n), sorted_neighbors)

def circuits(coords_list):
    junction_boxes = [JunctionBox(coords) for coords in coords_list]
    junction_boxes_index = {junction_box: idx for idx, junction_box in enumerate(junction_boxes)}
    for junction_box in junction_boxes:
        for other_box in junction_boxes:
            if junction_box != other_box:
                junction_box.add_neighbor(other_box)
    box_to_neighbors = dict()
    for junction_box in junction_boxes:
        box_to_neighbors[junction_box] = deque(junction_box.get_neighbors())

    union_find = UnionFind(len(junction_boxes))
    unions = 0
    while unions < N-1:
        print(unions, union_find.pi)
        list_of_closest = list(map(lambda value: tuple([value[1][0][0], value[1][0][1], value[0]]), box_to_neighbors.items()))
        closest = min(list_of_closest, key=lambda x: x[0])
        u,v = closest[1], closest[2]
        fu, fv = union_find.find(junction_boxes_index[u]), union_find.find(junction_boxes_index[v])

        if fu != fv:
            union_find.union(junction_boxes_index[u], junction_boxes_index[v])
            unions += 1
            # unions += 1
        box_to_neighbors[u].popleft()
        box_to_neighbors[v].popleft()

        # i += 1
    # s = collections.Counter(union_find.pi)
    s = collections.Counter(union_find.find(i) for i in range(len(junction_boxes)))
    print(s.most_common(3))
    return [count for _, count in s.most_common(3)]

def main():
    # with open('input/8.txt', 'r') as file:
    with open(INPUT, 'r') as file:
        lines = file.readlines()
    _input = []

    for line in lines:
        tokens = line.strip().split(',')
        tokens = [int(t) for t in tokens]
        _input.append(tokens)

    result = circuits(_input)
    product = 1
    for t in result:
        product *= t
    print(product)


if __name__ == '__main__':
    main()
