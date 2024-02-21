
import math

n, m, k = map(int, input().split())

train_data = []
balls = [[0 for j in range(1001)] for i in range(1001)]

for i in range(n):
    x, y, label = map(int, input().split())
    train_data.append((x, y, label))

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def move_ball(x, y, direction):
    if direction == 0:
        y += 2
    elif direction == 1:
        x += 2
    elif direction == 3:
        y -= 2
    elif direction == 4:
        x -= 2
    return x, y

for i in range(m):
    x, y, direction = map(int, input().split())
    if balls[x][y] != 0:
        x, y = move_ball(x, y, direction)
        while balls[x][y] != 0:
            if x < 1 or x > 1000 or y < 1 or y > 1000:
                break
            x, y = move_ball(x, y, direction)
    distances = []
    for j in range(n):
        distance = euclidean_distance((x, y), train_data[j][:2])
        distances.append((distance, train_data[j][2]))
    distances.sort()
    labels = {}
    for d, l in distances[:k]:
        if l in labels:
            labels[l] += 1
        else:
            labels[l] = 1
    max_count = max(labels.values())
    for l in sorted(labels.keys()):
        if labels[l] == max_count:
            print(l, end=' ')
    balls[x][y] = i+1