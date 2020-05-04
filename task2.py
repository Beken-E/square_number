"""
@Makers
Write a function square_number that
takes in a number and squares it.
"""
def square_number(number):
    a = number ** 2
    return a
#DO NOT remove lines below here, this is designed to test your code.
def test_square_number():
    assert square_number(2) == 4
    assert square_number(8) == 64
    assert square_number(10) == 100
    print("YOUR CODE IS CORRECT!")
test_square_number()