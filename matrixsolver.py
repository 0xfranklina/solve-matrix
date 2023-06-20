import numpy as np

# Задаем матрицу системы уравнений
matrix = np.array([[2, 1, -1, 2],
                   [3, 2, 1, -1],
                   [1, -2, 3, 2],
                   [4, 3, 2, 1]])

# Задаем вектор свободных членов
b = np.array([4, 1, 2, 3])

# Решаем систему уравнений
solution = np.linalg.solve(matrix, b)

# Выводим решение
print("Решение системы уравнений:")
for i, x in enumerate(solution):
    print(f"x{i+1} = {x}")
