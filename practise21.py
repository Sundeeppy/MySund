# String Methods

# 1. capitalize() = Converts the first character to upper case

txt = "sundeep"
x = txt.capitalize()
print(x)

# 2. casefold() = converts string to lower case

txt = "sundeep"
x = txt.casefold()
print(x)

# 3. center() = returns a centered string

txt = "hello"
x = txt.center(20)
print(x)

# 4. count() = returns the number of times a specified value occurs in a string

txt = "sundeep"
x = txt.count(e) # we need to specify the element to be counted
print(x)

# 5. endswith() =  returns true if the string ends with the specified value

txt = "hello world"
x = txt.endswith("d") # shud specify the end element within quotes
print(x)

# 6. find() = searches the string for a specified value and returns the position where it is found

txt = "sundeep"
x = txt.find(e) # will only find the first occurence index position
print(x)

# 7. format() = formats the specified value(s) and insert them inside the string's placeholder

#named indexes :

txt1 = " My name is {fname}, I'm {age}".format(fname = "John", age = 40)
print(txt1)

#numbered indexes :

txt2 = "My name is {0}, I'm {1}".format("John",40)
print(txt2)

# empty placeholder :

txt3 = "My name is {}, I'm {}".format("John",40)
print(txt3)

# 8. isdigit() = returns true if all character in the string are digits

txt1 = "sun2345"
x = txt.isdigit()
print(x)

# 9. join() = converts the elements of an iterable into a string

txt = ("hello","world") # tuple into a string
x = " ".join()
print(x)

# 10. isupper() =  returns true if all characters in the string are upper case

txt = "THIS IS NOW!"
x = txt.isupper()
print(x)

# Dictionary methods

my_dict = {}
print(my_dict)
my_dict = {1: 'Python', 2 : 'Java'} # Dictionary with elements
print(my_dict)

# Output
# {}
# {1:'Python',2:'Java'}

my_dict = {'First':'Python','Second':'java'}
print(my_dict)
my_dict['Second'] = 'C++'
print(my_dict)
my_dict['Third'] = 'Ruby'
print(my_dict)

# Output

# {'first':'Python','Second':'Java'}
# {'First':'Python','Second':'C++'}
# {'First':'Python','Second':'C++','Third':'Ruby'}


# Deleting key, value pairs
# pop() = which returns the value that has been deleted
# popitems() = To retrieve the key-value pairs
# clear() = To clear the entire dictionary

my_dict = {'First':'Python','Second':'Java','Third':'Ruby'}
a = my_dict.pop('Third') #pop element
print('Value:', a )
print('Dictionary:', my_dict)
b = my_dict.popitem() #pop the key-value pair
print('Key,value pair:', b)
print('Dictionary', my_dict)
my_dict.clear()
print('n', my_dict)

# Output
# Value:Ruby
# Dictionary:{'First':'Python','Second':'Java'}
# Key,value pair:('Second','Java')
# Dictionary{'First':'Python'}

# Accessing Elements

my_dict = {'First' : 'Python', 'Second' : 'Java'}
print(my_dict['First']) #access elements using keys
print(my_dict.get('Second'))

# Output
# Python
# Java

#Other Functions

my_dict = {'First':'Python','Second':'Java','Third':'Ruby'}
print(my_dict.keys()) #get keys
print(my_dict.values()) #get values
print(my_dict.items()) #get key-value pairs
print(my_dict.get('First'))

#Output
# dict_keys(['Fisrt,'Second','Third'])
# dict_values(['Python','Java','Ruby])
# dict_items([('First','Python'),('Second','Java'),('Third','Ruby')])
# Python


# Tuple

# Creating tuple

my_tuple = (1,2,3) # creating tuple
print(my_tuple)

# Accessing Elemenets

my_tuple2 = (1,2,3,'edureka') #access elements
for x in my_tuple2:
    print(x)
print(my_tuple2)
print(my_tuple2[0])
print(my_tuple2[:])
print(my_tuple[3][4])

# Output
# 1
# 2
# 3
# edureka
# (1,2,3,'edureka')
# 1
# (1,2,3,'edureka')
# e

# appending elements

my_tuple = (1,2,3)
my_tuple = my_tuple + (4,5,6) #add elements
print(my_tuple)

# output
(1,2,3,4,5,6)














