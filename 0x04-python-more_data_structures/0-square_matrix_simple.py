#!/usr/bin/puthon3

def square_matrix_simple(matrix=[]):
    new_mat = []
    for row in matrix:
        new_mat.append([x ** 2 for x in row])
    return new_mat
