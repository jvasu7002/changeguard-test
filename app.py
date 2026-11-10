def login(password):
    if password == "admin123":
        return True
    return False


def dashboard(password):
    if login(password):
        return "Welcome"
    return "Access denied"