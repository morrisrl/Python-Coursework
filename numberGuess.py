import random
print("Welcome to Guess My Number!")
print()
print("I'm thinking of a number between 1 and 100.Try to guess it in as few attempts as possible.")

number = random.randrange(1, 100)
user_input = eval(input("Take a guess."))
attempt = 0
while True:
    if user_input < number:
        print("Lower...")
    attempt += 1
    elif user_input > number:
        print("Higher...")
    attempt+=1
    elif user_input == number:
        print("You guessed it! The number was", number)
        print("And it only took you", sum(attempt), "times.")
    break
