class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = [[int(i) for i in e.split()]for e in matrix_string.split("\n")]
    def row(self, i):
        return self.matrix[i - 1]
    def column(self, i):
        return[r[i - 1] for r in self.matrix]