"""A program that can be used by Wacdonalds Queenstown to get receipt."""

import os
import time


# 2D list of customer details ordered in name, adress, phone number
customer_details = []

# 2D list of customers order details
order_details = []


# Dictonary of the items on the menu
menudict = {
  "Small Big Wac": 10.00,
  "Large Big Wac": 15.00,
  "Small Wac Quarter Pounder": 9.49,
  "Large Wac Quarter Pounder": 14.49,
  "Small Wac Chicken": 9.49,
  "Large Wac Chicken": 14.49,
  "Small Filet-Waco-Fish": 8.79,
  "Large Filet-Waco-Fish": 13.79,
  "Small Wac Cheeseburger": 6.39,
  "Large Wac Cheeseburger": 11.39,
  "Small Double Wac Cheeseburger": 8.99,
  "Large Double Wac Cheeseburger": 13.99,
  "6pc Chicken WacNuggets": 9.39,
  "10pc Chicken WacNuggets": 12.39,
  "Small Wac Fries": 5.70,
  "Large Wac Fries": 10.70,
  "Small Wac Soft Drink": 4.89,
  "Large Wac Soft Drink": 9.89,
  "Wac Cheese Burger Combo": 17.69,
  "Big Wac Combo": 18.89
}


def error_message():
    """Send error message to user and wait 2 seconds."""
    print("Invalid Input\n")
    time.sleep(2)


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


def back_to_menu():
    """Ask the Wacdonald's employee if they want to go back to the menu or if they want to stop the program."""
    while True:
        choice = pos_int_input_validation("Do you want to go back to the menu?\n Type 1 for yes or 2 for no\n")
        if choice == 1:
            menu()
            break
        elif choice == 2:
            print("Program has ended")
            break
        else:
            error_message()


def order():
    """Ask the Wacdonald's employee what the customer has ordered."""
    os.system("cls")
    print("What does the customer want to order?")
    # Create local varable that will be used in this function
    total_price = 0
    full_order = ""
    menu_item_number = 0
    # Prints out the menu in a formated way
    for order, price in menudict.items():
        menu_item_number += 1
        print(f"{menu_item_number}: {order} ${price:.2f}")
    # While loop that asks the Wacdonald's employee what the customer has ordered.
    while True:
        menu_choice = pos_int_input_validation("Type number next to the item the customer wants:   ")
        # Checks to see if chosen number by the employee is a above  the max number of the menu
        # If true then makes user type number in again
        if menu_choice > menu_item_number:
            error_message()
            continue
        menu_number = 0
        # Asks how many of the menu item the customer wants, calculates how much the price is
        # And adds both of them to the customers full_order_details
        for order, price in menudict.items():
            menu_number += 1
            if menu_number == menu_choice:
                amount_of_item = pos_int_input_validation(f"How many of {order} does the customer want? ")
                total_item_amount_price = amount_of_item * price
                total_price += total_item_amount_price
                total_price = round(total_price, 2)
                individual_item_order = f"{amount_of_item} x {order}"
                full_order += individual_item_order + ", "
                full_order_details = [full_order.strip(", "), total_price]
        # Asks if the employee wants to keep ordering for the customer
        # If yes then goes back to the start of the outer loop
        # If no then finishes the ordering function
        while True:
            ordering = True
            choice = pos_int_input_validation("Continue ordering?\n Type 1 for yes or 2 for no\n")
            if choice == 1:
                break
            elif choice == 2:
                order_details.append(full_order_details)
                ordering = False
                break
            else:
                error_message()
                continue
        if not ordering:
            break


def receipt():
    """Print out the receipt of the customer."""
    # Gets the index of the most recent customer to print out the receit of the customer
    customer_number = len(customer_details)
    index = customer_number-1
    print(f"Name: {customer_details[index][0]}")
    # Checks if order is delivery or pickup and print the corresponding statements
    if len(customer_details[index]) != 1:
        print(f"Address: {customer_details[index][1]}")
        print(f"Phone Number: {customer_details[index][2]}")
        print(f"Delivery Order of {order_details[index][0]}")
    else:
        print(f"Pickup Order of {order_details[index][0]}")
    print(f"Price of ${order_details[index][1]:.2f}")


def delivery():
    """Ask the Wacdonald's employee what their name, address, phone numer and print their receipt."""
    os.system('cls')
    # Asks employee for all the customers infomation
    name = non_zero_len_string("Type in the customers name:  ")
    street_number = pos_int_input_validation("Type in the customer's street number: ")
    street_name = non_zero_len_string("Type in the customer's street name: ")
    suburb_or_locality = non_zero_len_string("Type in the customer's suburb or locality:   ")
    city_or_town = non_zero_len_string("Type in the customer's city or town:  ")
    # Checks if the customer has inputed a number that has between 7-11 digits
    while True:
        phone_number = pos_int_input_validation("Type in the customer's phone number (in format XXXXXXXX where the phone number can only have between 7 and 11 digits, including both 7 and 11  (this limit does not include leading 0's): ")
        if 7 <= len(str(phone_number)) <= 11:
            break
        else:
            error_message()
    # Adds infomation into customer details
    address_tuple = (str(street_number), street_name, suburb_or_locality, city_or_town)
    address = " ".join(address_tuple)
    customer_info = [name, address, phone_number]
    customer_details.append(customer_info)
    # Asks for the order, prints receipt and goes asks if they want to go back to the menu
    order()
    receipt()
    back_to_menu()


def pickup():
    """Ask the Wacdonald's employee what their name is and prinits their receipt."""
    os.system('cls')
    # Asks employee for the customers name only and adds it to customer details
    name = non_zero_len_string("Type in the customers name:  ")
    customer_info = [name]
    customer_details.append(customer_info)
    print(customer_details)
    # Asks for the order, prints receipt and goes asks if they want to go back to the menu
    order()
    receipt()
    back_to_menu()


def order_history():
    """Print out the order history."""
    os.system('cls')
    # Checks if there has not been and order
    # If not that prints statment and does back_to_menu()
    # If ther has been at least 1 order prints out all orders
    if len(customer_details) != 0:
        i = 0
        for customer, order in zip(customer_details, order_details):
            i += 1
            # Checks if order is delivery or pickup and print the corresponding statements
            if len(customer) == 1:
                print(f"Customer {i}| Name : {customer[0]}, Customer {i} ordered {order[0]} with total price of ${order[1]:.2f}")
            else:
                print(f"Customer {i}| Name : {customer[0]}, Address : {customer[1]},  Phone Number : {customer[2]},  Customer {i} ordered {order[0]} with total price of ${order[1]:.2f}")
    else:
        print("\nEnter at least 1 order to see order history")
    back_to_menu()


def menu():
    """Menu system for program that runs at the start of the program."""
    while True:
        print("\nIs the order delivery or pickup?")
        print("Type 1 for Delivery ")
        print("Type 2 for Pickup")
        print("Type 3 for order history")
        print("Type 4 to end program")
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
        elif choice == 4:
            break
        else:
            error_message()


menu()
