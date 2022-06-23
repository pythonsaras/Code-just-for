# def myDecorator(fun):
#     def wrapper():
#         print("Decorator ")
#         fun()
#     return wrapper
# @myDecorator# use in python  to use decorators
# def hello():
#     print("hello")
# hello()

# myDecorator(hello)()#also give same above result 
# def myDecorator(fun):
#     def wrapper( *args, **kwargs):
#         print("Decorator ")
#         fun(*args, **kwargs)
#     return wrapper
# @myDecorator# use in python  to use decorators
# # def hello(name):
# #     print(f"hello {name}")
# # hello("ram")

# def hello(name):
#     return f"hello {name}"
# hello("ram")

# def logged(fun):
#     def wrapper(*args, **kwargs):
#         return_value=fun(*args, **kwargs)
#         with open('logfile.txt','+a') as f:
#             fname=fun.__name__
#             f.write(f"{fname} return value is {return_value}\n")
#     return wrapper        
# @logged
# def add(x,y):
#     return x+y
# print(add(4,3))
import time
def timed(function):
    def wrapper(*args, **kwargs):
        before=time.time()
        value=function(*args, **kwargs)
        after=time.time()
        fname=function.__name__
        print(f"{fname} took {after-before} seconds to eexecute!")
    return wrapper
@timed
def hello(x):
    result=1
    for i in range(1,x):
        result+=1
    return result

print(hello(1000000))
        