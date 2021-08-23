from itertools import zip_longest


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
         if len(self.matrix[0]) != len(self.matrix[1]): #Сделал быстро, знаю что могут на 3 списке сделать больше
             print('ValueError')
         else:
             for i in range(len(self.matrix)):
                 for j in range(len(self.matrix[0])):
                     print(self.matrix[i][j], end=' ')
                 print()
         print()

    def __add__(self, other):
        spisok_1 = []
        spisok_2 = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                spisok_1.append(self.matrix[i][j])
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                spisok_2.append(self.matrix[i][j])
        spisok_sum = [x+y for x, y in zip_longest(spisok_1, spisok_2)]
        for i in range(len(spisok_sum)):
            if i%2:
                print(spisok_sum[i], end=' ')
                print()
            else:
                print(spisok_sum[i], end=' ')




matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])
matrix_1.__str__()
matrix_2.__str__()
matrix_1 + matrix_2