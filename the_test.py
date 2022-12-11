from the_app import fizzBuzz
def test_0():
    assert fizzBuzz(1) == 1
    assert fizzBuzz(2) == 2
    assert fizzBuzz(3) == "Fizz"
    assert fizzBuzz(5) == "Buzz"
    assert fizzBuzz(15) == "FizzBuzz"
    assert fizzBuzz(0) == None
