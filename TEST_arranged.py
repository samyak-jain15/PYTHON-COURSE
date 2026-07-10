password = "samyakjain"
guess = "samyak"
while guess !=password:
    guess = input("ENTER PASSWORD: ")
    if guess!=password:    
        print("WRONG PASSWORD")
print("CORRECT")
#so this shows if i use if THEN THE CODE WILL ALSO RUN ON WRONG PASSWORD
######################################################################
# NOTES: COMMON ERROR TYPES
######################################################################
#name error = variable/function name is misspelled
#type error wrong numberor type of arguments
#syntax error typo in code str
#index error list index out of range

######################################################################
# IMPORTS
######################################################################
from cmath import sqrt
import math
import turtle

######################################################################
# VARIABLES, DATA TYPES, type() & isinstance()
######################################################################
my_set_var = [7,"hello world", 8.6]#this is a commenrt 
print("set:",my_set_var )
print("hello world")
developer = "sam"
print(type(developer))
account_balance = 12
print(type(account_balance))
account_balance = 12.5
print(isinstance(account_balance,int))
print(isinstance(account_balance,(int,float)))

######################################################################
# STRINGS
######################################################################
my_str_1 = "hello"
my_str_2 = "world"
str_plus_str = my_str_1 +" "+ my_str_2
print(str_plus_str)
my_str_3 = """this 
is a multiline string"""
print(my_str_3)
my_str_4 = "hello world hi"
print("hello" in my_str_4)#true
print(my_str_4.endswith("hi"))#true
print(len(my_str_4))#14
print(my_str_4[0])
name = "samyak"
age = 19
name_and_age = name + " " + str(age)
print(name_and_age)
#string interpolation 
name = "samyak"
age = 19 
name_and_age = f' My name is {name} and my age is {age} years old'
print(name_and_age)
num1 = 5
num2 = 10 
print(f'the sum of {num1} and {num2} is {num1 + num2}')
my_str_5 = "hello world"
print(my_str_5[2:7])#7 is not included
print(my_str_5[2: :2])#2 is spacing 
#some inbuild string 
#upper
sam = "hello world"
jain = sam.upper()
print(jain)
#2. lower 
#3.startswith(prefix)
sam = "hello world"
jain = sam.startswith("hello")
print(jain)
#endswith()
#find(substring)
sam = "hello world"
jain = sam.find("world")
print(jain)
#TITLE() RETURN FIRST LETTER CAPITAL OF EACH WORD 
#replace{old,new}

######################################################################
# NUMBERS: INT & FLOAT OPERATIONS
######################################################################
one = 5
two = 40 
total_sum = one + two
print(total_sum)
three = 10.6
four = 20.5
total_sum = three + four
print(total_sum) 
my_float_1 = 5.4
my_float_2 = 12.0
float_addition = my_float_1 + my_float_2
print('Float Addition:', float_addition) # Float Addition: 17.4 
my_int_1 = 56
my_int_2 = 12
# Division
div_ints = my_int_1 / my_int_2
print('Division:', div_ints) # Division: 4.666666666666667
#modulo operation remainder
sam = 10
jain = 4
modulo = sam % jain
print('Modulo:', modulo) # Modulo: 2
floor_division = sam // jain
print('Floor Division:', floor_division) # Floor Division: 2
#floor divides two no and give  the largest integer value that is less than or equal to the result of the division
#exponentiation raise a number to the power of another number
base = 2    
exponent = 3
result = base ** exponent
print('Exponentiation:', result) # Exponentiation: 8    
#some time error so convert int to float and vice versa
my_int = 10 
my_float = 3.5
# Convert int to float
my_float_from_int = float(my_int)
print('Float from int:', my_float_from_int) # Float from int: 10.0
# Convert float to int
my_int_from_float = int(my_float)
print('Int from float:', my_int_from_float) # Int from float: 3     
#some other operation
#round
rounded_value = round(3.14159, 2)
print('Rounded Value:', rounded_value) # Rounded Value: 3.14
#abs turn negative to positive
negative_number = -10
absolute_value = abs(negative_number)
print('Absolute Value:', absolute_value) # Absolute Value: 10
#pow 
base = 2
exponent = 3
result = pow(base, exponent,3) # 2 raised to the power of 3, then take modulo 3
print('Power with Modulo:', result) # Power with Modulo: 2
mu_num = 36
print(sqrt(mu_num)) # Square Root: 6.0
#The division assignment operator (/=) divides the left variable by the right and stores the result back in the left variable:
price = 100
price /= 4
print(price) # 25.0
price = 100
price //= 4#floor operator and other also can be used
print(price) # 25
#And the multiplication assignment operator can be used to repeat a string:
greet = 'Hello'
greet *= 3
print(greet) # HelloHelloHello

######################################################################
# COMPARISON OPERATORS
######################################################################
#but only add and multiply can be used
print(3>4)#false
print(3<4)#true
print(3==4)#false equal to
print(3!=4)#true not equal to 
print(3>=4)#false greater than or equal to
print(3<=4)#true less than or equal to  

######################################################################
# CONDITIONAL STATEMENTS (if / elif / else)
######################################################################
age = 18
if age>=18:#if condition:
 print("you are an adult")
age = 12
if age>=18:
 print("you are an adult")
else:
 print("you are not adult")
# for muliple condition 
age = 65
if age>= 80:
 print("you are old")
elif age>= 60:
 print("mostly old aunty")
elif age>=30:
 print("young kee going")
else:
 print("you are child")
is_citizen = True
age = 25
if  is_citizen:
 if age >=18:
  print("you are eligible to vote")
else:
 print("you are not eligible")

is_citizen = True
age = 20 
if is_citizen:
    if age>=25:
        print("HEY DOING GOOD")
    else:
        print("HEY ELSE IS DOING WORK")
 #falsy value like 0 ,"",0.00, None,False
# to check falsy statement
print(bool(0))
print(bool(""))
#some operator like and or and main important is not 
#not 
sam = True
age = 24
if age>=20 and sam:
    print("very good")

distance = 21
if not isinstance(distance , float):
    print("good you learn not statement")

######################################################################
# USER INPUT & TRY-EXCEPT
######################################################################
name = input("what is your name")
age = int(input("what is your age"))
if age>=18:
    print("HELLO",name and "You are an adult")
else:
    print("HELLO",name and "You are not an adult")
value = input("Enter a value:")

try:
    number = int(value)
    print("you entered an integer")
except:
    print("you did not enter an integer")
print(int(3.14))#3 and this is different from input

######################################################################
# LISTS
######################################################################
#list it is like indexing 
cities = ["indore", "bhopal", "hatta"]
print(cities[0])#indore
print(cities[-1])#hatta
#to convert into lists 
sam = "samyak"
print(list(sam))
numbers = [1, 2, 3, 4, 5]
len(numbers) # 5
sam = ["1","2","3"]
sam[0] = "0"
print(sam)#replace the 1 with 0 
sam = ["1","5","8"]
del sam[2]#so changes can be made by using indexing 
print(sam)#1,3 this will delete the index 2 
#to check element is in the list or not in is used
sam = ["1",'2','3','4','5']
print('3' in sam)#True
print(3 in sam)#False
sam = ['1' , '2',['3','4','5']]
print(sam[2])#[3,4,5,] as indexing starts from 0 
print(sam[2][1])#4
sam = ["1",'2','3','4','5']
jain , good , boy , *rest= sam
print(jain)#!
print(good)#2
print(boy)#3
print(rest)#[4,5]
sam = ["1",'2','3','4','5','6']
print(sam[1::2])#(2,4,6)
#append USED TO ADD ELEMENT IN LAST 
sam = ["1",'2','3','4','5','6']
sam.append(7)
print(sam)
sam = ["1",'2','3','4','5','6']
jain = ['1','2']
sam.append(jain)
print(sam)#['1''2''3','4','5','6',['1','2']]
#extend() it is like append but for multiple value to add
sam = ["1",'2','3','4','5','6']
jain =['7','8']
sam.extend(jain)
print(sam)#["1",'2','3','4','5','6','7','8']
#insert(at,number) it is used to add in between 
sam = ["1",'2','3','4','5','6']
sam.insert(2,2.5)
print(sam)
#remove() THIS WILL REMOVE FIRST OCCURANCE
sam = ["1",'2','3','4','5','6','6']
sam.remove("6")
print(sam)#["1",'2','3','4','5','6']
#pop(index)remove specific index
sam = ["1",'2','3','4','5','6']
sam.pop(2)
print(sam)
#if no number then default last index 
#clear() emplty the list
sam = ["1",'2','3','4','5','6']
sam.clear()
print(sam)
#sort()sort the randomness of list
jain = ['16','1','55','435']
jain.sort()
print(jain)
#we can use sort function sorted()
jain = ['16','1','55','435']
sam = sorted(jain)
print(sam)
#reverse 
sam = ["1",'2','3','4','5','6']
sam.reverse()
print(sam)
#index(element) it will index of that 
sam = ["1",'2','3','4','5','6']
print(sam.index('4'))

######################################################################
# TUPLES
######################################################################
#tuple like list but can store different type of elements
sam = ['samyak','19']
print(sam[1])
sam = 'samyak'
print(tuple(sam))
sam = ('1', 'samyak','19')#can use both bracket
print('1' in sam)
sam = ('1', 'samyak','19')
jain,samyak,hello = sam
print(jain)
print(samyak)
#NOTE - TUPLE ARE IMMUTABLE THAT MEANS THAT CHANGES CANNOT BE MADE
#LIKE ADDING , REMOVIN ETC. ERROR WILL COME
#FEW OPERATION IN TUPLE ARE 
#count number of times an element occur
sam = ('Rust', 'Java', 'Python', 'C++', 'Rust')
print(sam.count('Rust')) # 2
#index() you can also pass the index starting optional(basically giving starting and ending position)
sam = ('Rust', 'Java', 'Python', 'C++', 'Rust','Python')
print(sam.index('Python',3))#5 it will start searching from 3 
sam = ('Rust', 'Java', 'Python', 'C++', 'Rust','Python')
print(sam.index('Python',2,5))#2 it will start from 2 and end in 5 
#sorted also work
#reverse also work
sam = ('Rust', 'Java', 'Python', 'C++', 'Rust')
print(sorted(sam, key=len))
print(sorted(sam, reverse = True))##########

######################################################################
# LOOPS: for, while, break, continue, range, enumerate, zip
######################################################################
#different types of loops 
#for 
sam = ['1','2','3','4']
for number in sam:
    print(number)
sam = ['1','2','3','4']
jain = ['sam','jain']
for number in sam:
    for name in jain:
        print(number,name)     
for char in "SAMYAK":
    print(char)
#while it work until false comes
secret_number = 2
guess = 5 
while guess != secret_number:
    guess = int(input('Guess the number btw(1,5): '))
    if guess!= secret_number:
        print('wrong number ,guess again')
print('you are correct')  
#break once the value comes it stopped and print before of that
sam = ['1','2','3','4']
for jain in sam:
    if jain =='3':
        break
    print(jain)     
#continue it skip that particular Value 
sam = ['1','2','3','4']
for jain in sam:
    if jain =='2':
        continue
    print(jain)
sam = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
for number in sam:
    if number % 2 ==0:
        continue
    print(number)
#now we will combine else statement for and while 
words = ('samyak', 'jain', 'good', 'boy')
for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains vowel '{letter}'")
            break
    else:
        print("'{words}' do not contain vowel")###########
#range generate integers (start,stop,step) stop is not included and must number is stop 
#default start 0 and step 1
for num in range(5):
    print(num)
for num in range(2,10,2):
    print(num)
number = list(range(2,10))
print(number)
#when we use for statement it generate element one by one 
#if we want to keep the track of indexing then 
#method 1 
language = ['HINDI','ENGLISH','SPANISH']
index = 0 
for languages in language:
    print(f'index {index} and language {languages} ') 
    index += 1 
#method 2 
#enumerate()   
language = ['HINDI','ENGLISH','SPANISH']
print(list(enumerate(language)))#[(0,HINDI),(1,ENGLISH),(2,SPANISH)]
language = ['HINDI','ENGLISH','SPANISH'] 
for index , languages in list(enumerate(language)):
    print(f'index {index} and language {languages}')
#so here we start from 0 if we want to start from 1 numbering then 
languages = ['Spanish', 'English', 'Russian', 'Chinese']

for index, language in enumerate(languages, 1):
    print(f'Index {index} and language {language}')
# if we want to add multiple list together
sam = ['1','2','3','4'] 
languages = ['Spanish', 'English', 'Russian', 'Chinese']
print(list(zip(sam,languages)))  
developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

for name, id in zip(developers, ids):
    print(f'Name: {name}')
    print(f'ID: {id}')

######################################################################
# LIST COMPREHENSIONS
######################################################################
even_number = []
for num in range(21):
    if num % 2 == 0: 
      even_number.append(num)
print(even_number)  
#short form 
even_number = [num for num in range(21) if num % 2 == 0 ]
print(even_number) 
number = [1,2,3,4,5]
result = [(num,'EVEN') if num % 2 == 0 else(num ,"ODD") for num in number] 
print(result)

######################################################################
# FUNCTIONS: def, return, filter, map, lambda, recursion
######################################################################
#functions
def hello():
    print("hello world")
hello()
def calculate(a,b):
    print(a+b)
calculate(3,2)
def calculate(a,b):
    return(a+b)#this will store 7 in sum 
result = calculate(3,4)
print(result)
def function():
    sam =10
    print(sam)
function()
#filter() 
words = ["sky",'tree','samyak','jain','in']
def longword(word):
    return len(word)>4
longwords = list(filter(longword, words))
print(longwords)
#map() operate operationj on each element 
celcius = [10,20,30,40,50]
def toferenhight(temp):
    return(temp*9/5) + 32
ferenhight = list(map(toferenhight, celcius)) 
print(ferenhight)   
numbers = [5, 10, 15, 20]
total = sum(numbers, 50) #100  positional argument so here 50 is additional added by me 
print(total)
def square(num):
    return num**2
print(square(4))
#lambda
numbers = [1,2,3,4,5,6,]
sam = list(filter(lambda x: x % 2 ==0 , numbers))
print(sam)  
number = [1,2,3,4,5,6]
square = lambda x: x**2
square_number = list(map(square,number)) 
print(square_number)
result = (lambda x : (x**2 + 2*x) if x>0 else(x**3 -x +4))(3)
print(result)
def calculates(x):
    if x>0:
        return x**2 +2*x
    else:
        return x**3 -x +4
print(calculates(3))
def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)  
print(fact(5))
def sam(n):
    if n==0:
        return 
    print(n)
    sam(n-1)
sam(5)

######################################################################
# TURTLE GRAPHICS
######################################################################
#sam = turtle.Turtle()
#sam.forward(100)
#turtle.Screen().exitonclick()
n = int(input("integer:" ))
for i in range(1,10):
  print(f'{n} x {i} = {n*i}')
import math

# Read the shape
shape = input("shape:" ).strip()
if shape == "rectangle":
  width = int(input())
  length = int(input())
  area = float(width * length)
  print(f'Area: {area:.2f}')
elif shape == "triangle":
  base = int(input())
  height = int(input())
  area = float((base*height)/2)
  print(f'Area: {area:.2f}')
elif shape == "circle":
  radius = int(input("radius:" ))
  area = float(math.pi*radius*radius)#math.pi very important################
  print(f'Area: {area:.2f}')#2 decimals ans area : 10.00
  
# Read measurements and calculate area

# Print the area
#dictionary
info = {
       'name':'samyak jain',
       'age':19 ,
       'profession':['student','coding']
        }
print(info['name'])
info['name'] = 'SAMYAK JAIN'
print(info['name'])
print(info.get('jain',[]))#if jain is not there it will return empty list
print(info.get('age',[]))
#keys #values
print(info.keys())#name,age
print(info.values())#samyak jain 19
print(info.items())#dono sath mein













