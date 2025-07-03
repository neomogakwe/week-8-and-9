
def greet(name):
    print(f"Hello, {name}")

greet("Neo")  # Call happens *after* the function is defined

# returning a function in python
def add(a, b):
    return a + b
result = add(2, 5)
print(result)

# functions including loops , conditional statements etc.
def function(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
# optional parameters when you call a function ,it will use its default value.
def greet( name, greeting="Hello"): 
      print(f"{greeting} ,{name}")
greet("Neo", "Good Morning")    