# Using an IF/ELSE write a program to have a hard coded variable <user_guess> 
# compared to a hard coded variable <number_2_guess> and print the results.
# You will use this source code in the next few program labs
print('Write a program to compare 2 hard coded numbers with an IF/ELSE')

# (instructions) Add your code here
#  1) Add some comments to describe your code
#     guess-01-YourFirstName-YourLastName.py


# -------------------------------------------
# Add Your Comments Here

# -------------------------------------------

# (instructions) Add your code here
#  2) Add some print() statements to describe to
#     the user what is happening and expected.

print("This is a Guessing Game")
print("Ready to play?")

# (instructions) Add your code here
#  3) Add a variable: number_2_guess = 7
#  4) print() the variable number_2_guess

number_2_guess = 7
print(number_2_guess)

# (instructions) Add your code here
# 5) Add a hard coded user guess
# user_guess = 5 

user_guess=5

# (instructions) Add your code here
#  6) print the type() of the user_guess to show it is an integer
#  7) print() the value of the user_guess variable

print(type(user_guess))
print(user_guess)

# (instructions) Add your code here
#  8) Add an IF statement to check if user_guess is equal to number_2_guess
#  9) If they are equal, print() something like 'Good Guess, you are a Winner'
# 10) also print() <user_guess> is equal to <number_2_guess>

if user_guess==number_2_guess:
    print("Good Guess, you are a Winner")
    print(user_guess, "is equal to", number_2_guess) 
  
# (instructions) Add your code here
# 11) Add an ELSE statement and in that block print() if they are not equal
# 12) print() something like 'Better Luck Next Time'
# 13) also print() <user_guess> is NOT equal to <number_2_guess>

else:
    print("Better Luck Next Time")
    print(user_guess, "is NOT equal to", number_2_guess)

# (instructions) Add your code here
# 14) End with a print() that says something like 'All Done!'

print("All Done!")
