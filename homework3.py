
for i in range(1, 4):
    n = int(input("Введите число: "))
    
    # Вычисляем квадрат суммы
    square_of_sum = sum(range(1, n+1))**2
    
    # Вычисляем сумму квадратов
    sum_of_squares = sum([i**2 for i in range(1, n+1)])
    
    # Вычисляем разность
    difference = square_of_sum - sum_of_squares
    
    print("Разность квадрата суммы и суммы квадратов:", difference)


