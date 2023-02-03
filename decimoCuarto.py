
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# This code creates a decorator called my_decorator that wraps around 
# the say_hello function. When the say_hello function is called, 
# the decorator is executed first, printing out "Something is happening 
# before the function is called." before the function is called, 
# and "Something is happening after the function is called." 
# after the function is called.

# You can use the @ syntax to apply the decorator to a function, 
# as shown in the example. The @my_decorator line above the say_hello 
# function tells Python to use the my_decorator decorator for that 
# function.