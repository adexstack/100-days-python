def logging_decorator(fn):
    def wrapper(*args, **kwargs):
        print(f"You called {fn.__name__}{args}")
        result = fn(*args)
        print(f"It returned: {result}")
    return wrapper

# Use the decorator
@logging_decorator
def add(num1, num2):
  return(num1 + num2)

add(2, 3)