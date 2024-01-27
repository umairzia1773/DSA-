from Matrix import Matrix

def main():

    matrix1 = Matrix(2, 3)
    matrix2 = Matrix(3, 2)
    matrix3 = Matrix(2, 3)

    matrix1.data.set_data(0, 0, 1)
    matrix1.data.set_data(0, 1, 2)
    matrix1.data.set_data(0, 2, 3)
    matrix1.data.set_data(1, 0, 4)
    matrix1.data.set_data(1, 1, 5)
    matrix1.data.set_data(1, 2, 6)

    matrix2.data.set_data(0, 0, 7)
    matrix2.data.set_data(0, 1, 8)
    matrix2.data.set_data(1, 0, 9)
    matrix2.data.set_data(1, 1, 10)
    matrix2.data.set_data(2, 0, 11)
    matrix2.data.set_data(2, 1, 12)


    matrix3.data.set_data(0, 0, 2)
    matrix3.data.set_data(0, 1, 4)
    matrix3.data.set_data(0, 2, 6)
    matrix3.data.set_data(1, 0, 8)
    matrix3.data.set_data(1, 1, 10)
    matrix3.data.set_data(1, 2, 12)


    print("Matrix 1:")
    print("========")
    matrix1.display()
    print()

    print("Matrix 2:")
    print("========")
    matrix2.display()
    print()

    print("Matrix 3:")
    print("========")
    matrix3.display()
    print()


    result_add = matrix1.add(matrix3)
    result_subtract = matrix1.subtract(matrix3)

    result_multiply = matrix1.multiply(matrix2)


    if result_add:
        print("Matrix 1 + Matrix 3:")
        print("=====================")
        result_add.display()
        print()

    if result_subtract:
        print("Matrix 1 - Matrix 3:")
        print("=====================")
        result_subtract.display()
        print()

    if result_multiply:
        print("Matrix 1 * Matrix 2:")
        print("=====================")
        result_multiply.display()
        print()

if __name__ == "__main__":
    main()
