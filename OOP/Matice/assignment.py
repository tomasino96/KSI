class Matrix:
    def __init__(self, array: list[list[int | float]]) -> None:
        for row in array:
            if len(row) != len(array[0]):
                raise Exception("Matrix Error: invalid number of elements")
            
        self.data = array
        self.num_of_rows = len(array)
        self.num_of_columns = len(array[0])

    @staticmethod
    def zero_matrix(height: int, width: int) -> 'Matrix':
        matrix = []
        for _ in range(height):
            row = []
            for _ in range(width):
                row.append(0)
            matrix.append(row)

        return Matrix(matrix)

    @staticmethod
    def identity_matrix(side: int) -> 'Matrix':
        matrix = []
        diagonal = 0
        for _ in range(side):
            row = []
            for i in range(side):
                if i == diagonal:
                    row.append(1)
                else:
                    row.append(0)
            diagonal += 1
            matrix.append(row)

        return Matrix(matrix)

    def __str__(self) -> str:
        result = []
        for row in self.data:
            row_str = ""
            for element in row:
                row_str += str(element) + " "
            row_str = row_str.strip() 
            # Removes space after string https://www.digitalocean.com/community/tutorials/python-remove-spaces-from-string
            result.append(row_str)

        return "\n".join(result) + "\n"

    def __getitem__(self, tup: tuple[int, int]) -> int | float:
        if not isinstance(tup, tuple):
            raise Exception("Matrix Error: must be a tuple of two integers")

        row, column = tup

        if row < 1 or row > self.num_of_rows or column < 1 or column > self.num_of_columns:
            raise Exception(f"Matrix Error: tuple ({row}, {column}) is out of bounds")

        return self.data[row - 1][column - 1]

    def __setitem__(self, tup: tuple[int, int], new_value: int | float) -> None:
        if not isinstance(tup, tuple):
            raise Exception("Matrix Error: must be a tuple of two integers")

        row, column = tup

        if row < 1 or row > self.num_of_rows or column < 1 or column > self.num_of_columns:
            raise Exception(f"Matrix Error: tuple ({row}, {column}) is out of bounds")
        
        self.data[row - 1][column - 1] = new_value

    def transposition(self) -> 'Matrix':
        transposed_matrix = []

        for column in range(self.num_of_columns):
            transposed_row = []
            for row in self.data:
                transposed_row.append(row[column])
            transposed_matrix.append(transposed_row)
        
        return Matrix(transposed_matrix)

    def is_squared(self) -> bool:
        if self.num_of_rows == self.num_of_columns:
            return True

        return False

    def is_symetrical(self) -> bool:
        squared = self.is_squared()
        if not squared:
            return False

        for row in range(self.num_of_rows):
            for column in range(row + 1, self.num_of_columns):
                if self.data[row][column] != self.data[column][row]:
                    return False

        return True

    def is_antisymetrical(self) -> bool:
        squared = self.is_squared()
        if not squared:
            return False
        
        for row in range(self.num_of_rows):
            if self.data[row][row] != 0:
                return False

            for column in range(row + 1, self.num_of_columns):
                if self.data[row][column] != -(self.data[column][row]):
                    return False

        return True

    def is_triangular(self) -> bool:
        squared = self.is_squared()
        if not squared:
            return False

        upper = True
        lower = True

        for row in range(self.num_of_rows):
            for column in range(row + 1, self.num_of_columns):
                if self.data[row][column] != 0:
                    upper = False

                if self.data[column][row] != 0:
                    lower = False
        
        return upper or lower

    def is_diagonal(self) -> bool:
        squared = self.is_squared()
        if not squared:
            return False
        
        for row in range(self.num_of_rows):
            for column in range(row + 1, self.num_of_columns):
                if self.data[row][column] != 0:
                    return False

                if self.data[column][row] != 0:
                    return False

        return True
        
    def get_info(self) -> tuple[tuple[int, int], bool, bool, bool, bool, bool]:
        size = self.num_of_rows, self.num_of_columns
        squared = self.is_squared()
        symetrical = self.is_symetrical()
        antisymetrical = self.is_antisymetrical()
        triangular = self.is_triangular()
        diagonal = self.is_diagonal()
        
        return size, squared, symetrical, antisymetrical, triangular, diagonal


    def __eq__(self, other_matrix: object) -> bool:
        if not isinstance(other_matrix, Matrix):
            return False

        if self.num_of_rows != other_matrix.num_of_rows or self.num_of_columns != other_matrix.num_of_columns:
            return False

        for row in range(self.num_of_rows):
            if self.data[row] != other_matrix.data[row]:
                return False

        return True

    def __ne__(self, other_matrix: object) -> bool:
        if not self == other_matrix:
            return True

        return False

    def __add__(self, other_matrix: 'Matrix') -> 'Matrix':
        if self.num_of_rows != other_matrix.num_of_rows or self.num_of_columns != other_matrix.num_of_columns:
            raise Exception(f"Matrix Error: dimensions does not match")

        new_matrix = []

        for row in range(self.num_of_rows):
            new_row = []
            for column in range(self.num_of_columns):
                element = self.data[row][column]
                other_element = other_matrix.data[row][column]
                new_row.append(element + other_element)
            new_matrix.append(new_row)

        return Matrix(new_matrix)

    def __sub__(self, other_matrix: 'Matrix') -> 'Matrix':
        if self.num_of_rows != other_matrix.num_of_rows or self.num_of_columns != other_matrix.num_of_columns:
            raise Exception(f"Matrix Error: dimensions does not match")

        new_matrix = []

        for row in range(self.num_of_rows):
            new_row = []
            for column in range(self.num_of_columns):
                element = self.data[row][column]
                other_element = other_matrix.data[row][column]
                new_row.append(element - other_element)
            new_matrix.append(new_row)

        return Matrix(new_matrix)

    def __mul__(self, other_matrix: 'Matrix') -> 'Matrix':
        if self.num_of_columns != other_matrix.num_of_rows:
            raise Exception(f"Matrix Error: dimensions does not match, number of columns in first matrix must match number of rows in second matrix")

        new_matrix = []

        for i in range(self.num_of_rows):
            new_row = []
            for j in range(other_matrix.num_of_columns):
                new_element = 0
                for k in range(self.num_of_columns):
                    new_element += self.data[i][k] * other_matrix.data[k][j]
                new_row.append(new_element)
            new_matrix.append(new_row)

        return Matrix(new_matrix)

    def __rmul__(self, constant: int | float) -> 'Matrix':
        new_matrix = []

        for row in range(self.num_of_rows):
            new_row = []
            for column in range(self.num_of_columns):
                element = self.data[row][column]
                new_element = element * constant
                new_row.append(new_element)
            new_matrix.append(new_row)
        return Matrix(new_matrix)

    def determinant(self) -> int | float:
        """ Vrati determinant matice """
        pass

    def inverse(self) -> 'Matrix':
        """ Vrati inverzni matici """
        pass


class Matrix3D:
    def __init__(self, array: list[list[list[int]]]) -> None:
        """ Vytvoreni matice 3D"""
        pass

    def __eq__(self, other_matrix: object) -> bool:
        """ Pretizeni operatoru ==; tzn jestli se dve 3D matice rovnaji """
        pass

    def __ne__(self, other_matrix: object) -> bool:
        """ Pretizeni operatoru !=; tzn jestli jsou dve 3D matice rozdilne """
        pass

    def determinant_3d(self) -> int:
        """ Vrati determinant 3D matice """
        pass


A = Matrix([[1, 2, 3], [4, 5, 6]])

zero_mat = Matrix.zero_matrix(3, 3)

identity_mat = Matrix.identity_matrix(5)

B = Matrix([[-1, 3, -3, 1], [2, 0, 0, 5], [1, 5, 7, -10]])

C = Matrix.transposition(B)

D = Matrix([[7, 3], [0, 1]])
E = Matrix([[4, 5], [2, 3]])

F = 1000 * D
print(F)

G = A * B
print(G)