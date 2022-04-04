# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Dawson"
print('Hello', name, '!')  # with a comma
print('Hello ' + name + '!')  # with a +
# 3. print "Hello 42!" with the number in a variable
name = 42  # Answer to life, the universe, and everything.
print('Hello', name, '!')  # with a comma
# with a +	-- this one should give us an error!
print('Hello ' + str(name) + '!')
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "ramen"
fave_food2 = "pizza"
print('I love {} and {}!'.format(fave_food1, fave_food2))  # with .format()
print(f'I love {fave_food1} and {fave_food2}!')  # with an f string
