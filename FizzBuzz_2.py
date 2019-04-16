number = int(input("1つの自然数を入れてね: "))


def fizzbuzz_convert(number):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(str(number))


fizzbuzz_convert(1)
fizzbuzz_convert(2)
fizzbuzz_convert(3)
fizzbuzz_convert(4)
fizzbuzz_convert(5)
fizzbuzz_convert(6)
fizzbuzz_convert(7)
fizzbuzz_convert(8)
fizzbuzz_convert(11)
fizzbuzz_convert(24)
fizzbuzz_convert(100)
