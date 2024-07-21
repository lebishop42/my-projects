import requests
import json
import sys
from prettytable import PrettyTable


# RETRIEVING DATA FROM THE API FOR THE CUSTOMER
def show_api_catalogue():
    result = requests.get(
    'http://127.0.0.1:5001/catalogue',
    headers={'content-type': 'application/json'}
    )
    return result.json()


# POSTING RECORD OF SALES TO THE API
def api_add_purchase(input_name, input_horse_sold):

    purchase = {
        "buyer_name": input_name,
        "sold_horse_name": input_horse_sold
    }

    headers = {'content-type': 'application/json'}
    result_two = requests.post(
        'http://127.0.0.1:5001/bought_list',
        headers=headers, data=json.dumps(purchase))

    return result_two.json()


# UPDATING STATUS TO SOLD
def update_listing(input_horse_sold):

    update = {
        "horse_name": input_horse_sold,
        "status": "sold"
    }

    headers = {'content-type': 'application/json'}
    result_three = requests.put(
        'http://127.0.0.1:5001/catalogue',
        headers=headers, data=json.dumps(update))

    return result_three.json()


# ADDING A NEW LISTING TO THE API
def new_listing(sale_horse_name, sale_age, sale_colour, sale_price):

    listing = {
        "horse_name": sale_horse_name,
        "age": sale_age,
        "colour": sale_colour,
        "price": sale_price,
        "status": "for sale"
    }

    headers = {'content-type': 'application/json'}
    result_four = requests.post(
        'http://127.0.0.1:5001/catalogue',
        headers=headers, data=json.dumps(listing))

    return result_four.json()


# CONVERTS CATALOGUE TO TABLE FOR CLIENT
def make_table():
    my_table = PrettyTable(["Horse Name", "Age", "Colour", "Price"])
    for item in show_api_catalogue():
        my_table.add_row([item["Horse name"], item["Age"], item["Colour"], item["Price"]])
    return my_table


# TO CHECK IF A HORSE IS AVAILABLE
def check_listing(input_horse_sold):
    names_list = []
    for i in show_api_catalogue():
        names_list.append(i["Horse name"])
    if input_horse_sold not in names_list:
        sys.exit("Sorry, this horse is not available. Please try a different one.")
    else:
        pass


def validate_age(sale_age):
    if sale_age.isdigit():
        valid_sale_age = int(sale_age)
        if 0 > valid_sale_age > 25:
            sys.exit("That doesn't sound right, please check your details.")
        else:
            pass
    else:
        sys.exit("Please give a valid age in digits.")


def validate_price(sale_price):
    if sale_price.isdigit():
        valid_sale_price = int(sale_price)
        if valid_sale_price < 0:
            sys.exit("Sorry, please give a value of 0 or more.")
        else:
            pass
    else:
        sys.exit("Please give a valid number (greater than 0) in digits.")


# *** MAIN FUNCTION FOR CLIENT INTERACTION ***
def run():

    try:
        print("-------------------------------------")
        print("Howdy! Welcome to the Horse Exchange.")
        print("-------------------------------------")
        buy_or_sell = input("Would you like to buy or sell a horse today? Type 'b' to buy or 's' to sell: ")

        if buy_or_sell == "b":
            print("Horses for sale:")
            print(make_table())
            input_horse_sold = input("Which horse would you like to buy?: ")
            check_listing(input_horse_sold)
            input_name = input("Please provide your name: ")
            api_add_purchase(input_name, input_horse_sold)
            print(f"Thank you for buying {input_horse_sold}.\nOur Catalogue has now been updated.")
            update_listing(input_horse_sold)
            print(make_table())
        elif buy_or_sell == 's':
            sale_horse_name = input("Please enter your horse's name: ")
            sale_age = input("Please enter your horse's age: ")
            validate_age(sale_age)
            sale_colour = input("Please enter the colour of your horse: ")
            sale_price = input("Please enter the price: ")
            validate_price(sale_price)
            new_listing(sale_horse_name, sale_age, sale_colour, sale_price)
            print("Thank you, our catalogue has now been updated:")
            print(make_table())
        else:
            print("Not a valid option, please try again.")

    except ValueError as e:
        print("Value exception: ", e)
    except ConnectionError as c:
        print("Connection Error (check API connection): ", c)
    except ConnectionRefusedError as r:
        print("Connection Refused: ", r)

if __name__ == '__main__':
    run()