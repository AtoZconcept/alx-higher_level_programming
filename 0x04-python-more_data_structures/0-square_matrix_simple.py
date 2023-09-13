#!/usr/bin/puthon3

def square_matrix_simple(matrix=[]):
    if not matrix:
        return matrix
    new = []
    for row in matrix:
        new.append(list(map(lambda n: n**2, row)))
    return new
