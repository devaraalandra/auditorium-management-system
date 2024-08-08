# Auditorium Management System

This Auditorium Management System is the final project of my group's Python Module in APU. It is a console based app designed to manage halls, bookings, and users efficiently. Below is a detailed overview of the system's features and functionalities.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
  - [Admin Features](#admin-features)
  - [Manager Features](#manager-features)
  - [Worker Features](#worker-features)
  - [Customer Features](#customer-features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributors](#contributors)
- [Acknowledgments](#acknowledgments)

## Introduction

The Auditorium Management System is a comprehensive tool designed to streamline the management of halls, bookings, and user accounts. Developed as the final project for my Python Module, this system leverages Python and the `tabulate` library to create an efficient, user-friendly console application.

## Features

### Admin Features

- **Add Hall**: Allows administrators to add new halls with detailed information such as ID, name, description, capacity, status, and rate.
- **View Halls**: Provides a tabulated view of all halls in the system, making it easy to review and manage available spaces.
- **Search Hall**: Enables searching for specific halls based on various criteria like ID, name, description, capacity, status, and rate, ensuring quick access to needed information.
- **Edit Hall**: Facilitates the editing of existing hall information to keep data up-to-date.
- **Delete Hall**: Allows administrators to delete hall records from the system, maintaining an accurate database.
- **View Bookings**: Administrators can view all booking information in a tabulated format for comprehensive monitoring.
- **Search Bookings**: Enables searching for specific booking details based on multiple parameters.
- **Edit Bookings**: Allows administrators to edit booking information, ensuring accuracy.
- **Delete Bookings**: Facilitates the deletion of bookings, keeping the system clean and organized.
- **View Users**: Provides a comprehensive view of all user credentials, helping in managing user access.
- **Search Users**: Enables searching for specific user information quickly.
- **Edit Users**: Allows administrators to edit user details, including passwords and profile information.
- **Delete Users**: Facilitates the deletion or blocking of user accounts, enhancing security.

### Manager Features

- **Assign Job**: Allows managers to assign jobs to workers based on requests, ensuring efficient task distribution.
- **View Modes**: Displays all requests and their assigned workers, providing a clear overview of ongoing tasks.
- **Edit Profile**: Enables managers to update their profile information to keep records current.

### Worker Features

- **Update Jobs**: Allows workers to update the status of their assigned jobs, providing real-time progress updates.
- **View Jobs**: Displays all requests assigned to the worker with options to filter and search, enhancing task management.
- **Edit Profile**: Enables workers to update their profile information, ensuring personal data is accurate.

### Customer Features

- **View Services**: Displays available services to the customer, making it easy to explore options.
- **Make Requests**: Facilitates the creation and confirmation of service requests, streamlining the booking process.
- **View Status**: Shows the status of the customer's requests, providing transparency.
- **Edit Profile**: Allows customers to update their profile information, ensuring contact details are current.

## Getting Started

### Prerequisites

- Python 3.x
- `tabulate` library

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/auditorium-management-system.git
   ```

2. Navigate to the project directory:

   ```sh
   cd auditorium-management-system
   ```

3. Install the required dependencies:

   ```sh
   pip install tabulate
   ```

4. Run the application:

   ```sh
   python main.py
   ```

## Usage

- **Login**: Use the login functionality to access the system as an admin, manager, worker, or customer.
- **Navigation**: Navigate through the various features using the console prompts.

## Screenshots

### Admin Dashboard
*To be added*

### Hall Management
*To be added*

### Booking Management
*To be added*

### User Management
*To be added*

## Future Enhancements

- **Web-Based Interface**: Transition from a console-based application to a web-based interface for better accessibility and user experience.
- **Automated Notifications**: Implement email or SMS notifications for booking confirmations, cancellations, and reminders.
- **Advanced Analytics**: Integrate advanced analytics to provide insights into hall usage, booking patterns, and user activity.
- **Mobile Application**: Develop a mobile application to allow users to manage bookings and view information on the go.
- **Enhanced Security**: Implement multi-factor authentication and enhanced security protocols to protect user data.
- **API Integration**: Provide APIs for integrating the system with other applications or services.

## Contributors

- [Devara Alandra Wicaksono](https://github.com/devaraalandra) (Lead Developer; *Developed significant foundations for Login System, Customer, Admin, Manager, and Worker section*)
- [Gilang Eko Vinanda](https://github.com/Gjlang) (Senior Developer; *Enhanced and implemented complex customer features*)
- Fernando Salim
- Kobalen Khaniska Arasen

## Acknowledgments

Special thanks to our Python course instructor, Dr. Muhammad Huzaifah Ismail, for his guidance on our booking database management system and continuous support throughout this project.
