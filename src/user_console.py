from tabulate import tabulate
def user_console(username):  # Function to output user console in main.py
    def get_user_email(username):  # Function to get user email using username
        with open("user_credentials.txt", "r") as file:  # Open user_credentials.txt as read
            for line in file:
                user_data = line.strip().split(": ")  # Splits each line in user_credentials.txt and creates list 'user_data'
                if user_data[0].lower() == username.lower():  # Checks line if the username is same, and returns the email
                    return user_data[7]  # Return email
        return None

    def update_hall_availability(hall_id, new_status):  # Function to update hall availability according to hall_id
        hall_data = []  # New list
        with open("hall_management.txt", "r") as file: # Open txt file as read
            for line in file:
                data = line.strip().split(": ")  # Splits each line in user_credentials.txt and creates local list 'data'
                if data[0] == hall_id:  # Checks if Hall ID is equal to hall_id parameter
                    data[4] = new_status  # Updates availability status in data list
                hall_data.append(data)  # Appends to hall_data list

        with open("hall_management.txt", "w") as file: # Open txt file as write
            for hall in hall_data:
                file.write(": ".join(map(str, hall)) + "\n")  # Convert 'hall_data' elements into a string and join them with ': ' into the file

    def user_booking(username):  # Function to create new user booking
        email_address = get_user_email(username)  # Declares variable email_address using function 'get_user_email' and 'username'

        def is_hall_available(hall_id):  # Function to check the hall availability according to ID
            with open("hall_management.txt", "r") as file:  # Open hall_management.txt file as read
                for line in file:
                    data = line.strip().split(": ")  # Splits each line in txt file and creates local list 'data'
                    if data[0].lower() == hall_id and data[4].lower() == "available": # Checks if Hall ID matches and is available
                        return True  # Returns value True and the capacity of the hall  # Returns True
            return False  # If none are available, returns false

        # Function to check if payment is sufficient
        def is_payment_sufficient(payment, hall_id):  # Function to check if payment is enough to pay for specific hall
            hall_rate = 0  # Declares 'hall_rate' variable as integer
            with open("hall_management.txt", "r") as file:  # Open txt file as write
                for line in file:
                    data = line.strip().split(": ")  # Splits each line in txt file and creates local list 'data'
                    if data[0] == hall_id:  # Checks if Hall ID matches
                        hall_rate = float(data[5])  # Declares hall_rate according to hall info's rate and exits loop
                        break

            return payment >= hall_rate  # Returns boolean that determines if payment is more or equal than Hall Rate

        def is_pax_suitable(hall_id, pax):  # Read hall data to check if pax is suitable with hall
            hall_capacity = 0  # Declares variable 'hall_capacity' as integer
            with open("hall_management.txt", "r") as file:   # Open txt file as write
                for line in file:
                    data = line.strip().split(": ")  # Splits each line in user_credentials.txt and creates local list 'data'
                    if data[0] == hall_id:  # Checks if Hall ID matches
                        hall_capacity = int(data[3])  # Declares hall_capacity as pax according to hall info
                        break
            return pax <= hall_capacity # Returns boolean that determines if Pax is less or equal than hall_capacity



        event_name = input("Please enter your event name: ")  # Input event name
        event_description = input("Please input your event's description: ")  # Input event description

        while True:  # While loop to check hall availability
            hall_id = input("Please enter the ID for the hall you'd like to use: ")  # input hall ID
            hall_available = is_hall_available(hall_id)  #checks hall availability
            if hall_available:
                break  # If hall is available, break while loop and continue
            else:
                print("\nSorry! The Hall ID was either booked or not found in our database. Returning to console.\n -- Please try again.")
                return  # Returns to console if not available

        while True:  # While loop to check pax suitability
            pax = int(input("Please enter the number of Pax for your event: "))  # input pax
            if is_pax_suitable(hall_id, pax):  # If pax is suitable, break while loop and continue
                break
            else:
                print(f"\nThe hall cannot accommodate {pax} people. \n-- Please choose a different hall type.")
                return  # Returns to console if not available

        event_date = input("Please input the date and time of your event: (YYYY-MM-DD xx.xx-xx.xx) ")  # Input the event date

        while True:  # While loop to check payment amount
            payment_amount = float(input("Please input the amount of payment for your booking: "))  # inputs payment amount
            if is_payment_sufficient(payment_amount, hall_id):  # If payment is sufficient, ask for  payment transaction ID, break while loop and continue
                transaction_id = input("Enter your payment transaction ID: ")
                break
            else:
                print("\nInsufficient payment. Returning to console.\n -- Please enter the correct amount.")
                return  # Return to console if payment is unsufficient

        with open("booking_management.txt", "a") as file:  # Opens booking_management.txt using append
            file.write(f"{username}: {email_address}: {event_name}: {event_description}: {hall_id}: {pax}: {event_date}: {payment_amount}: {transaction_id}\n")  # Writes all the variables into the file
        print(f"Booking successfully recorded. Hall ID {hall_id} was successfully booked.")

        update_hall_availability(hall_id, "unavailable")  # Updates the hall_id as unavailable

    def view_past_bookings(username):  # Views all halls
        print("\nViewing hall information...\n")

        hall_data = []  # Creates list to store hall_management.txt

        with open("booking_management.txt", "r") as file:
            for line in file:
                data = line.strip().split(": ")  # Splits each line in hall_management and creates list 'data'
                if data[0] == username:
                    hall_data.append(data[2:])  # Appends data to hall_data list

        if hall_data:  # If hall_data is not empty
            print(tabulate(hall_data, headers=["Event Name", "Description", "Hall ID", "Pax", "Date and Time",
                                               "Payment Amount (RM)", "Transaction ID"],
                           tablefmt="grid"))  # Prints a table using tabulate
        else:
            print("No booking information available.")

    def search_booking(username):  # Function to search booking according to username
        print("Searching specific booking information ...\n")

        print("What value would you like to search for?")  # Asks for the field to search
        print("1. Event name")
        print("2. Event description")
        print("3. Hall ID")
        print("4. Number of Pax")
        print("5. Date and Time of Renting")
        print("6. Payment Amount")
        print("7. Transaction ID")
        print("8. Exit back to Console")
        search_input = int(input("\n> Please choose a single option: "))  # Input the option

        if search_input == 8:  # Exit option
            print("Exitting...")
            return

        search_term = str(input("Enter the search term: ").lower())  # Input search term

        booking_data = []  # Creates empty 'booking_data' list

        with (open("booking_management.txt", "r") as file):  # Opens txt file as read
            for line in file:
                booking_info = line.strip().split(": ")  # Splits each line in booking_management and creates local list 'booking_info'
                if username == booking_info[0].lower():  # Checks if username matches
                    if search_term in booking_info[search_input+1].lower():  # If search term is found in booking info, append to hall data
                        booking_data.append(booking_info[2:])  # Excludes username and email

        if booking_data:
            print("\n",tabulate(booking_data, headers=["Event Name", "Description", "Hall ID", "Pax", "Date & Time", "Payment Amount", "Transaction ID"],
                    tablefmt="grid"))
        else:
            print("No matching hall information found.")

    def edit_bookings(username):
        input_id = input("\nEnter your hall ID: ")  # Inputs hall ID to edit
        print("\n1. Event Name")
        print("2. Event Description")
        user_input = input("\n> Please choose a single option to edit: ")  # Chooses field to edit

        if user_input == '1':
            new_name = input("Enter the new event description: ").lower()
            # Check for description uniqueness
            with open("booking_management.txt", "r") as file:  # Reads booking_management to get data
                booking_data = []
                updated = False
                for line in file:
                    data = line.strip().split(": ")  # Declares new list called 'data' to store booking info temporarily
                    if data[4] == input_id:
                        if data[2] == new_name:
                            print("There is no changes")
                            return
                        data[2] = new_name
                        updated = True
                    booking_data.append(": ".join(data) + "\n")
                if not updated:
                    print("Error: Hall ID not found")
                else:
                    with open("booking_management.txt", "w") as file:
                        file.writelines(booking_data)
                        print("-- Booking information updated successfully.")

        elif user_input == '2':
            new_description = input("Enter the new value for the selected field: ")
            with open("booking_management.txt", "r") as file:  # Reads booking_management to get data
                booking_data = []
                updated = False
                for line in file:
                    data = line.strip().split(": ")  # Declares new list called 'data' to store booking info temporarily
                    if data[4] == input_id:
                       if data[3] == new_description:
                        print("There is no changes")
                        return
                       data[3] = new_description
                       updated = True
                    booking_data.append(": ".join(data) + "\n")
                if not updated:
                    print("Error: Hall ID not found")
                else:
                    with open("booking_management.txt", "w") as file:
                        file.writelines(booking_data)
                        print("-- Booking information updated successfully.")
        else:
            print("Your input is invalid, please try again!")

    def delete_bookings(username):
        input_id = input("\nPlease enter a Hall ID to delete: ").lower()  # Gets hall ID to delete
        hall_data = []
        found = False
        with open("booking_management.txt", "r") as file:
            for line in file:  # Reads every line in 'booking_management.txt'
                data = line.strip().split(": ")
                if len(data) >= 5 and data[4] == input_id and data[0] == username:  # Check the length of data before accessing index 4
                    found = True
                else:
                    hall_data.append(line.strip())

        if found:
            with open("booking_management.txt", "w") as file:
                for line in hall_data:
                    file.write(line + "\n")
            print(f"-- Hall ID {input_id} for user {username} was successfully deleted!")
        else:
            print(f"-- Hall ID {input_id} for user {username} was not found.")

    def update_profile(username):
        print("\n1. Username")
        print("2. Password")
        print("3. First Name")
        print("4. Last Name")
        print("5. Contact Number")
        print("6. Date of Birth")
        print("7. Email")
        print("8. Exit to console")

        user_input = int(input("\n> Please choose a single option to update: "))  # Gets user input

        if user_input == 8:
            print("Exiting...")
            return

        if user_input == 1:
            new_id = input("Enter the new username: ").lower()
            # Checks for ID uniqueness
            with open("user_credentials.txt", "r") as file:  # Opens user_credentials.txt as read
                for line in file:
                    data = line.strip().split(": ")  # Declares 'data' list
                    if data[0] == new_id:  # If username database matches new_input, outputs error
                        print("Error: Username already exists.")
                        return
            update_value = new_id
        elif 2 <= user_input <= 7:  # Options other than username
            update_value = input("Enter the new value for the selected field: ")
        else:
            print("Please input a valid number")  # Error for valid number
            return

        user_data = []  # Declares 'user_data' variable
        found = False  # Declares 'found' variable

        with open("user_credentials.txt", "r") as file:  # Opens user_credentials.txt as read
            for line in file:
                data = line.strip().split(": ")  # Declares 'data' list
                if data[0] == username:  # If username matches database
                    if user_input >= 3:  # Value over 3 to exclude user/admin status
                        data[user_input] = update_value  # Updates value accordingly
                    else:  # If value is 2, slicing index equals to 1
                        data[user_input - 1] = update_value
                    found = True  # found declared as true
                user_data.append(": ".join(data))  # Appends to 'data' list

        if found:
            with open("user_credentials.txt", "w") as file:  # Opens user_credentials.txt as write
                for line in user_data:  # Writes into file
                    file.write(line + "\n")
            print("-- User information updated successfully.")
        else:  # Error text
            print(f"-- Edit unsuccessful. User {username} was not found.")

    loop = True
    while loop:
        print("\nWhat would you like to do today?")
        print("---")
        print("1. Book a new event")
        print("2. View past booking information")
        print("3. Search for booking information")
        print("4. Edit a booking information")
        print("5. Delete a booking information")
        print("6. Update my profile information")
        print("7. Logout")

        user_input = input("\n> Please choose a single option: ")

        if (user_input=="1"): # Admin Console Input #1 for Adding Halls
            user_booking(username)
            input("\n Success! Press enter to return to the console.")
        elif (user_input=="2"): # Admin Console Input #2 for Viewing All Hall Info
            view_past_bookings(username)
            input("\n Success! Press enter to return to the console.")
        elif (user_input=="3"): # Admin Console Input #3 for Searching Hall Info
            search_booking(username)
            input("\n Success! Press enter to return to the console.")
        elif (user_input=="4"):
            edit_bookings(username)
            input("\n Success! Press enter to return to the console.")
        elif (user_input=="5"):
            delete_bookings(username)
            input("\n Success! Press enter to return to the console.")
        elif (user_input=="6"):
            update_profile(username)
            input("\n Success! Press enter to return to the console.")
        elif (user_input=="7"):
            input("\nExitting... Press enter to return to login")
            return True
        else:
            print("Please input a valid number!")