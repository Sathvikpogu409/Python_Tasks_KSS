roles = {
    "Rahul": "admin",
    "Amit": "user"
}


def check_role(func):

    def wrapper(name):

        if roles.get(name) == "admin":
            return func(name)
        else:
            print("Access Denied")

    return wrapper


@check_role
def view_dashboard(name):
    print(name, "can view dashboard")


@check_role
def manage_users(name):
    print(name, "can manage users")


view_dashboard("Rahul")
manage_users("Amit")
