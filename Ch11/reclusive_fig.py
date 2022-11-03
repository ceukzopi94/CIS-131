
def factorial(number):
    """Return factorial of number."""
    print(number)

    if number <= 1:
        return 1

    return number * factorial(number - 1)

for i in range(11):
    print(f'{i}! = {factorial(i)}')