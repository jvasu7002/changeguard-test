def login(password):
    if password == "admin123":
        return password == "admin123"
    return False


def dashboard(password):
    if login(password):
        return "Welcome to ChangeGuard"
    return "Access denied"