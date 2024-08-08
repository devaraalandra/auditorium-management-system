from tabulate import tabulate

def hall_management():
    # Creates a console for hall_management
    def add_h():  # Function to add new hall
        id = str(input("Please input the Hall ID: "))
        name = str(input("Please input the Hall name: "))
        description = str(input("Please input the Hall description: "))
        pax = int(input("Please input the Hall Pax: "))
        status = str(input("Please input the Hall status (available/unavailable): ")).lower()
        rate = int(input("Please input the Hall Rate (RM): "))
        def adding_hall(id, name, description, pax, status, rate):
            # Adds a new hall according to the inputted variables
            with open("hall_management.txt", "a") as file:
                file.write(f"{id}: {name}: {description}: {pax}: {status}: {rate}\n")

        adding_hall(id, name, description, pax, status, rate)

    def view_h(): # Views all halls
        print("\nViewing hall information...\n")

        hall_data = [] # Creates list to store hall_management.txt

        with open("hall_management.txt", "r") as file:
            for line in file:
                data = line.strip().split(": ") # Splits each line in hall_management and creates list 'data'
                hall_data.append(data) # Appends data to hall_data list

        if hall_data: # If hall_data is not empty
            print(tabulate(hall_data, headers=["Hall ID", "Name", "Description", "Pax", "Status", "Rate (RM)"],
                           tablefmt="grid")) # Prints a table using tabulate
        else:
            print("No hall information available.")

    def search_h():
        print("Searching specific hall information ...\n")

        print("What value would you like to search for?")
        print("1. Hall ID")
        print("2. Hall Name")
        print("3. Description")
        print("4. Hall @ Pax")
        print("5. Hall Status (Available/Unavailable)")
        print("6. Hall Rate (RM)")
        print("7. Exit back to Console")
        search_input = int(input("\n> Please choose a single option: "))

        if search_input == 7:
            print("Exitting...")
            return

        search_term = str(input("Enter the search term: ").lower())

        hall_data = []

        with open("hall_management.txt", "r") as file:
            for line in file:
                hall_info = line.strip().split(": ")
                if search_input != 5: # Excludes Hall Status option
                    if search_term in hall_info[search_input-1].lower(): # If search term is found in any hall info, then it will append to hall data
                        hall_data.append(hall_info)
                else:
                    if search_term == hall_info[4].lower(): # Search term is very specific to Hall Status
                        hall_data.append(hall_info)

        if hall_data:
            print("\n",tabulate(hall_data, headers=["Hall ID", "Name", "Description", "Pax", "Status", "Rate (RM)"],
                    tablefmt="grid"))
        else:
            print("No matching hall information found.")

        # Check if hall_data is not empty

    def edit_h():
        input_id = input("\nPlease enter a Hall ID to edit: ").lower() # Inputs hall ID to edit
        print("\n1. Hall ID")
        print("2. Hall Name")
        print("3. Description")
        print("4. Hall @ Pax")
        print("5. Hall Status")
        print("6. Hall Rate (RM)")
        user_input = int(input("\n> Please choose a single option to edit: ")) # Chooses field to edit

        if user_input == 1:
            new_id = input("Enter the new Hall ID: ").lower()
            # Check for ID uniqueness
            with open("hall_management.txt", "r") as file: # Reads hall_management to get data
                for line in file:
                    data = line.strip().split(": ") # Declares new list called 'data' to store hall info temporarily
                    if data[0] == new_id: # Checks if ID is unique
                        print("Error: Hall ID already exists.")
                        return
            update_value = new_id # If ID is indeed unique, then a variable new_value is declared with the value of new_id
        else:
            update_value = input("Enter the new value for the selected field: ")

        hall_data = [] # declares hall_data list to transfer new data
        found = False # declares 'found' boolean to check if hall info was successfully updated

        with open("hall_management.txt", "r") as file: # Reads hall_management to get data
            for line in file:
                data = line.strip().split(": ") # Re-declares new list 'data' because locally-stored
                if data[0] == input_id: # Checks if user input 'input_id' is in database
                    data[user_input - 1] = update_value # Replaces a value in 'data' list according to update_value; updates 'found' to True
                    found = True
                hall_data.append(": ".join(data)) # Appends 'data' list to 'hall_data'

        if found:
            with open("hall_management.txt", "w") as file: # Opens hall_management and enables write
                for line in hall_data: # get every line in hall_data and transfer to hall_management.txt
                    file.write(line + "\n")
            print("-- Hall information updated successfully.")
        else:
            print(f"-- Edit unsuccessful. Hall ID {input_id} was not found.")

    def delete_h():
        input_id = input("\nPlease enter a Hall ID to delete: ").lower() # Gets hall ID to delete

        hall_data = []
        found = False
        with open("hall_management.txt", "r") as file:
            for line in file: # Reads every line in 'hall_management.txt'
                data = line.strip().split(": ")
                if data[0] != input_id: # If hall ID is not equal to input_id, it stores it in hall_data
                    hall_data.append(line.strip())
                else:
                    found = True

        if found:
            with open("hall_management.txt", "w") as file:
                for line in hall_data:
                    file.write(line + "\n")
            print(f"-- Hall ID {input_id} was successfully deleted!")
        else:
            print(f"--Hall ID {input_id} was not found.")

    loop = True
    while loop:
        print("\nWhat would you like to access?")
        print("---")
        print("1. Enter new hall information")
        print("2. View every hall information")
        print("3. Search hall information")
        print("4. Edit hall information")
        print("5. Delete hall information")
        print("6. Exit")

        admin_input = int(input("\n> Please choose a single option: "))

        if (admin_input==1): # Admin Console Input #1 for Adding Halls
            add_h()
            input("\n Success! Press enter to return to the console.")
        elif (admin_input==2): # Admin Console Input #2 for Viewing All Hall Info
            view_h()
            input("\n Success! Press enter to return to the console.")
        elif (admin_input==3): # Admin Console Input #3 for Searching Hall Info
            search_h()
            input("\n Success! Press enter to return to the console.")
        elif (admin_input==4):
            edit_h()
            input("\n Success! Press enter to return to the console.")
        elif (admin_input==5):
            delete_h()
            input("\n Success! Press enter to return to the console.")
        elif (admin_input==6):
            input("\nExitting... press enter to return to the console.")
            admin_console()
        else:
            print("Please input a valid number!")

def booking_management():
    def view_b():
        print("\nViewing booking information...\n")

        booking_data = []  # Creates list to store booking_management.txt

        with open("booking_management.txt", "r") as file:  # Opens the file
            for line in file:  # Splits each line in booking_management and creates local list 'data'
                data = line.strip().split(": ")
                booking_data.append(data)  # Appends data to booking_data list

        if booking_data:  # if booking_data is not empty, show booking_data
            # Printing the data in a tabular format
            print(tabulate(booking_data,
                           headers=["Username", "User Email", "Event Name", "Event Description", "Hall ID", "Pax",
                                    "Date & Time", "Payment Amount", "Transaction ID"],
                           tablefmt="grid"))  # prints a table using tabulate
        else:  # If empty, output info unavailable
            print("No hall information available.")

    def search_b():
        print("Searching specific booking information ...\n")

        print("What value would you like to search for?")
        print("1. Username")
        print("2. User Email")
        print("3. Exit to console")

        search_input = int(input("\n> Please choose a single option: "))

        if search_input == 3:
            print("Exitting...")
            return
        elif search_input >= 1 and search_input <= 2:
            search_term = str(input("Enter the search term: ").lower())

            hall_data = []

            with open("booking_management.txt", "r") as file:
                for line in file:
                    hall_info = line.strip().split(": ")
                    if search_term in hall_info[
                        search_input - 1].lower():  # If search term is found in any hall info, then it will append to hall data
                        hall_data.append(hall_info)

            if hall_data:
                print("\n", tabulate(hall_data,
                                     headers=["Username", "E-mail", "Event Name", "Event Description", "Hall ID", "Pax",
                                              "Date & Time", "Payment Amount", "Transaction ID"],
                                     tablefmt="grid"))
            else:
                print("No matching hall information found.")
            print("Search booking information... ")

        else:
            print("please input valid number from the single option")
            search_b()

    def edit_b():
        input_username = input("\nPlease enter a username to edit: ").lower()  # Inputs username to edit
        print("\n1. Username")
        print("2. User Email")
        print("3. Event Name")
        print("4. Event Description")
        print("5. Hall ID")
        print("6. Pax")
        print("7. Date & Time")
        print("8. Payment Amount")
        print("9. Transaction ID")
        print("10. Exit to console")

        user_input = int(input("\n> Please choose a single option to edit: "))  # Chooses field to edit
        update_value = None

        if user_input == 10:
            print("Exitting...")
            return
        elif user_input == 1:
            new_username = input("Enter the new username: ").lower()
            # Check for username uniqueness
            with open("booking_management.txt", "r") as file:  # Reads booking_management to get data
                for line in file:
                    data = line.strip().split(": ")  # Declares new list called 'data' to store hall info temporarily
                    if data[0] == new_username:  # Checks if username is unique
                        print("Error: it is the same username.")
                        return
            update_value = new_username  # If username is indeed unique, then a variable update_value is declared with the value of new_username
        elif user_input >= 2 and user_input <= 9:
            update_value = input("Enter the new value/information for the selected field: ")
        else:
            print("please input valid number from the single option")
            edit_b()

        hall_booking = []  # declares hall_booking list to transfer new data
        found = False  # declares 'found' boolean to check if hall info was successfully updated

        with open("booking_management.txt", "r") as file:  # Reads booking_management to get data
            for line in file:
                data = line.strip().split(": ")  # Re-declares new list 'data' because locally-stored
                if data[0] == input_username:  # Checks if user input 'input_username' is in database
                    data[
                        user_input - 1] = update_value  # Replaces a value in 'data' list according to update_value; updates 'found' to True
                    found = True
                hall_booking.append(": ".join(data))  # Appends 'data' list to 'hall_booking'

        if found:
            with open("booking_management.txt", "w") as file:  # Opens booking_management and enables write
                for line in hall_booking:  # get every line in hall_booking and transfer to booking_management.txt
                    file.write(line + "\n")
            print("-- booking management information updated successfully.")
        else:
            print(f"-- Edit unsuccessful. Hall ID {input_username} was not found.")

    def delete_b():
        input_username = input("\nPlease enter a Hall ID to delete: ").lower()  # Gets username to delete

        hall_booking = []
        found = False
        with open("booking_management.txt", "r") as file:
            for line in file:  # Reads every line in 'booking_management.txt'
                data = line.strip().split(": ")
                if data[0] != input_username:  # If username is not equal to input_username, it stores it in hall_booking
                    hall_booking.append(line.strip())
                else:
                    found = True

        if found:
            with open("booking_management.txt", "w") as file:
                for line in hall_booking:
                    file.write(line + "\n")
            print(f"-- Hall ID {input_username} was successfully deleted!")
        else:
            print(f"--Hall ID {input_username} was not found.")
        # print("Delete ")

    loop = True
    while loop:
        print("\nBooking Management")
        print("---")
        print("1. View all booking information")
        print("2. Search for booking information")
        print("3. Edit booking information")
        print("4. Delete/cancel booking information")
        print("5. Return to console")

        admin_input = int(input("\n> Please choose a single option: "))

        if (admin_input == 1):
            view_b()
            input("\n Success! Press enter to return to the console.")
        elif (admin_input == 2):
            search_b()
        elif (admin_input == 3):
            edit_b()
        elif (admin_input == 4):
            delete_b()
        elif (admin_input == 5):
            input("\nExitting... press enter to return to the console.")
            admin_console()
        else:
            print("Please input a valid number!")
def user_management():
    def view_u():
        print("\nViewing user credentials...\n")

        user_data = []  # Creates list to store user_credentials.txt

        with open("user_credentials.txt", "r") as file:  # Opens the file
            for line in file:
                data = line.strip().split(": ")  # Splits each line in user_credentials and creates local list 'data'
                user_data.append(data)  # Appends data to user_data list

        if user_data:  # If user_data is not empty, show user_data
            print(tabulate(user_data,headers=["Username", "Password", "User Type", "First Name", "Last Name", "DOB", "Phone No.",
                                    "Email Address"],
                           tablefmt="grid"))  # Prints a table using tabulate
        else:  # If empty, output info unavailable
            print("No hall information available.")

    def search_u():
        print("Searching specific user credentials ...\n")

        print("What value would you like to search for?")
        print("1. Username")
        print("2. Password")
        print("3. User Type")
        print("4. First Name")
        print("5. Last Name")
        print("6. DOB (YYYY-MM-DD)")
        print("7. Phone No.")
        print("8. Email Address")
        print("9. Exit to console")
        search_input = int(input("\n> Please choose a single option: "))

        if search_input == 9:
            print("Exitting...")
            return
        elif search_input >= 1 and search_input <= 8:
            search_term = str(input("Enter the search term: ").lower())

            user_data = []

            with open("user_credentials.txt", "r") as file:
                for line in file:
                    hall_info = line.strip().split(": ")
                    if search_term in hall_info[
                        search_input - 1].lower():  # If search term is found in any hall info, then it will append to hall data
                        user_data.append(hall_info)

            if user_data:
                print("\n",tabulate(user_data,
                               headers=["Username", "Password", "User Type", "First Name", "Last Name", "DOB",
                                        "Phone No.",
                                        "Email Address"],
                               tablefmt="grid"))
            else:
                print("No matching hall information found.")
        else:
            print("Please input a valid number")
            search_u()

    def edit_u():
        print("Edit user information... ")
        input_username = input("\nPlease enter a username to edit: ").lower()  # Inputs username to edit
        print("1. Username")
        print("2. Password")
        print("3. User Type")
        print("4. First Name")
        print("5. Last Name")
        print("6. DOB (YYYY-MM-DD)")
        print("7. Phone No.")
        print("8. Email Address")
        print("9. Exit to console")
        search_input = int(input("\n> Please choose a single option:"))
        update_value = None

        if search_input == 1:
            new_username = input("Enter the new username: ").lower()
            # Check for username uniqueness
            with open("user_credentials.txt", "r") as file:  # Reads user_credentials to get data
                for line in file:
                    data = line.strip().split(": ")  # Declares new list called 'data' to store hall info temporarily
                    if data[0] == new_username:  # Checks if username is unique
                        print("Error: it is the same username")
                        return
            update_value = new_username  # If username is indeed unique, then a variable update_value is declared with the value of new_username
        elif search_input >= 2 and search_input <= 8:
            update_value = input("Enter the new value for the selected field: ")
        else:
            print("please input a valid number!")
            edit_u()

        hall_user = []  # declares hall_user list to transfer new data
        found = False  # declares 'found' boolean to check if user info was successfully updated

        with open("user_credentials.txt", "r") as file:  # Reads user_credentials to get data
            for line in file:
                data = line.strip().split(": ")  # Re-declares new list 'data' because locally-stored
                if data[0] == input_username:  # Checks if user input 'input_username' is in database
                    data[
                        search_input - 1] = update_value  # Replaces a value in 'data' list according to update_value; updates 'found' to True
                    found = True
                hall_user.append(": ".join(data))  # Appends 'data' list to 'hall_user'

        if found:
            with open("user_credentials.txt", "w") as file:  # Opens user_credentials and enables write
                for line in hall_user:  # get every line in hall_user and transfer to user_credentials.txt
                    file.write(line + "\n")
            print("-- Hall information updated successfully.")
        else:
            print(f"-- Edit unsuccessful. Hall ID {input_username} was not found.")

    def delete_u():
        print("\n Delete or Block")
        print("---")
        print("1. Block User")
        print("2. Delete")
        print("3. Return")
        search_input = int(input("\nPlease choose a single option:"))  # input delete or block option to proceed

        def block_user(username):
            user_data = []  # Creates list to store user_credentials.txt
            with open("user_credentials.txt", "r") as file:
                for line in file:  # Reads every line in 'user_credentials.txt'
                    data = line.strip().split(": ")
                    if data[0] == username:
                        data[-1] = "blocked"
                        user_data.append(": ".join(data) + "\n")  # input 'blocked' at the end of the data in user_data
                        continue
                    user_data.append(line.strip())

            with open("user_credentials.txt", "w") as file:
                for line in user_data:
                    file.write(line + "\n")
            print(f"-- User {username} was successfully blocked!")

        def delete_user(username):
            user_data = []  # Creates list to store user_credentials.txt
            found = False  # to find username that does not match to the data and will be stored in user_data
            with open("user_credentials.txt", "r") as file:
                for line in file:
                    data = line.strip().split(": ")
                    if data[
                        0] != username:  # to check if the username matches the data or not, if no it will be stored to 'user_data' list
                        user_data.append(line.strip())
                    else:
                        found = True

            if found:
                with open("user_credentials.txt", "w") as file:
                    for line in user_data:
                        file.write(
                            line + "\n")  # the data that stored to the new list 'user_data' will replace 'user_credentials.txt'
                print(f"-- Username {username} was successfully deleted!")
            else:
                print(f"-- Username {username} was not found.")

        if search_input == 1:
            input_username = input("\nPlease enter a username to block: ")
            block_user(input_username)

        elif search_input == 2:
            input_username = input("\nPlease enter a username to delete: ")
            delete_user(input_username)

        elif search_input == 3:
            print("Returning to menu.")
            return
        else:
            print(" please input a valid number")
            delete_u()

    loop = True
    while loop:
        print("\nUser Management")
        print("---")
        print("1. View all user credentials")
        print("2. Search for user information")
        print("3. Edit user information")
        print("4. Delete/block user information")
        print("5. Return to console")

        admin_input = int(input("\n> Please choose a single option: "))

        if (admin_input == 1):
            view_u()
            input("\n Success! Press enter to return to the console.")
        elif (admin_input == 2):
            search_u()
        elif (admin_input == 3):
            edit_u()
        elif (admin_input == 4):
            delete_u()
        elif (admin_input == 5):
            input("\nExitting... press enter to return to the console.")
            admin_console()
        else:
            print("Please input a valid number!")

def admin_console():
    print("\nWhat would you like to do today?")
    print("---")
    print("1. Hall Management")
    print("2. Booking Management")
    print("3. User Management")
    print("4. Logout")
    option_input = input("\nPlease choose a single option: ")
    if option_input == '1':
        hall_management()
    elif option_input == '2':
        booking_management()
    elif option_input == '3':
        user_management()
    elif option_input == '4':
        input("\nExitting... Press enter to return to login")
        return True
    else:
        print("Please input a valid number!")