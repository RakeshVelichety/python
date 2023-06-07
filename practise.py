#ARITHMETIC OPERATIONS--INTEGERS

'''print("Addition",4+4)
print("Substraction",8-4)
print("Multiplication",6*6)
print("Division",4/2)
print("Division",7/2)
print("Division without remainder",7//2)
print("Modulus",3%2)
print("Exponentation",2**3)'''

# Floating numbers
'''print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)'''


# Complex numbers
'''print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))'''


# Declaring the variable at the top first

'''a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function - try to avoid overriding built-in functions
# if you do not label your print with some string, you never know where the result is coming from
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)'''


'''print('== Addition, Subtraction, Multiplication, Division, Modulus ==')

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)'''

# Calculating area of a circle
'''radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)'''

#Calculate area of rectangle
'''length = 10
width = 20
area_of_rectangle = length*width
print("Area_of_rectangle",area_of_rectangle)'''

#Calculating weight of an object
'''mass = 76
gravity = 9.8
weight = mass*gravity
print("weight in N",weight)'''

#Calculating density of a fluid
'''mass =75 #in kg
volume = 0.075 #in cubic meter
density = mass/volume #1000 kg/m^3
print("Density",density)'''

#comparison operators
'''print(3>2)
print(3>=2)
print(3<2)
print(2<3)
print(2<=3)
print(3==2)
print(3!=2)
print(len('mango')==len('avacado'))
print(len('namgo')!=len('avacado'))
print(len('mango')<len('avacado'))
print(len('milk')==len('meat'))
print(len('milk')!=len('meat'))'''


#comparing something gives either a true or false
'''print('True==True',True==True)
print('False==False',False==False)
print('True==False',True==False)'''

'''In addition to the above comparison operator Python uses:

is: Returns true if both variables are the same object(x is y)
is not: Returns true if both variables are not the same object(x is not y)
in: Returns True if the queried list contains a certain item(x in y)
not in: Returns True if the queried list doesn't have a certain item(x in y)'''

'''print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)'''   # True


#Logical operators

'''print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False)''' # False


#*************************DAY-3(EXERCISE)****************************************
#age = 24
#print(age)

#height = 194.5
#print(height)

#complex = 2+5j
#print("complex number:",complex)

#Continued in pycharm