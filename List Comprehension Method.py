squared = [i**2+3 for i in range(1,11) if i % 2 == 1]
print(squared)


lst = [10,20,30,40,60,100,200]
#Iteration: index-based
for i in range(len(lst)):
  print(lst[i])

# Iteration: element-based
for i in lst:
  print(i)