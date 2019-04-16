number = int(input("1つの自然数を入れてね: "))


def fizzbuzz_convert(number):
    if number % 15 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)


result = fizzbuzz_convert(1)
print(result)

result = fizzbuzz_convert(3)
print(result)

fizzbuzz_convert(100)
