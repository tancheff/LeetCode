import math

matrix = [[1,5],[7,3],[3,5]]

smallest_possible_num = -math.inf

richest = smallest_possible_num

for list in matrix:
    if sum(list) >= richest:
        richest = sum(list)

print(richest)

print(matrix[0][0])
print(matrix[0][1])

print([sum(list) for list in matrix])
print(max([sum(list) for list in matrix]))