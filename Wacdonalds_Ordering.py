
"""A program that can be used at Wacdonalds Queenstown to enter customer details, food orders and pick-up or delivery requirements into a computer and have it display the delivery details, itemised order, and total cost.
"""
import os
import time


# 2D list of customer_details in which there is 
# order in name, adress, phone number
customer_details = [["NAME1", "ADDRESS1", "PHONE NUMBER1"], 
                    ["NAME2", "ADDRESS2", "PHONE NUMBER2"]]


#Sends error message to user and clears screen
def error_message():
    print("Invalid Input")
    time.sleep(2)
    os.system("cls")

#Checks if value is a 
def pos_int_input_validation(ques):
    while True:
        try:
            chosen_int = int(input(ques))
            if chosen_int < 1:
                error_message()
            else:
                return chosen_int
        except ValueError:
            error_message()

# For delivery 
def delivery():
    print("BLANK")
# For pickup
def pickup():
    print("BLANK")

# For menu 
def menu():
    while True:
        "Is the order delivery or pickup?"
        "Type 1 for Delivery "
        "Type 2 for Pickup"
        choice = pos_int_input_validation(":    ")
        if choice == 1:
            delivery()
            break
        elif choice == 2:
            pickup()
            break
        else:
            error_message()
        
menu()


