import random

my_fibonacci = []
x = True
fib_int1 = 0

while x:
    try:
        fib_int1 = int(input("Please input an integer from 0 to 9: "))
        x = False
    except:
        print("That is not an integer.")
    if (fib_int1>9 or fib_int1<0):
        print("That is not an integer from 0 to 9.")
        x = True
        
print('The random number is', fib_int1, 'and this means you should check if you have your towel.')
fib_int2 = random.randint(1,20)
print("Random Number: ", fib_int2)

my_fibonacci.append(fib_int1)
my_fibonacci.append(fib_int2)
print(my_fibonacci)

for i in range(10):
    my_fibonacci.append(my_fibonacci[i] + my_fibonacci[i+1])
    print(my_fibonacci)
print(my_fibonacci)
print("done")
