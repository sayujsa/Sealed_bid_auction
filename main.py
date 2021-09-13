from replit import clear
from art import logo

print(logo)
print("Welcome to Blind Auction Program")

auction_list = []

def new_bid(given_name, given_amount):
    global auction_list
    auction_list += [{
   "name" : given_name,
    "amount" : given_amount,
  }]

again = "yes"

while again == "yes":
    name = input("Enter your name : ").capitalize()
    try:
      amount = int(input("Enter your bid : $"))
    except ValueError:
      print("Enter an amount please\n")
      continue
    new_bid(name,amount)
    again = input("Enter 'yes' to add another bid\nOr 'no' to show highest bid : ").lower()
    clear()

highest_bid = 0
for dicts in auction_list:
    if dicts["amount"] > highest_bid:
        highest_bid = dicts["amount"]
        winner = dicts["name"]

print(logo)
print(f"\nThe highest amount is ${highest_bid} by {winner}")
