# This is a comment
"""
    This is a multi-
    line comment
"""
num1 = 42  # Variable decleration
num2 = 2.3  # Primitive number data type
boolean = True  # Primitive boolean data type
string = 'Hello World'  # Primitive String data type
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos',
                  'Cheese', 'Olives']  # Composite List initialization
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37,
          'is_balding': False}  # Composite Dictionary initialization
fruit = ('blueberry', 'strawberry', 'banana')  # Composite Tuple initialization
print(type(fruit))  # Type check
print(pizza_toppings[1])  # Composite List access value
pizza_toppings.append('Mushrooms')  # Composite List add value
print(person['name'])  # Composite Dictionary access value
person['name'] = 'George'  # Composite Dictionary change value
person['eye_color'] = 'blue'  # Composite Dictionary add value
print(fruit[2])  # Composite Tuple access value

if num1 > 45:  # Conditional: if
    print("It's greater")  # Log statement
else:  # Conditional: else
    print("It's lower")

if len(string) < 5:  # Length check
    print("It's a short word!")
elif len(string) > 15:  # Conditional: else if
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):
    print(x)
for x in range(2, 5):
    print(x)
for x in range(2, 10, 3):  # For loop start, stop, and increment
    print(x)
x = 0
while(x < 5):  # While loop start / stop conditional
    print(x)
    x += 1  # While loop increment

pizza_toppings.pop()  # Composite List delete value
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')  # Composite Dictionary delete value
print(person)

for topping in pizza_toppings:  # For loop sequence
    if topping == 'Pepperoni':
        continue  # For loop continue
    print('After 1st if statement')
    if topping == 'Olives':
        break  # For loop break


def print_hello_ten_times():
    for num in range(10):
        print('Hello')


print_hello_ten_times()


def print_hello_x_times(x):  # Function parameter
    for num in range(x):
        print('Hello')


print_hello_x_times(4)  # Function argument


def print_hello_x_or_ten_times(x=10):
    for num in range(x):
        print('Hello')


print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3) # NameError: name num3 is not defined
# num3 = 72
# fruit[0] = 'cranberry' # TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) # KeyError: 'favorite_team'
# print(pizza_toppings[7]) # IndexError: list index out of range
#   print(boolean) # IndentationError: unexpected indent
# fruit.append('raspberry') # AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) AttributeError: 'tuple' object has no attribute 'pop'
