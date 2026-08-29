import random


def task1():
    print("Задача 1 - Калькулятор")
    print("Введите два числа и операцию (+, -, *, /):")
    num1 = float(input("Первое число: "))
    num2 = float(input("Второе число: "))
    operation = input("Операция: ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Ошибка: Деление на ноль!")
            return
        result = num1 / num2
    else:
        print("Неверная операция!")
        return

    print(f"Результат: {result}")

def task2():
    print("Задача 2 - Генератор случайных чисел")
    lower = int(input("Введите нижнюю границу: "))
    upper = int(input("Введите верхнюю границу: "))
    random_number = random.randint(lower, upper)
    print(f"Случайное число между {lower} и {upper}:")

    while True:
        source = float(input("Введите число для проверки: "))
        if source > random_number:
            print("Меньше")
        elif source < random_number:
            print("Больше")
        else:
            print("Поздравляем! Вы угадали число.")
            break
    

def task3():
    ...
def task4():
    ...

def task5():
    ...
    

def task6():
    ...

def task7():
    ...

def task8():
    ...

def task8():
    ...

def task9():
    ...

def task10():
    ...






def main():
    tasks = {
        "1": task1,
        "2": task2,
        "3": task3,
        "4": task4,
        "5": task5,
        "6": task6,
        "7": task7,
        "8": task8,
        "9": task9,
        "10": task10,
    }

    while True:
        print("\n===== PYTHON TASKS =====")

        for number in tasks:
            print(f"{number}. Задача {number}")

        print("0. Выход")

        choice = input("\nВыберите задачу: ")

        if choice == "0":
            print("Выход...")
            break

        if choice in tasks:
            tasks[choice]()
        else:
            print("Такой задачи нет.")


main()



