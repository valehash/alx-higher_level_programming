#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matric = [[]]
    for inner_list in matrix:
        for i, j in enumerate(inner_list):
            matric[i].append(j)
    for i in matric:
        for j in range(len(matric)):
            i[j]**=2
    return matric
