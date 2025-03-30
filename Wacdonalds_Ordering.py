"""A program that can be used by Wacdonalds Queenstown to get receipt."""

import os
import time


# 2D list of customer details ordered in name, adress, phone number
customer_details = [["NAME1", "ADDRESS1", "PHONE NUMBER1"], ["NAME2", "ADDRESS2", "PHONE NUMBER2"]]

order_details = ["ORDER1", "ORDER2"]


def error_message():
    """Send error message to user and clears screen."""
    print("Invalid Input")
    time.sleep(2)
    os.system("cls")


def pos_int_input_validation(ques):
    """Check if value is a postive interager and if not makes user input again."""
    while True:
        try:
            chosen_int = int(input(ques))
            if chosen_int < 1:
                error_message()
            else:
                return chosen_int
        except ValueError:
            error_message()


def non_zero_len_string(ques):
    """Check if string is a string with a length over 0 and if not makes the user input again."""
    while True:
        answer_string = input(ques).strip()
        if len(answer_string) <= 0:
            error_message()
        else:
            return answer_string


def order():
    """Ask the Wacdonald's employee what the customer has ordered."""
    print("")


def delivery():
    """Ask the Wacdonald's employee what their name, address, phone numer and prints their receipt."""
    os.system('cls')
    print("BLANK1")
    name = non_zero_len_string("Type in the customers name:  ")
    street_number = pos_int_input_validation("Type in the customer's street number: ")
    street_name = non_zero_len_string("Type in the customer's street name: ")
    suburb_or_locality = non_zero_len_string("Type in the customer's suburb or locality:   ")
    city_or_town = non_zero_len_string("Type in the customer's city or town:  ")
    while True:
        phone_number = pos_int_input_validation("Type in the customer's phone number (in format XXXXXXXX where the phone number can only have between 7 and 11 digits): ")
        if 7 <= len(str(phone_number)) <= 11:
            break
        else:
            error_message()
    customer_info = []
    customer_info.append(name)
    address_tuple = (str(street_number), street_name, suburb_or_locality, city_or_town)
    print(address_tuple)
    address = " ".join(address_tuple)
    customer_info.append(address)
    customer_info.append(phone_number)
    print(customer_info)
    customer_details.append(customer_info)
    print(customer_details)


def pickup():
    """For pickup."""
    print("BLANK2")


def order_history():
    """For order_history."""
    print("BLANK3")


def menu():
    """Menu system for program that runs at the start of the program."""
    while True:
        print("Is the order delivery or pickup?")
        print("Type 1 for Delivery ")
        print("Type 2 for Pickup")
        print("Type 3 for order history")
        choice = pos_int_input_validation(":    ")
        if choice == 1:
            delivery()
            break
        elif choice == 2:
            pickup()
            break
        elif choice == 3:
            order_history()
            break
        else:
            error_message()


menu()
