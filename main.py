import random
import string

def get_average(ratings):
    if len(ratings) == 0:
        return 0
    return sum(ratings) / len(ratings)

def get_max(ratings):
    if len(ratings) == 0:
        return None
    return max(ratings)

def get_min(ratings):
    if len(ratings) == 0:
        return None
    return min(ratings)

def count_ratings(ratings, rating):
    count = 0
    for r in ratings:
        if r == rating:
            count += 1
    return count

def sort_ratings(ratings):
    return sorted(ratings)

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
    print(f"Number of vowels in the string: {sum(1 for char in str.lower() if char in 'aeiouy')}")
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
    print("Task 5 - Telephone Book")
    telephone_book = {}
    t_choice = {
        "1": "Add contact",
        "2": "Search contact",
        "3": "Remove contact",
        "4": "Show all contacts",
        "0": "Exit"
    }
    while True:
        print("\n===== TELEPHONE BOOK =====")
        for number, action in t_choice.items():
            print(f"{number}. {action}")

        choice = input("\nEnter your choice: ")

        if choice == "0":
            print("Exiting...")
            break

        if choice == "1":
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            telephone_book[name] = phone_number
            print(f"Contact {name} added.")
        elif choice == "2":
            name = input("Enter contact name to search: ")
            if name in telephone_book:
                print(f"{name}: {telephone_book[name]}")
            else:
                print(f"Contact {name} not found.")
        elif choice == "3":
            name = input("Enter contact name to remove: ")
            if name in telephone_book:
                del telephone_book[name]
                print(f"Contact {name} removed.")
            else:
                print(f"Contact {name} not found.")
        elif choice == "4":
            if len(telephone_book) == 0:
                print("No contacts found.")
            else:
                print("Contacts:")
                for name, phone_number in telephone_book.items():
                    print(f"{name}: {phone_number}")
        else:
            print("Invalid choice.")
    

def task6():
    print("Task 6 - Statistics ratings")
    ratings = []

    while True:
        try:
            rating = float(input("Enter a rating (0-10), or -1 to finish: "))
            if rating == -1:
                break
            elif 0 <= rating <= 10:
                ratings.append(rating)
            else:
                print("Invalid rating. Please enter a value between 0 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"Average rating: {get_average(ratings)}")
    print(f"Highest rating: {get_max(ratings)}")
    print(f"Lowest rating: {get_min(ratings)}")
    print(f"Number of 5-star ratings: {count_ratings(ratings, 5)}")
    print(f"Number of 2-star ratings: {count_ratings(ratings, 2)}")
    print(f"Sorted ratings: {sort_ratings(ratings)}")

class BankAccount:
    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def show_balance(self):
        print(f"Account owner: {self.owner}, Balance: {self.balance}")


def task7():
    print("Task 7 - Bank Account")
    owner = input("Enter account owner name: ")
    balance = float(input("Enter initial balance: "))

    account = BankAccount(balance, owner)

    b_choice = {
        "1": "Deposit",
        "2": "Withdraw",
        "3": "Show balance",
        "0": "Exit"
    }

    while True:
        print("\n===== BANK ACCOUNT =====")
        for number, action in b_choice.items():
            print(f"{number}. {action}")

        choice = input("\nEnter your choice: ")

        if choice == "0":
            print("Exiting...")
            break

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            account.show_balance()
        else:
            print("Invalid choice.")

def task8():
    print("Task 8 - Work with files")
    f_choice = {
        "1": "Add notes to file",
        "2": "Show notes from file",
        "3": "Clear notes from file",
        "0": "Exit"
    }
    while True:
        print("\n===== FILE OPERATIONS =====")
        for number, action in f_choice.items():
            print(f"{number}. {action}")

        choice = input("\nEnter your choice: ")

        if choice == "0":
            print("Exiting...")
            break

        if choice == "1":
            note = input("Enter a note to add: ")
            with open("notes.txt", "a") as file:
                file.write(note + "\n")
            print("Note added.")
        elif choice == "2":
            try:
                with open("notes.txt", "r") as file:
                    notes = file.readlines()
                    if notes:
                        print("Notes:")
                        for note in notes:
                            print(note.strip())
                    else:
                        print("No notes found.")
            except FileNotFoundError:
                print("No notes found.")
        elif choice == "3":
            with open("notes.txt", "w") as file:
                pass
            print("Notes cleared.")
        else:
            print("Invalid choice.")


def task9():
    print("Task 9 - Password manager")
    p_choice = {
        "1": "Add account",
        "2": "Find account",
        "3": "Show all accounts",
        "4": "Remove account",
        "5": "Generate random password",
        "0": "Exit"
    }
    while True:
        print("\n===== PASSWORD MANAGER =====")
        for number, action in p_choice.items():
            print(f"{number}. {action}")

        choice = input("\nEnter your choice: ")
        if choice == "0":
            print("Exiting...")
            break
        elif choice == "1":
            account = input("Enter account name: ")
            password = input("Enter password: ")
            with open("passwords.txt", "a") as file:
                file.write(f"{account}:{password}\n")
            print("Account added.")
        elif choice == "2":
            account = input("Enter account name to find: ")
            try:
                with open("passwords.txt", "r") as file:
                    for line in file:
                        if line.startswith(account + ":"):
                            print(f"Password for {account}: {line.split(':')[1].strip()}")
                            break
                    else:
                        print("Account not found.")
            except FileNotFoundError:
                print("No accounts found.")
        elif choice == "3":
            try:
                with open("passwords.txt", "r") as file:
                    accounts = file.readlines()
                    if accounts:
                        print("All accounts:")
                        for line in accounts:
                            print(line.strip())
                    else:
                        print("No accounts found.")
            except FileNotFoundError:
                print("No accounts found.")
        elif choice == "4":
            account = input("Enter account name to remove: ")
            found = False
            try:
                with open("passwords.txt", "r") as file:
                    lines = file.readlines()
                for line in lines:
                    if line.startswith(account + ":"):
                        found = True
                        break
                if found:
                    with open("passwords.txt", "w") as file:
                        for line in lines:
                            if not line.startswith(account + ":"):
                                file.write(line)
                    print("Account removed.")
                else:
                    print("Account not found.")
            except FileNotFoundError:
                print("No accounts found.")
        elif choice == "5":
            length = int(input("Enter desired password length: "))
            try:
                if length <= 0:
                    print("Password length must be positive.")
                    continue
                characters = string.ascii_letters + string.digits + string.punctuation
                password = ''.join(random.choice(characters) for _ in range(length))
                print(f"Generated password: {password}")
            except ValueError:
                print("Invalid input. Please enter a valid number.")


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20
        self.defense = 10
        self.gold = 20

    def attack(self):
        return self.attack_power

    def use_potion(self):
        self.health = min(100, self.health + 40)

    def show_stats(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Attack Power: {self.attack_power}")
        print(f"Defense: {self.defense}")
        print(f"Gold: {self.gold}")


class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self):
        return self.attack_power

def shop(player):
    print("Welcome to the shop!")
    print("1. Buy potion (10 gold)")
    print("2. Leave shop")
    choice = input("Enter your choice: ")
    if choice == "1":
        if player.gold >= 10:
            player.gold -= 10
            player.use_potion()
            print("You bought a potion and restored 40 health.")
            print(f"Remaining gold: {player.gold}")
            print(f"Current health: {player.health}")

        else:
            print("Not enough gold.")
    elif choice == "2":
        print("Leaving shop.")
    else:
        print("Invalid choice.")

def battle(player, enemy):
    print(f"A wild {enemy.name} appears!")
    while enemy.health > 0 and player.health > 0:
        action = input("Choose an action (attack - 1 /buy potion - 2): ")
        if action == "1":
            damage = player.attack()
            enemy.health -= damage
            print(f"You attacked the {enemy.name} for {damage} damage.")
        elif action == "2":
            shop(player)
        else:
            print("Invalid action.")

        if enemy.health > 0:
            damage = max(0, enemy.attack() - player.defense)
            player.health -= damage
            print(f"The {enemy.name} attacked you for {damage} damage.")

        player.show_stats()
        print(f"{enemy.name} Health: {enemy.health}")

    if player.health <= 0:
        print("You have been defeated!")
    else:
        print(f"You defeated the {enemy.name}!")
        print(f"You earned 20 gold.")
        player.gold += 20

def task10():
    print("Task 10- Mini RPG Game")
    player_name = input("Enter your character's name: ")
    player = Player(player_name)
    enemy1 = Enemy("Goblin", 50, 10)
    enemy2 = Enemy("Orc", 100, 20)
    enemy3 = Enemy("Dragon", 150, 30)
    g_choice = {
        "1": "Start game",
        "2": "Show player stats",
        "0": "Exit"
    }

    while True:
        print("\n===== MINI RPG GAME =====")
        for number, action in g_choice.items():
            print(f"{number}. {action}")

        choice = input("\nEnter your choice: ")

        if choice == "0":
            print("Exiting...")
            break
        elif choice == "1":
            print(f"Starting game with {player.name}!")
            battle(player, enemy1)
            print("Next battle!")
            battle(player, enemy2)
            print("Final battle!")
            battle(player, enemy3)
            print("Game over!")
            break
        elif choice == "2":
            player.show_stats()
        else:
            print("Invalid choice.")
     
        
        


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



