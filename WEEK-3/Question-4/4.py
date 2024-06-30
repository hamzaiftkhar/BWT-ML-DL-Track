# Task 4: Iterators and Generators

# 1. Create an iterator class Countdown:

#   Logic: Implement an iterator that counts down from a given number to 1.
#   Approach:
#       Define the __init__ method to initialize the start value.
#       Implement the __iter__ and __next__ methods to return the next value and stop iteration when reaching 1.
# 
# 2. Implement a generator function fibonacci_generator:

#   Logic: Generate Fibonacci numbers up to a specified limit.
#   Approach:
#       Use a while loop to yield Fibonacci numbers until the limit is reached.
# 
# 
#3. Implement a generator function random_number_generator:

#   Logic: Yield a sequence of random numbers within a specified range.
#   Approach:
#       Use a for loop and random.randint to generate and yield random numbers.
# 
# 4. Write a Python program to demonstrate usage:

#   Logic: Use the Countdown iterator and the generator functions to show their functionality.
#   Approach:
#       Create instances of Countdown and use it in a for loop.
#       Call fibonacci_generator and random_number_generator in loops to print generated values.



import random

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.n = self.start
        return self

    def __next__(self):
        if self.n > 0:
            result = self.n
            self.n -= 1
            return result
        else:
            raise StopIteration

def fibonacci_generator(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

def random_number_generator(start, end, count):
    for _ in range(count):
        yield random.randint(start, end)

# Demonstrate Countdown
countdown = Countdown(10)
for num in countdown:
    print(num)

# Demonstrate fibonacci_generator
for num in fibonacci_generator(100):
    print(num)

# Demonstrate random_number_generator
for num in random_number_generator(1, 100, 10):
    print(num)
