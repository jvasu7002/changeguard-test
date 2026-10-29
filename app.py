def login(password):
    if password == "admin":
        return True
    return False


def dashboard(password):
    if login(password):
        return "Welcome"
    return "Access denied"