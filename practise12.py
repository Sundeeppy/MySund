# creating list

from django.conf import PASSWORD_RESET_TIMEOUT_DAYS_DEPRECATED_MSG


my_list = [] #create empty list
print(my_list)

my_list = [1,2,3,"example",3.132] #creating list
print(my_list)

# To add elements in a list use append(),extend() and insert()

my_list = [1,2,3]
print(my_list)
my_list.append([55,12,15]) # add as a single element
print(my_list)

# output is [1,2,3,[55,12,15]]

my_list.extend([234,'example']) # add different element
print(my_list)

# output is [1,2,3,[55,12,15],234,'example']

my_list.insert(1,'xxxx') # add one element
print(my_list)

# output is [1,'xxxx',2,3,[55,12,12],234,'example']

# Deleting elements in a list
# del keyword is used

my_list = [1,2,3,'example',3.132,10,30]
del my_list[5] # delete element at 5th index

# pop() will remove last element if ntg specified
# pop(1) will remove the first indiex position value

my_list = [1,2,3,'example',3.132,10,30]
a = my_list.pop(1) 
print('Popped Element: ',a,'List remaining: ', my_list)

my_list.clear() #empty the list
print(my_list)

# Accessing elements in the list

my_list = [1,2,3,'example', 3.132,10,30]
for element in my_list: #access elements one by one
    print(element)
print(my_list) # accessing all elements
print(my_list[3]) # access index 3 element
print(my_list[0:2]) # access elements from 0 to 1 and exclude 2 
print(my_list[::-1]) # access elements in reverse

# Other functions

# 1. len() = length of the list
# 2. index() = index value of value
# 3. count() = find the count of value passed
# 4. sorted() / sort() = do the same, sort value of the list
# 5. sorted() = has a return type
# 6. sort() = modifies the original list

my_list = [1,2,3,10,30,10]
print(len(my_list)) # find length of list
print(my_list.index(10)) # find index of element that occurs first
print(my_list.count(10)) #find count of the element
print(sorted(my_list)) #print sorted list but not change original
my_list.sort(reverse=True) #sort original list
print(my_list)
