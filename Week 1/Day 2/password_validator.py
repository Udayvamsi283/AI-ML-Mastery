def is_valid_password(password):
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    return True

password = input("Enter a password: ")
if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is not valid.")