#importing random package
import random
#writing loop so that the user can play as much times he want
while True:
#we need a variable to store the random number
    number = random.randint(1, 100)
#we are using exception handling to avoid the error while giving inputs
    try:
        total_rounds = int(input("Enter number of attempts Dude: "))
        #we are writing this so that to avoid negative or 0 rounds
        if total_rounds <= 0:
            print("Dude,Enter a positive number.")
            continue
    #if user enter an string in-case of number
    except:
        print("Dude it's anInvalid input.")
        continue
    #we are writing this so that we can store total rounds in rounds_left
    rounds_left = total_rounds
    #at first guessed is false if he guessed correctly then it will change to true
    guessed = False
    #cheking weather rounds left is greater than zero if its equal to zero it will come out
    while rounds_left > 0:
        #here we are writing exception handling so that user enters a valid input
        try:
            guess = int(input(f"Enter your guess (Attempts left: {rounds_left}): "))
        #this will catch the error if user enters a string
        except:
            print("Enter a valid number.")
            continue
        #if guessed number is too high than the random number
        if guess > number:
            print("Too High Dude,Try again..")
        #if guessed number is too low than the random number
        elif guess < number:
            print("Too Low Dude,Try again...")
        #if guessed number is equal to the random number
        else:
            print(f"Congratulations Dude it's Correct! The number was {number}")
            guessed = True
            break
        #everytime user enters his guess rounds will be decreased
        rounds_left -= 1
    #if he guessed correctly
    if guessed:
        #if he guessed the anwser above half of the rounds
        if rounds_left >= total_rounds // 2:
            print("Great job! You guessed within half rounds...")
        #if he guessed the answer below half of the rounds
        else:
            print("Good job!")
    #if he didn't guessed corretly and rounds has been completed
    else:
        print(f"Game Over!,Dude Try Again after sometime The number was {number}")
    #we are asking the user if he want's to play again or not
    choice = input("Play again? (yes/no): ").lower()
    #if he dont want to play again then we will exit the program
    if choice != "yes":
        print("Exiting the Program have a good day....")
        break