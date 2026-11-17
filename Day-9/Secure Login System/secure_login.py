#Secure Login System (Decorators) 
#A web application wants to ensure that users are authenticated before accessing 
#sensitive functions. Create a decorator that checks whether the user is logged in before 
#allowing access to a function.


def login_required(func):
    def wrapper(is_logged_in):
        if is_logged_in:
            func()
        else:
            print("Please login first")
    return wrapper


@login_required
def sensitive_function():
    print("Access granted! Welcome.")


sensitive_function(True)
sensitive_function(False)
