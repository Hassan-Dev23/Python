import os
os.system('cls' if os.name == 'nt' else 'clear')

name = "hassan"

def addi(num1,num2):
    return num1+num2
    

print(addi(23,23))

# all of this is about nested function
def outer_func(a):
    def inner_func(b):
        return a + b
    return inner_func

# closure = outer_func("has")
# print(closure("san"))

def fun():
    print(",,,,")
    def fun2():
        print("---")
    return fun2
        

# function1=fun()
# print(function1())

def uni():print("hassan")

def un(function):
    return function

# un(uni())

def printlist(**data):
    print(data)

printlist(name = "hassan", age = 14)


# Decortor function 


def deco(fun):
    def dec():
        print("First Call")
        fun()
        print("after call")
    return dec


@deco
def show():
    print("Hassan")
show()

sq = lambda num: num*num
print(sq(7))


def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

counter = count_up_to(5)
print(next(counter))  # Output: 1
print(next(counter))  # Output: 2
print(list(counter))  # Output: [3, 4, 5]


def f(x, arr=[]):
    arr.append(x)
    return arr

print(f(1))
print(f(2))
print(f(3))


