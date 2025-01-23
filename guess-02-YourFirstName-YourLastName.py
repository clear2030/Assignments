
# -------------------------------------------
# Add Your Comments Here
# I used if and else statements along with boolean operations to evaluate and print whether the two codes were equal.
# I used the input function and the int function to take user input for the user_input variable, and cast it to an int type.
# -------------------------------------------

print("This is a Guessing Game")
print("Ready to play?")

number_2_guess = 7
print(number_2_guess)

# user_guess = 5 

user_guess= int(input("input user guess: "))

print(type(user_guess))
print(user_guess)

if user_guess==number_2_guess:
    print("Good Guess, you are a Winner")
    print(user_guess, "is equal to", number_2_guess) 

else:
    print("Better Luck Next Time")
    print(user_guess, "is NOT equal to", number_2_guess)

print("All Done!")
