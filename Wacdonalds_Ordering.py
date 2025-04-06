"""A program that can be used by Wacdonalds Queenstown to get receipt."""

import os
import time


# 2D list of customer details ordered in name, adress, phone number
customer_details = [["NAME1", "ADDRESS1", "PHONE NUMBER1"], ["NAME2", "ADDRESS2", "PHONE NUMBER2"]]

# 2D list of customers order details
order_details = [["ORDER1", "TOTPRICE1"], ["ORDER2", "PRICE2"]]


menudict = {
  "Small Big Wac": 9.70,
  "Large Big Wac": 15.00,
  "Small Wac Quarter Pounder": 9.50,
  "Large Wac Quarter Pounder": 14.50,
  "Small Wac Chicken" : 9.50,
  "Large Wac Chicken" : 14.50,
  "Small Filet-Waco-Fish" : 8.80,
  "Large Filet-Waco-Fish" : 13.80,
  "Small Wac Cheeseburger": 6.40,
  "Large Wac Cheeseburger": 11.40,
  "Small Double Wac Cheeseburger": 8.10,
  "Large Double Wac Cheeseburger": 13.10,
  "6pc Chicken WacNuggets": 9.30,
  "10pc Chicken WacNuggets": 12.40,
  "Small Wac Fries": 5.70,
  "Large Wac Fries": 10.70,
  "Small Wac Soft Drink": 4.90,
  "Large Wac Soft Drink": 9.90,
  "Wac Cheese Burger Combo": 17.60,
  "Big Wac Combo": 18.90
}


def error_message():
    """Send error message to user and clears screen."""
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


def order():
    os.system("cls")
    """Ask the Wacdonald's employee what the customer has ordered."""
    print("What do the customer want to order?")
    i = 0
    for order, price in menudict.items():
        i += 1
        print(f"{i}, {order} ${price:.2f}")
    while True:
        menu_choice = pos_int_input_validation("Type number next to the item the customer wants:   ")
        if menu_choice > i:
            error_message()
        else:
            break
    i = 0
    total_price = 0
    full_order = ""
    for order, price in menudict.items():
        i += 1
        if i == menu_choice:
            amount_of_item = pos_int_input_validation(f"How many of {order} do you want?")
            total_price_one_type_item = amount_of_item * price
            total_price += total_price_one_type_item
            total_price = round(total_price, 2)
            individual_item_order = order
            full_order += individual_item_order + " "
            full_order_details =[]
            full_order_details.append(full_order)
            full_order_details.append(total_price)
            choice = pos_int_input_validation("Do you to add more items to your order\n Type 1 for yes or 2 for no\n")
            if choice == 1:
                continue
            else:
                order_details.append(full_order_details)
                break


def receipt():
    customer_number = len(customer_details)
    print(customer_details[customer_number-1])
    print(order_details[customer_number-1])


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
    order()
    receipt()


def pickup():
    """For pickup."""
    print("BLANK2")


def order_history():
    """For order_history."""
    print("BLANK3")
    i = 0
    for customer, order in zip(customer_details, order_details):
        i += 1
        print(f"Customer {i} details : {customer}, Customer {i} order {order}")


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
