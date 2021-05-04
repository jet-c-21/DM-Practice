import random
import math

# all_pairs = [(random.randint(1, 100), random.randint(1, 100)) for _ in range(10)]

all_pairs = [(98, 48), (46, 31), (78, 52), (56, 16), (39, 7), (92, 60), (66, 25), (72, 22), (78, 49), (2, 66)]


def get_dist(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


def get_closest_pair(point_seq: list):
    res = None
    min_dist = math.inf
    for i in range(1, len(point_seq)):
        for j in range(i):
            point_i = point_seq[i]
            point_j = point_seq[j]

            new_dist = get_dist(point_i, point_j)
            if new_dist < min_dist:
                min_dist = new_dist
                res = [point_i, point_j]

    return res


x = get_closest_pair(all_pairs)
print(x)
