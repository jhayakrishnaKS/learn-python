# map function

def square(num):
    return num**2

my_nums=[1,2,3,4,5]
for i in map(square,my_nums):
    print(i,end=" ")
    
print("\n",list(map(square,my_nums)))

def splicer(mystring):
    if len(mystring)%2==0:
        return "EVEN"
    else:
        return mystring[0]

names=["jk","krish","tris","afr"]

print(list(map(splicer,names)))


# filter
def check_even(num):
    return num%2==0
print(list(filter(check_even,my_nums)))
for i in filter(check_even,my_nums):
    print(i,end=" ")
    
# lambda functions
cube=lambda num: num**3
print("\n",cube(2))
print(list(map(lambda num: num**3,my_nums)))
print(list(filter(lambda num:num%2==0,my_nums)))
print(list(map(lambda nam:nam[0],names)))
