import random
def guessing_number_game():
    unique_number = random.randint(1, 100)
    print("The guess number is :",unique_number)
    print("Welcome to guessing number game")
    attempt = 0
    guess = None
    while guess != unique_number:
        guess = int(input("Entre the guess number :"))
        attempt+=1
        if unique_number > guess:
            print("This number is too high")
        elif unique_number < guess:
            print("This number is too low")
        else:
            print(f"🎉 Congratulations! You guessed the number {unique_number}.")
            print("Re-type the number again",guess)
            print("The total number of attempt in count",attempt)
