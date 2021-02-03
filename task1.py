class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        m_in = ''
        m_n = ''
        for i in self.my_list:
            for p in i:
                m_n += f'{p}  '
            m_in += f'{m_n}\n'
            m_n = ''
        return m_in

    def __add__(self, other):
        m_in = []
        if len(self.my_list) == len(other.my_list):
            for i in range(len(self.my_list)):
                if len(self.my_list[0]) == len(other.my_list[0]):
                    m_n = [int(self.my_list[i][p]) + int(other.my_list[i][p]) for p in range(len(self.my_list[0]))]
                    m_in.append(m_n)
                else:
                    m_out = f'Не соблюдены условия сложения матриц'
                    return m_out
            m_out = Matrix(m_in)
        else:
            m_out = f'Не соблюдены условия сложения матриц'
            return m_out
        return m_out


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix_1)
matrix_2 = Matrix([[9, 8, 7, 1], [6, 5, 4, 1], [3, 2, 1, 1]])
print(matrix_2)
matrix_3 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print(matrix_3)
print(matrix_1 + matrix_2)
print(matrix_3 + matrix_1)
