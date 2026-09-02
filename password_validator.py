# Password Validation Program (without loops or if-else)
# Check if password contains @ and has at least 8 characters

password = input("Enter a password: ")

# Validation using boolean operations
is_valid = ('@' in password) and (len(password) >= 8)

# Print using list indexing (no if-else or ternary)
print(["✗ Password is invalid!", "✓ Password is valid!"][is_valid])
