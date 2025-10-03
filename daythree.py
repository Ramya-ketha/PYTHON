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
#dictionaries
dict={
    "model":"1st model",
    "year":2021,
    "age":25
# }

print(type(dict))
print(dict['model'])
dict['city']='Hyderbad'
print(dict)

#function example
def mom(a,b):
    print(a+b)
a=10
b=20
c=mom(a,b)
print(c)
d=mom(5,6)
print(d)
e=mom(a,b)
print(e)
f=mom(5,6)
print(f)
