import numpy as np

def create_matrix(rows, cols):
    matrix = []
    print(f"Введіть елементи для матриці розміром {rows}x{cols}:")
    for i in range(rows):
        row = []
        for j in range(cols):
            value = float(input(f"Елемент [{i+1}, {j+1}]"))
            row.append(value)
        matrix.append(row)
    return np.array(matrix)

def display_menu():
    print("\nберіть операцію:")
    print("1. додавання матриць")
    print("2. віднімання матрицб")
    print("3. множення мариць")
    print("4. множення матриць на число")
    print("5. вихід")


def matrix_calculator():
    rows = int(input("Введіть кількість рядків матриць: "))
    cols = int(input("Введіть кількість стовпців матриць: "))

    print("\nСтворення прешої мтриці")
    matrix1 = create_matrix(rows, cols)

    print("\nСтворення другої матриці")
    matrix2 = create_matrix(rows, cols)

    while True:
        display_menu()
        choise = input("Ваш вибір (1/2/3/4/5): ")

        if choise == '1':
            result = matrix1 + matrix2
            print("\nРезультат додавання:")
            print(result)

        elif choise == '2':
            result = matrix1 - matrix2
            print("\nРезультат відніиання")
            print(result)

        elif choise == '3':
            if rows == cols:
                result = np.dot(matrix1, matrix2)
                print("\nРезультат множення")
                print(result)
            else:
                print("Множення можлиле тільки для квадратних матриць.")

        elif choise == '4':
            num = int(input("Введіть число на яке ви хочете помножити матрицю: "))
            mut_num = input("Вибір матриці 1/2: ")
            if mut_num == '1':
                result = matrix1 * num
                print("\nРезультат множення на число")
                print(result)
            elif mut_num == '2':
                result = matrix2 * num
                print("\nРезультат множення на число")
                print(result)
            else:
                print("не правильно введено число")

        elif choise == '5':
            print("Вихід з програми")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

matrix_calculator()