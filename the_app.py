def fizzBuzz(x):
    if x <= 0:
        return None
    elif x%3 == 0 and x%5 == 0:
        return("FizzBuzz")
    elif x%3 == 0:
        return("Fizz")
    elif x%5 == 0:
        return("Buzz")
    else:
        return(x)
