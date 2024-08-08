from custom_login import *
from user_console import *
from admin_console import *

def main():
    login_loop = True
    print("\nWelcome to Hall Symphony Inc!")
    while True:
        action = input("\nWould you like to login or register? (type R to register) ")

        # Common inputs for both login and registration
        print("\n   ====================   ")

        if action.lower() == "r":
            username = input("Enter your username: ")
            if is_username_taken(username):
                print("-- The username has already been taken. Please try again. --")
                continue
            password = input("Enter your password: ")
            # Additional inputs for registration
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            dob = input("Enter your date of birth (YYYY-MM-DD): ")
            contact_number = input("Enter your contact number: ")
            email_address = input("Enter your email address: ")

            register(username, password, "user", first_name, last_name, dob, contact_number, email_address)
            print(f"User registration of {username} was successful! You can now login.")

        else:
            # Login process
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            success, user_type = login(username, password)
            if success == True:
                if user_type == "admin":
                    print(f"\nAdmin login successful!\nWelcome, admin {username}!")
                    admin_console()
                elif user_type == "user":
                    print(f"\nUser login successful!\nWelcome, user {username}!")
                    user_console(username)
                login_loop = False
            else:
                print("Invalid username or password. Please try again.")


if __name__ == "__main__":
    main()