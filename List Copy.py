list1 = [ 10, 20, 30, 'AI Lab', 'Vacation']
print ( list1 )

list2 = list1
print ( list2 )

list2.append ( 100 )
print( list1, list2 )

list3 = list1.copy()
list3.pop()
print( list1, list2, list3 )


# mutable - list, string, dictionary
# immutable - int, float, tuple
a = 'AI Lav is vest'
print(a)
print(a+'b')
print(a.index('v'))
a = a.replace('v','b')
print(a)
