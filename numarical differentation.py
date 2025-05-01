import math

def f(x):
    return 3*x**3 - 2*x + x  # Simplifies to 3*x**3 - x

h = 1
x = 4

# Forward differences
dff1 = (f(x+h) - f(x)) / h
dff2 = (f(x+2*h) - 2*f(x+h) + f(x)) / h**2
dff3 = (f(x+3*h) - 3*f(x+2*h) + 3*f(x+h) - f(x)) / h**3

print('Solution by forward differences:')
print(f"f'({x}) = {dff1}")
print(f"f''({x}) = {dff2}")
print(f"f'''({x}) = {dff3}")

# Central differences
dfc1 = (f(x+h) - f(x-h)) / (2*h)
dfc2 = (f(x+h) - 2*f(x) + f(x-h)) / h**2
dfc3 = (f(x+2*h) - 2*f(x+h) + 2*f(x-h) - f(x-2*h)) / (2*h**3)

print('\nSolution by central differences:')
print(f"f'({x}) = {dfc1}")
print(f"f''({x}) = {dfc2}")
print(f"f'''({x}) = {dfc3}")

# Backward differences
dfb1 = (f(x) - f(x-h)) / h
dfb2 = (f(x) - 2*f(x-h) + f(x-2*h)) / h**2
dfb3 = (f(x) - 3*f(x-h) + 3*f(x-2*h) - f(x-3*h)) / h**3

print('\nSolution by backward differences:')
print(f"f'({x}) = {dfb1}")
print(f"f''({x}) = {dfb2}")
print(f"f'''({x}) = {dfb3}")
