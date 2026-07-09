

#can't devide by 0 zero division error
x = 10
y = 2
result = x/y
print("Result:", result)

#indentation error
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(numbers[i])

#indentation and syntax
def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area
radius = 5
print(calculate_area(radius))  

#indentation, syntax
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(is_even(4))
print(is_even(7))

#syntax and indentation
for i in range(5):
    print(i)

#indentaion,
def greet(name):
    return "Hello, {name}"
print(greet("Alice"))

#indentaton
numbers = [1, 2, 3, 4, 5]
total = 0
for number in numbers:
    total += number
print("Sum of numbers:", total)

#indentation
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n + 1)
        print(factorial(5))

#
name = input("Enter your name: ")
if name == "Alice" or "Bob":
        print("Hello, " + name)
else:
    print("Hello, stranger!")

#
def divide_numbers(x, y):
    if y == 0:
        return result
num1 = 10
num2 = 0
print(divide_numbers(num1, num2))