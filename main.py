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
    print("Task 3 - String")
    str = input("Enter a string: ")
    print(f"Length of the string: {len(str)}")
    print(f"Number of words in the string: {len(str.split())}")
    print(f"Number of vowels in the string: {sum(1 for char in str.lower() if char in 'aeiou')}")
    print(f"The longest word in the string: {max(str.split(), key=len)}")
    print(f"Reversed string: {str[::-1]}")
def task4():
    shopping_list = []
    print("Task 4 - Shopping List")
    t_list = {
        "1": "Show list",
        "2": "Add item",
        "3": "Remove item",
        "4": "Clear list",
        "0": "Exit"
    }
    while True:
        print("\n===== SHOPPING LIST =====")
        for number, action in t_list.items():
            print(f"{number}. {action}")

        choice = input("\nEnter your choice: ")

        if choice == "0":
            print("Exiting...")
            break

        if choice == "1":
            print("Shopping List:")
            if len(shopping_list) == 0:
                print("The list is empty.")
            else:
                for item in shopping_list:
                    print(f"- {item}")
            
        elif choice == "2":
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} added to the list.")
        elif choice == "3":
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed from the list.")
            else:
                print(f"{item} not found in the list.")
        elif choice == "4":
            shopping_list.clear()
            print("Shopping list cleared.")
        else:
            print("Invalid choice.")
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
            print(f"{number}. Tasks {number}")

        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "0":
            print("Exiting...")
            break

        if choice in tasks:
            tasks[choice]()
        else:
            print("Invalid choice.")


main()



