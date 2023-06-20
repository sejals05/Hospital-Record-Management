#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("\nHello! Welcome to the Hospital Management Program.")
import pandas as pd

class Node:
    def __init__(self, data):
        self.item = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def insert(self, name, age, gender, address, weight, height):
        details = [name, age, gender, address, weight, height]
        df = pd.DataFrame([details])
        df.to_csv('new.csv', mode='a', index=False, header=False)

        new_node = Node(details)
        if self.front is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def display_names(self):
        try:
            df = pd.read_csv('new.csv', header=None)
            if df.empty:
                print("The waiting list is empty")
            else:
                print("Waiting List:")
                print("Name")
                print(df[0].to_string(index = None,header = None))
        except FileNotFoundError:
            print("The waiting list file does not exist or is empty")

    def search(self, name):
        try:
            df = pd.read_csv('new.csv', header=None)
            result = df[df[0] == name]
            if result.empty:
                print("Patient not found.")
            else:
                print("Patient details:")
                print('Name Age Gender Address Weight Height')
                print(result.to_string(index=False, header= False))
        except FileNotFoundError:
            print("The waiting list file does not exist or is empty")

    def doctors(self):
        try:
            hosp = pd.read_csv('hosp.csv', header=None)
            doctors = hosp[0].tolist()
            if doctors:
                print("Doctors who are working today:")
                for doctor in doctors:
                    print(doctor)
            else:
                print("No doctors are available.")
        except FileNotFoundError:
            print("The hospital details file does not exist")

    def ambulance(self):
        try:
            hosp = pd.read_csv('hosp.csv', header=None)
            ambulances = hosp[1][1]
            print("The number of ambulances available:", ambulances)
        except FileNotFoundError:
            print("The hospital details file does not exist")

    def beds(self):
        try:
            hosp = pd.read_csv('hosp.csv', header=None)
            beds = hosp[2][1]
            print("The number of beds available:", beds)
        except FileNotFoundError:
            print("The hospital details file does not exist")

def main():
    ob = Queue()
    while True:
        print("\nWelcome to the Hospital Queue System")
        print("1. If you are a staff")
        print("2. If you are a patient")
        print("0. To Exit")
        choice = int(input("Enter your choice: "))

        if choice == 0:
            print("Exiting the program.")
            break
        elif choice == 1:
            while True:
                print("\n--- Staff Options ---")
                print("1. Find patient details")
                print("2. View list of doctors")
                print("3. View the number of ambulances")
                print("4. View the number of beds")
                print("0. Go back")
                sel = int(input("Enter your choice: "))

                if sel == 0:
                    print("Going back to the main menu.")
                    break
                elif sel == 1:
                    name = input("Enter the patient name: ")
                    ob.search(name)
                elif sel == 2:
                    ob.doctors()
                elif sel == 3:
                    ob.ambulance()
                elif sel == 4:
                    ob.beds()
                else:
                    print("Invalid choice. Please try again.")
        elif choice == 2:
            while True:
                print("\n--- Patient Options ---")
                print("1. Enter your details")
                print("2. View the waiting list")
                print("3. View list of doctors")
                print("0. Go back")
                ch = int(input("Enter your choice: "))

                if ch == 0:
                    print("Going back to the main menu.")
                    break
                elif ch == 1:
                    name = input("Enter your name: ")
                    age = int(input("Enter your age: "))
                    gender = input("Enter your gender (Male or Female): ")
                    address = input("Enter your address: ")
                    weight = int(input("Enter your weight (kg): "))
                    height = int(input("Enter your height (cm): "))
                    ob.insert(name, age, gender, address, weight, height)
                    print("Your details have been added to the waiting list.")
                elif ch == 2:
                    ob.display_names()
                elif ch == 3:
                    ob.doctors()
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Invalid choice. Please try again.")


main()


# In[ ]:





# In[ ]:




