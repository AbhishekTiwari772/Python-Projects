# FizzBuzz Exercise in Python

def fizzBuzz(x):
    if x%3 == 0 and x%5==0:
        print("FizzBuzz")
    elif x%3==0:
        print("Fizz")
    elif x%5==0:
        print("Buzz")
    else:
        print(x)


num = int(input("Enter a number: "))

fizzBuzz(num)
