# Hospital-Record-Management
## Hospital Queue System
The "Hospital Queue System" is a program that manages a queue of patients in a hospital. It allows staff members and patients to perform various operations related to patient management.
## Objectives:
* To help hospital staff find patient details easily and find the number of ambulances.
* To help hospital staff to be updated about available doctors, the number of ambulances and the number of beds.
* To help patients view the waiting and view the available doctors 

## Libraries Used
* pandas: A library for data manipulation and analysis. It is used to read and write data to CSV files.
Class and Data Structure
Node Class
* The Node class represents a node in a linked list. Each node holds a patient's details.
Queue Class
* The Queue class implements the queue data structure to manage the waiting list of patients.
* The class has the following methods:
* insert(name, age, gender, address, weight, height): Inserts a patient's details into the queue and saves it to a CSV file.
* display_names(): Displays the list of patients in the waiting list.
* search(name): Searches for a patient in the waiting list by name and displays their details.
* doctors(): Displays the list of doctors working today.
* ambulance(): Displays the number of ambulances available.
* beds(): Displays the number of beds available.
## Main Function
The main function is the entry point of the program. It creates an instance of the Queue class and provides a menu-driven interface for staff and patients to interact with the system.
The main menu presents the following options:
* Staff:
  * Find patient details: Allows staff to search for a patient by name and view their details.
  * View list of doctors: Displays the list of doctors working today.
  * View the number of ambulances: Shows the number of available ambulances.
  * View the number of beds: Shows the number of available beds.
* Patients:
  * Enter your details: Patients can enter their personal details to be added to the waiting list.
  * View the waiting list: Displays the list of patients in the waiting list.
  * View list of doctors: Shows the list of doctors working today.
  The program continues to run until the user chooses to exit by selecting the "0" option.
## Running the Program
To run the program:
  * The pandas library must be installed.
  * The program starts by displaying a welcome message and presents a menu for staff and patients to select their roles.
  * Staff members can perform operations related to patient management, such as finding patient details, viewing doctors, ambulances, and 
    beds.
  * Patients can enter their personal details, view the waiting list, and see the list of doctors.
  * The program loops until the user chooses to exit.
  Note: The program assumes the existence of two CSV files, new.csv for storing patient details and hosp.csv for storing hospital details (doctors, ambulances, beds). If these files are missing, the program will display appropriate error messages.
  That's an overview of the code's functionality and how to run it. 
## Error Handling
The program includes basic error handling to handle missing files or empty lists. If the waiting list file (new.csv) or hospital details file (hosp.csv) is not found or empty, appropriate error messages are displayed to the user
## Usage and Deployment
To use the program, follow these steps:
  * Ensure that Python is installed on your system.
  * Install the required pandas library using the command pip install pandas.
  * Save the code in a Python file (e.g., hospital_queue_system.py).
  * Run the program by executing the Python file using the command python hospital_queue_system.py.
## Conclusion
The Hospital Queue System is a simple program that demonstrates the management of a patient waiting list in a hospital. It provides staff members and patients with an interface to perform various operations, including adding patient details, searching for patients, and viewing hospital information. The program can be customized and expanded upon to meet specific requirements, such as integrating with a database or adding additional functionalities.
