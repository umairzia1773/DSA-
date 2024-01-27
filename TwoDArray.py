class TwoDArray:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [0] * (rows * cols)

    def map_index(self, row, col):
        return row * self.cols + col

    def set_data(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[self.map_index(row, col)] = value
        else:
            print("Invalid row or column index.")

    def get_data(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.data[self.map_index(row, col)]
        else:
            print("Invalid row or column index.")
            return None

    def display(self):
        print("[", end="")
        for row in range(self.rows):
            if row != 0:
                print()
            print("[", end="")
            for col in range(self.cols):
                print(self.get_data(row, col), end="")
                if col < self.cols - 1:
                    print(",", end="")
            print("]", end="")
        print("]")
