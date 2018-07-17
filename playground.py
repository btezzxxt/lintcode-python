# visited = [[0] * 5 for i in range(6)] 

# print(visited)

def calcHeightDown(matrix):
    m = len(matrix)
    n = len(matrix[0])
    for col in range(n):
        count = 0
        for i in range(m-1, -1, -1):
            if matrix[i][col] == 1:
                count += 1
            else:
                count = 0
            matrix[i][col] = count

# visited[3][0] = 1
# visited[4][0] = 1

# # print(visited)
# calcHeight(visited, 0)
# print(visited)
import os
fn = os.path.join(os.path.dirname(__file__), 'data_true_matrix')
txt = open(fn, 'r')
matrix = []
for raw in txt:
    raw = raw[2:-2]
    arr = raw.split('],[')
    for line in arr:
        arr2 = line.split(',')
        for i in range(len(arr2)):
            arr2[i] = 1
        matrix.append(arr2)

calcHeightDown(matrix)

