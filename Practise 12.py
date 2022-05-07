list1 = [1,2,3,4,[5,6,7,8,9]]
for x in list1[4]:
 print(x)

list2 = [{'a':1, 'b':2, 'c':{1:2, 2:{'a':5, 'b':7, "c":'sundeep'}}}]
print(list2[0]['c'][2]["c"])
x = list2[0]['c'][2]["c"]
print({i:x.count(i) for i in x})


list_of_lists = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
transposed = [[row[i] for row in list_of_lists] for i in range(len(list_of_lists[0]))]
print(transposed)