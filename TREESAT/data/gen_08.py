import random

random.seed(438239338)

N = 1000

edges = []
conds = []

# Complete random

for _ in range(20):
    base = random.randint(10000, 700000)
    perm = list(range(1, N+1))
    random.shuffle(perm)
    # Make sure a spanning tree exists
    for i in range(2, N+1):
        ind = len(edges) + 1
        edges.append([perm[random.randint(0, i-2)], perm[i-1], base + random.randint(-1000, 1000)])
        if i == 2:
            if ind != 0:
                conds.append([2, ind, ind - 1])
        else:
            conds.append([1, ind, ind - 1]);

for _ in range(70):
    perm = list(range(1, N+1))
    random.shuffle(perm)
    base = random.randint(10000, 700000)
    # Make sure a spanning tree probably doesn't exist
    for i in range(2, N+1):
        if i == 2 or random.randint(0, 1):
            ind = len(edges) + 1
            edges.append([perm[random.randint(0, i-2)], perm[i-1], base + random.randint(-1000, 1000)])
            if i == 2:
                if ind != 0:
                    conds.append([2, ind, ind - 1])
            else:
                conds.append([1, ind, ind - 1])



random.shuffle(conds)
print(N, len(edges), len(conds))
for e in edges:
    print(*e)
for c in conds:
    print(*c)
