from TwoDArray import TwoDArray

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = TwoDArray(rows, cols)

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            print("Matrix dimensions must match for addition.")
            return None
        result = Matrix(self.rows, self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                result.data.set_data(row, col, self.data.get_data(row, col) + other.data.get_data(row, col))
        return result

    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            print("Matrix dimensions must match for subtraction.")
            return None
        result = Matrix(self.rows, self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                result.data.set_data(row, col, self.data.get_data(row, col) - other.data.get_data(row, col))
        return result

    def multiply(self, other):
        if self.cols != other.rows:
            print("Matrix dimensions are not suitable for multiplication.")
            return None
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                dot_product = 0
                for k in range(self.cols):
                    dot_product += self.data.get_data(i, k) * other.data.get_data(k, j)
                result.data.set_data(i, j, dot_product)
        return result

    def display(self):
        self.data.display()

