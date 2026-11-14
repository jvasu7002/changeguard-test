def login(password):
    if password == "newpassword123":
        return True
    return False

def dashboard(password):
    if login(password):
        return "Welcome to ChangeGuard"
    return "Access denied"


def generate_report(password):
    if dashboard(password) == "Welcome to ChangeGuard":
        return "Report generated successfully"
    return "Report generation failed"


def user_profile(password):
    if login(password):
        return "User profile opened"
    return "Please login first"