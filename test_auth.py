from authentication import register_user, login_user

# Test registration
print(register_user("ayush", "mypassword"))

# Test login (correct password)
success, msg = login_user("ayush", "mypassword")
print(msg)

# Test login (wrong password)
success, msg = login_user("ayush", "wrongpass")
print(msg)
