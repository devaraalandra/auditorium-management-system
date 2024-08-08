def is_username_taken(username):  # Function to check if the username has been taken
    with open("user_credentials.txt", "r") as file:
        for line in file:
            stored_username, *_ = line.strip().split(": ")
            if stored_username == username:
                return True
    return False

def register(username, password, account_type, first_name, last_name, dob, contact_number, email_address):
    """
    Function to register a new user by saving their credentials and additional information to a text file.
    Checks if the username is already taken before proceeding.
    """

    with open("user_credentials.txt", "a") as file:
        file.write(f"{username}: {password}: {account_type}: {first_name}: {last_name}: {dob}: {contact_number}: {email_address}\n")
    return True, "Registration successful!"

def login(username, password):
    """
    Function to check if the username and password are correct.
    """
    with open("user_credentials.txt", "r") as file:
        for line in file:
            stored_username, stored_password, user_type, *_ = line.strip().split(": ")
            if stored_username == username and stored_password == password:
                return True, user_type # Returns the output True and the variable user_type in database
    return False, None
