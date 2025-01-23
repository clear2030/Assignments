import random
print('Write a program to compare 2 hard coded numbers with an IF/ELSE')

# -------------------------------------------
# Add Your Comments Here
# I used if and else statements along with boolean operations to evaluate and print whether the two codes were equal.
# I used the input function and the int function to take user input for the user_input variable, and cast it to an int type.
# I used the random.randint function to generate a random number between 0 and 20 for the number_2_guess variable.
# I used an elif statement to check whether the user_guess was within 1 of the nunber_2_guess and print something if it was.
# -------------------------------------------

print("This is a Guessing Game")
print("Ready to play?")

number_2_guess = random.randint(0,20)
#print(number_2_guess)

user_guess= int(input("input user guess: "))

#print(type(user_guess))
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
