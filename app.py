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

def format_status(status):
    return status.upper()

def calculate_total(price, quantity):
    discount = 20
    tax = 5
    return (price * quantity) - discount + tax


def generate_invoice(price, quantity):
    total = calculate_total(price, quantity)
    return f"Invoice Total: {total}"

def send_invoice_email(price, quantity):
    total = calculate_total(price, quantity)
    return f"Email sent with total: {total}"


def save_invoice(price, quantity):
    total = calculate_total(price, quantity)
    return f"Invoice saved: {total}"


def print_invoice(price, quantity):
    total = calculate_total(price, quantity)
    return f"Invoice printed: {total}"

def export_invoice(price, quantity):
    total = calculate_total(price, quantity)
    return f"Exported: {total}"


def audit_invoice(price, quantity):
    total = calculate_total(price, quantity)
    return f"Audited: {total}"