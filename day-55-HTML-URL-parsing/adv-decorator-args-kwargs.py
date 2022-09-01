class User:
    def __init__(self, name):
        self.name = name
        self.is_authenticated = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_authenticated == True:
            function(args[0])
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"{user.name} just created a blog")


new_user = User("Seyi")
new_user.is_authenticated = True
create_blog_post(new_user)
