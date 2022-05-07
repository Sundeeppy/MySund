test_list1 = [1, 3, 4, 6, 8]
test_list2 = [4, 5, 6, 2, 10]

print("Original list 1 : " + str(test_list1))
print("Original list 2 : " + str(test_list2))

res_list = []
for i in range(0, len(test_list1)):
       res_list.append(test_list1[i] + test_list2[i])

print("Resultant list is : " + str(res_list))
#
mydict2 = {1:'sundeep', 'name':{'location':{'marath', 'white'}, 'che':{1:{'hy', 'ra'}}}}
nl = []
nl.append(mydict2[1])
nl.append(mydict2['name']['location'])
nl.append(mydict2['name']['che'][1])
print(nl)

mydict3 = {10:56, 10:4, 20:1, 20:9, 30:1, 50:6}
mydict4 = {}
for x in mydict3:
       if x in mydict4:
              mydict4[x] += 1
       else:
              mydict4[x] = 1
print(mydict4)

a = {}

n = int(input("number of elements: "))
for i in range(n):
       k = input('Enter key: ')
       v = input('Enter value: ')
       a[k] = v

print('Details of Cadidates: \n', a)


a = {
    10 : 2,
    20 : 3,
    40 : 4,
    10 : 7,
}
print(a)
