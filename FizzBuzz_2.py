def fizzbuzz_convert(number):
    if number % 15 == 0:
        return "FizzBuzz"

    if number % 3 == 0:
        return "Fizz"

    if number % 5 == 0:
        return "Buzz"

    return str(number)


for number in range(1, 101):
    print(fizzbuzz_convert(number))
