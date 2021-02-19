    # Create a program that simulates an ATM. Implement the following functions
    # 1. Deposit
    # 2. Withdraw
    # 3. Account balance
    # 4. Exit

def atm():
    balance = 0
    is_active = True

    main_menu = ["\n\n--------------------------",
                 "What would you like to do?",
                 "0 - Exit",
                 "1 - Deposit",
                 "2 - Widthdraw",
                 "3 - Account balance"]
    
    while is_active:
        action = 4
        
        for line in main_menu:
            print(line)

        user_input = input("What would you like to do? ")

        if not user_input.isdigit():
            print("Invalid input! Try again")
            continue
        else:
            action = int(user_input)
        
        if (action < 0 or action > 3):
            print("This operatin is not supported! Try again")

        if action == 0:
            is_active = False
            break
        elif action == 1:
            balance += deposit()
        elif action == 2:
            balance -= withdraw(balance)
        elif action == 3:
            print_balance(balance)
        else:
            continue

def deposit():
    deposit = 0
    user_input = input("Enter the amount you want to deposit ")

    if user_input.isdigit():
        deposit = int(user_input)
    else:
        print("Not a valid deposit! Returned to main menu.")
    
    return deposit

def withdraw(balance):
    withdraw = 0
    user_input = input("Enter the amount you want to withdraw ")

    if user_input.isdigit():
        if (int(user_input) <= balance):
            withdraw = int(user_input)
        else:
            print("Not enough money! Returned to main menu.")
    else:
        print("Not a valid withdraw! Returned to main menu.")
    
    return withdraw

def print_balance(balance):
    print("\n\nYour current balance is: " + str(balance))
