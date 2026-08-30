import random


def task1():
    print("Task 1 - Calculator")
    print("Enter two numbers and an operation (+, -, *, /):")
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    operation = input("Operation: ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Error: Division by zero!")
            return
        result = num1 / num2
    else:
        print("Invalid operation!")
        return

    print(f"Result: {result}")

def task2():
    print("Task 2 - Random Number Generator")
    lower = int(input("Enter the lower bound: "))
    upper = int(input("Enter the upper bound: "))
    random_number = random.randint(lower, upper)
    print(f"Random number between {lower} and {upper}:")

    while True:
        source = float(input("Enter a number to check: "))
        if source > random_number:
            print("Less")
        elif source < random_number:
            print("Greater")
        else:
            print("Congratulations! You guessed the number.")
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



