import random

# -------------------------------------------
# Add Your Comments Here
# I used if and else statements along with boolean operations to evaluate and print whether the two codes were equal.
# I used the input function and the int function to take user input for the user_input variable, and cast it to an int type.
# I used the try and except statements to check if the input is a int value. If it isn't, it'll run the except code and won't run the full guessing game.
# -------------------------------------------

print("This is a Guessing Game")
print("Ready to play?")

number_2_guess = random.randint(0,20)
#print(number_2_guess)

# user_guess = 5 

try:
    user_guess= input("input user guess: ")
    user_guess = int(user_guess)
except:
    print(user_guess, "is not a number.")
else:
    print("Thanks for guessing with the number", user_guess)
    print(type(user_guess))
    print(user_guess)

    if user_guess==number_2_guess:
        print("Good Guess, you are a Winner")
        print(user_guess, "is equal to", number_2_guess) 

    elif ((user_guess+1)==number_2_guess) or ((user_guess-1)==number_2_guess):
        print("Close but no Cigar")
        print(user_guess, "is one number away from", number_2_guess)

    else:
        print("Better Luck Next Time")
        print(user_guess, "is NOT equal to", number_2_guess)

print("All Done!")
