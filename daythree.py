type casting 
a=10
print(type(a))
a=(str(a))
print(type(a))
k=float(a)
print(type(k))

lists=[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
k=set(lists)
print(k)

lists=[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
k=set(lists)
k.add(12)
print(k)
