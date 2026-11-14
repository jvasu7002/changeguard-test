def login(password):
    if password == "admin123":
        return True
    return False


def dashboard(password):
    if login(password):
        return "Welcome to ChangeGuard"
    return "Access denied"


def user_profile(password):
    if login(password):
        return "User profile opened"
    return "Please login first"