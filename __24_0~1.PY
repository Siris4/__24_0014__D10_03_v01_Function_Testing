def subtract_prank(a, b):
    return a + b         #add 2 numbers together as a sum

result = subtract_prank(4, 8)
print(result)
# 12



def firs_and_last_name(first_name, last_name):
    return first_name, last_name

full_name = firs_and_last_name("Gavin", "M.")
print(full_name)


def get_numbers():
    return [1, 2, 3, 4, 7]    #returns a List

numbers = get_numbers()
print(numbers)


# Conditional Return:
def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b

result = divide(6, 2)
print(result)  # Output: 3.0

result = divide(6, 0)
print(result)  # Output: Division by zero is not allowed


#Returning from Loops:
def find_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num

numbers = [1, 3, 4, 7, 8]
result = find_even(numbers)
print(result)  # Output: 4


#Returning from Conditional Statements:
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(is_even(7))  # Output: False


#Early Exit in a Function: Finding a matching number within a List:
def find_target(numbers, target):
    for num in numbers:
        if num == target:
            return True
    return False

numbers = [1, 3, 5, 7, 9]
result = find_target(numbers, 5)
print(result)  # Output: True


# Returning from Recursive Functions:
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

result = factorial(5)
print(result)  # Output: 120


#Returning Hello, then None:
def say_hello():
    print("Hello")

result = say_hello()
print(result)
# Hello
# None


# Returning Early with No Value:
def process_data(data):
    if not data:
        return  # No return value, exits the function

    # Process data here

result = process_data([])
print(result)  # Output: None



# Returning a Function:
def greeting(message):
    def greet(name):
        return f"{message}, {name}"

    return greet

say_hello = greeting("Hello")
print(say_hello("Alice"))  # Output: Hello, Alice



# Returning a Lambda Function:
def double_function(factor):
    return lambda x: x * factor

double = double_function(2)
result = double(4)
print(result)  # Output: 8
