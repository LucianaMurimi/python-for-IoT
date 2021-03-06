# Python is a dynamicaLly typed language
a = 60
print('type(60): ', type(a))

a=()
print('type(()): ', type(a))

print('1 is 2: ', 1 is 2)
# Python is case sensitive
print("'EMoS' == 'eMOS': ", 'EMoS: ' == 'eMOS')

#==============================================================================
#FOR Loops
# Counting from zero to twenty
for i in range(4):
    print(i)

# for i in range(initial, final, increment/decrement)
for i in range(1, 6, 2):
    print(i)
for i in range(6, 1, -2):
    print(i)

#==============================================================================
#importing libraries using the 'as' keyword
import keyword as kw
print(kw.kwlist)

for i in kw.kwlist:
    print(i)

#==============================================================================
x = 60
y = 40
# also, the variables above could be declared as:
#x,y = 60,40
z = 100 if x > y else 80
print('x = 60; y = 40; z = 100 if x > y else 80; therefore z = ', z);

#==============================================================================
i, j = 60, 40
if i > j:
    print(i, 'is greater than', j)
else:
    print(i, 'is less than', j)

#==============================================================================
# DEFINING FUNCTIONS AND CLASSES  -> always observe IDENTATION
# def funcName():
# class className:
def sumFunc(a, b):
    return (a + b)

print(sumFunc(200, 300))
#==============================================================================
# WHILE Loop
a = 0;
while(a < 10):
    a = a + 1
    print(a);

# INFINITE LOOP -> applicable say when sensing throughout; using a microcontroller and sensor
# while(True):
#     print('Hello, EMoS')

# Combining FOR loop and IF statement:
for i in range(1, 20, 1):
    # if i%5 == 0:
    #     print(i)

    # BREAK keyword
    # if i > 5:
    #     break   # to exit loop when IF condition is met
    # print(i)

    # CONTINUE keyword
    # if i == 5:
    #     continue
    # print(i)

    # PASS keyword
    # The 'pass' statement is used as a placeholder for future code.
    # When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.
    # Empty code is not allowed in loops, function definitions, class definitions, or in if statements.
    if i == 5:
        pass    # pass keyword does nothing
    print(i)

#==============================================================================
# Random Number Generator
import random
x = random.randint(1, 100)
print('Random x: ', x)
