def decorate_concat(func):
    def add_sex():
        print("I am male")
        func()

    return add_sex


@decorate_concat
def concat():
    print("I am the function")

concat()

# Similar way but using @ synthetic sugar above is more optimised
# decorated_function = decorate_concat(concat)
# decorated_function()
