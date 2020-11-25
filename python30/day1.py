def fun(a, b, c):
    print(a, b, c)

fun(1, 2, 3)

def fun(*args):
    print(args)

fun(1, 2, 3)

def fun(a=0, b=0, c=0):
    print(a, b, c)

fun(a=1, b=2, c=3)

def fun(**kwargs):
    print(kwargs)

fun(a=1, b=2, c=3)

def fun(*args, **kwargs):
    print(args)
    print(kwargs)

fun(1, 2, a=3, b=6)

# Output:
# (1, 2)
# {"a": 3, "b": 6}

def func(a, b, c):
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")

numbers = [5, 4, 2]
func(*numbers)

numbers = {"c": 4, "a": 6, "b": 9}
func(**numbers)

"""
Create a function that receives N numbers and returns
each of these multiplied by 2
"""


def multiply_by_two(*mix):
    data = []
    [data.append(x*2) for x in mix]
    print(data)

multiply_by_two(4, 6, 3, 5)
"""
Create a function that receives N arguments with your
personal information: name, age, phone, country, etc
Then print those values with their names
name: your name
country: your country
"""

def personal_information(**kwargs):
    for i,k in kwargs.items():
        print(i,k)

personal_information(some='value',name='nombre')
"""
The Python print function receives positional and named arguments,
the named arguments are used to alter the way this print works:
sep = It indicates how all the values we pass will be separated
end = Indicates what you will put at the end of printing
Default Values:
sep = " "
end = "\n"
Use the *args and **kwargs to pass these arguments and print a phrase
depending on a tuple/list of values.
"""
config = {"sep": "**", "end": "\nThis is the end"}
values = ["Hello", "World", "This", "Is", "Esteban"]

print(*values, **config)