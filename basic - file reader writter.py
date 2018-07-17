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

import os
fn = os.path.join(os.path.dirname(__file__), 'data_true_matrix')
file1 = open(fn, 'r')
matrix = []
for raw in file1:
    raw = raw[2:-2]
    arr = raw.split('],[')
    for line in arr:
        arr2 = line.split(',')
        for i in range(len(arr2)):
            arr2[i] = 1
        matrix.append(arr2)
file1.close()

calcHeightDown(matrix)

fn = os.path.join(os.path.dirname(__file__), 'data_true_matrix2')
file2 = open(fn, 'w')
for arr in matrix:
  file2.write("%s\n" % arr)
file2.close()