import copy


class Matrix:

    def __init__(self,matrix):
        self.matrix = matrix
        self.verified = len(self.matrix[0])
        self.verification_value = self.matrix_verified()
        if self.verification_value is False:
            raise ValueError("Incorrect data for Matrix initialization: not equal lenght of lists")

    def matrix_verified(self):
        for i in range(len(self.matrix)):
            if len(self.matrix[i]) < self.verified or len(self.matrix[i]) > self.verified:
                return False
        return True

    def __str__(self):
        result = ''
        for i in range(len(self.matrix)):
            result = result  +'|'+ ' '.join(map(str,self.matrix[i]))+'|' + '\n'
        return result

    def __add__(self,other):
        try:
            if len(self.matrix) != len(other.matrix):
                raise ValueError("Incorrect dimensions for add method")
            summ_matrix = copy.deepcopy(self.matrix)
            for lst in range(len(self.matrix)):
                for i in range(len(self.matrix[lst])):
                    summ_matrix[lst][i] = self.matrix[lst][i] + other.matrix[lst][i]
            return Matrix(summ_matrix)
        except IndexError:
            raise ValueError("Incorrect dimensions for add method")




print('Первый пример')
m1 = Matrix([[11,2,3],[4,5,6],[117,8,9]])
m2 = Matrix([[1,1,1],[1,1,1],[1,1,1]])
print(m1)
print(m2)
m3 = m1 + m2
print(m3)
print(type(m3))

print()

print('Второй пример')
m1 = Matrix([[11,2],[4,5],[117,8]])
m2 = Matrix([[1,1],[1,1],[1,1]])
print(m1)
print(m2)
m3 = m1 + m2
print(m3)
print(type(m3))

