def number_guessing_game():
    import random

    print("Welcome to Guessing Number Game:)")
    print("Please enter a number between 1 to 100:")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            user_input = int(input("Enter the number: "))
            
            if user_input < 1 or user_input > 100:
                print("Invalid number, please enter between 1 to 100!!!")
                continue

            attempts += 1

            if user_input > secret_number:
                print("Your number is greater!")
            elif user_input < secret_number:
                print("Your number is lesser!")
            else:
                print("Your number is correct congratulations!")
                print(f"You guessed it in {attempts} attempts!")
                break

        except ValueError:
            print("Invalid input! Please enter numbers only.")

number_guessing_game()