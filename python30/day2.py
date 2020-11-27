print(range(5))

sequence = list(range(5))
print(sequence)

print(list(range(5, -5, -1)))

"""
Generate a sequence using the function range that
returns the following.
[-100, -90, -80, -70, -60, -50, -40, -30, -20, -10, 0,
10, 20, 30, 40, 50, 60, 70, 80, 90]
"""
sequence = range(-100, 100, 10)
print(list(sequence))
"""
Generate the previous sequence but in this case in
the opposite way.
"""
sequence = range(100, -100, -10)
print(list(sequence))

"""
This challenge can be a bit difficult, try to create a
function that returns a sequence of decimal numbers between
2 numbers, incremental only.
Here's a hint, use the while statement
"""

def floating_range(start, stop, step):
    pass