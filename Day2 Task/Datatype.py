#number Datatypes

a=50
print(a, "is of type", type(a))

b=50.5
print(b, "is of type", type(b))
print(b, "is complex number?", isinstance(50.5, int))

c= 3 + 2j
print(c, "is complex number?", isinstance(3 + 2j, complex))

#String Datatypes

name= "patel Jaykumar"

print("name is:", name)
print(name[0])
print(name[2:6])
print(name[3:])
print(name[:6])
print(name * 2)
print(name + "hello")

#List datatypes

list1 = [50, 60, 70, "Jay", 90, 40, "hello", 10 ]

print("list1[2] =", list1[2])
print("list1[0:5] =", list1[0:5])
print("list1[5:] =", list1[5:])
print(type(list1))

#Tuple Datatypes

tuple1 = (50, 60, 70, "Jay", 90, 40, "hello", 10)
print(tuple1)
print("tuple1[2]", tuple1[2])
print("tuple1[0:4]", tuple1[0:4])
print("tuple1[5:]", tuple1[5:])

#Dictionary Datatype

d = {1: "Patel", 2: "Jay", "key": 50}

print(type(d))
print("d[2] =", d[1])
print("d[key] =", d["key"])
