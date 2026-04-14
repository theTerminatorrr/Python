# array - homogeneous structure
# list - heterogeneous structure
lst = list()
print(type(lst))
lst = [10,20,30,40,60]
print(len(lst))
print(lst[0])
print(lst[-2])



marks = []
marks.append(78)
print(marks)


marks.append(80) # adds an element at the end of the list
print(marks)
marks.insert(1,'AI') # adds an element at the specified position
print(marks)
# marks.pop() # removes an element from the end of the list
marks.pop(1) # removes an element from the specified position
print(marks)
marks.remove(80) # removes an element from the list if it exists
print(marks.index(78))



# searching
target = 80
if target in marks:
  marks.remove(target)
print(marks)