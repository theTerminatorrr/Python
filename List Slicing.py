squared = [ i**2 for i in range ( 1, 11 ) ]
print ( squared )

first = []
for i in range (0, 5):
  first.append( squared[i])
print ( first )

first = squared [ 0 : 5 ]
print ( first )

odd = squared [ : : 2 ]
print ( odd )

even = squared [ 1 : : 2 ]
print ( even )

ind = len(squared)//2
middle = squared [ ind : ind+3 : 2 ]
print ( middle )

middle = squared [ len(squared)//2: ]
print ( middle )