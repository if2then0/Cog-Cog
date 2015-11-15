# Personal Greeter
# Demonstrates getting user input

name = input("Hi, what's your name? ")

print(name)

print("Hi,",name)

input("\n\nPress the enter key to exit.")

# Quotation Manipulation
# Demonstrates string methods

# quote from IBM Chairman, Thomas Watson, in 1943

quote = "I think there is a world market for maybe five computers."

print("Original quote:")
print(quote)

print("\nIn uppercase:")
print(quote.upper())

print("\nIn lowercase:")
print(quote.lower())

print("\nAs a title:")
print(quote.title())

print("\nWith a minor replacement:")
print(quote.replace("five","millions of"))

print("\nOriginal quote is still:")
print(quote)

input("\n\nPress the enter key to exit.")

# Trust Fund Buddy - (Bad Corrected)
# Demonstrates a logical error - (Concoctenation: String Values to Numbers)

print(
    """
    Trust Fund Buddy

Totals your monthly spending so that your fund doesn't run out
(And you're forced to get a real job)

Please enter the requested, monthly costs. Since you're rich, ignore pennies and use only dollar amounts

"""
    )

car = int(input("Lamborghini Tune-Ups: "))
rent = int(input("Manhattan Apartment: "))
jet = int(input("Private Jet Rental: "))

gifts = int(input("Gifts: "))
food = int(input("Dining Out: "))
staff = int(input("Staff (butlers, chef, driver, assistant): "))

guru = int(input("Personal Guru and Coach: "))
games = int(input("Computer Games: "))

total = car+rent+jet+gifts+food+staff+guru+games

print("\nGrand Total: ",total)

input("\n\nPress the Enter Key to exit.")

# More input and styling

name = input("Hi. What's your name? ")
age = input("How old are you? ")
age = int(age)
weight = int(input("Okay, last question. How many pounds do you weigh? "))

print("\nIf poet ee cummings were to email you, he'd address you as ",name.lower())
print("But if ee were mad, he'd call you ",name.upper())

called = name*5
print("\nIf a small child were trying to get your attention,")
print("your name would become: ")
print(called)

seconds = age*365*24*60*60
print("\nYou're over", seconds, "seconds old.")

moon_weight = weight/6
print("\nDid you know that on the Moon you would weigh only",
      moon_weight, "pounds?")

sun_weight = weight*27.1
print("On the Sun, you'd weigh", sun_weight, "(but, ah...not for long).")

input("\n\nPress the enter key to exit.")

# Craps Roller
# Demonstrates random number generation

import random

# generate random numbers 1-6

die1 = random.randint(1,6)
die2 = random.randrange(6)+1

total = die1 + die2

print("You rolled a",die1,"and a",die2,"for a total of", total)

input("\n\nPress the Enter Key to exit.")

      
# Password
# Demonstrates the if statement

print("Welcome to Security System Inc.")
print("--where security is our middle name.\n")

password = input("Enter your password")

if password == "secret":
    print("Access Granted")

input("\n\nPress the enter key to exit.")

# Granted or Denied
# Demonstrates an else clause

print("Welcome to System Security Inc.")
print("--where security is our middle name\n")

password = input("Enter your password:")

if password == "secret":
    print("Access Granted")

else:
    print("Acces Denied")

input("\n\nPress the enter key to exit.")

# Mood Computer
# Demonstrates the elif clause

import random

print("I sense your energy. Your true emotions are coming across my screen.")
print("You are...")

mood = random.randint(1,3)

if mood == 1:
    #happy
    print(\
        """
:)

""")

elif mood == 2:
    #neutral
    print(\
        """

:|

""")

elif mood == 3:
    #sad
    print(\
        """

:(

""")

else:
    print("illegal mood value! (You must be in a really strange mood).")

print("...today.")

input("\n\nPress the enter key to exit.")

# Three Year-Old Simulator
# Demonstrates the while loop

print("\tWelcome to the 'Three-Year-Old Simulator'\n")
print("This program simulates a conversation with a three-year-old child.")
print("Try to stop the madness.\n")

response = ""
while response != "Because.":
    response = input("Why?\n")

print("Oh. Okay.")

input("\n\nPress the Enter Key to Exit.")

# Losing Battle
# Demonstrates the dreaded infinite loop

print("Your lone hero is surrounded by a massive army of trolls.")
print("Their decaying green bodies stretch out, melting into the horizon.")
print("Your hero unsheathes his sword for the last fight of his life.\n")

health = 10
trolls = 0
damage = 3

while health > 0:
    trolls +=1
    health -= damage

    print("Your hero swings and defeats an evil troll,"\
          "but takes",damage,"damage points.\n")

print("Your hero fought valiantly and defeated",trolls,"trolls.")
print("But alas, your hero is no more.")

input("\n\nPress the enter key to exit.")

# Maitre D'
# Demonstrates treating a value as a condition

print("Welcome to the Chateau D'Food")
print("It seems we are quite full this evening.\n")

money = int(input("How many dollars do you slip the Maitre D'?"))

if money:
    print("Ah, I am reminded of a table. Right this way.")

else:
    print("please, sit. It may be a while.")

input("\n\nPress the enter key to exit.")

# Guess my number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the number lets
# the player know if the guess is too high, too low,
# or right on the money.

import random

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# Set the initial values

the_number = random.randint(1,100)
guess = int(input("Take a guess:"))
tries = 1

# Guessing loop

while guess != the_number:
    if guess > the_number:
        print("Lower...")
    else:
        print("Higher...")
    guess = int(input("Take a guess:"))
    tries += 1

print("You guessed it! The number was",the_number)
print("And it only took you",tries,"tries!")

input("\n\nPress the enter key to exit.")

# Loopy String
# Demonstrates the for loop with a string

word = input("Enter a word:")

print("\nHere's each letter in your word:")
for letter in word:
    print(letter)
input("\n\nPress the enter key to exit.")

# Counts
# Demonstrates the range() function

print("Counting:")
for i in range(10):
    print(i, end = "")
print("\n\nCounting by fives:")
for i in range(0,50,5):
    print(i, end = "")
print("\n\nCounting backwards:")
for i in range(10,0,-1):
    print(i, end = "")

input("\n\nPress the enter key to exit.\n")


# Message Analyzer
# Demonstrates the len() function and the in operator

message = input("Enter a message: ")

print("\nThe length of your message is:",len(message))
print("\nThe most common letter in the English language, 'e',")

if "e" in message:
    print("is in your message.")
else:
    print("is not in your message.")

input("\n\nPress the Enter Key to exit.")

# Random Access
# Demonstrates string indexing

import random

word = "index"
print("The word is: ",word,"\n")

high = len(word)
low = -len(word)

for i in range(10):
    position = random.randrange(low,high)
    print("word[",position,"]\t",word[position])

input("\n\nPress the Enter Key to exit.")

# No Vowels
# Demonstrates creating new strings with a for loop

message = input("Enter a message: ")
new_message = ""
VOWELS = "aeiou"

print()
for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        print("A new string has been created: ",new_message)

print("\nYour message without vowels is: ",new_message)

input("\n\nPress the enter key to exit.")

# Pizza Slicer
# Demonstrates string slicing

word = "pizza"

print(
"""
 Slicing 'Cheat Sheet'

 0   1   2   3   4   5
 +---+---+---+---+---+
 | p | i | z | z | a |
 +---+---+---+---+---+
-5  -4  -3  -2  -1

"""
)

print("Enter the beginning and ending index for your slice of 'pizza'.")
print("Press the enter key at 'Start' to exit.")

start = None

while start != "":
    start = (input("\nStart: "))

    if start:
        start = int(start)

        finish = int(input("Finish: "))

        print("word[",start,":",finish,"] is ",end = "")
        print(word[start:finish])

input("\n\nPress the enter key to exit.")

# Hero's Inventory
# Demonstrates tuple creation
# Create an empty tuple

inventory = ()

# Treat the tuple as a condition

if not inventory:
    print("You are empty-handed.")

input("\nPress the enter key to continue.")

# Create a tuple with some items

inventory = ("sword",
             "armor",
             "shield",
             "healing potion")

# Print the tuple

print("\nThe tuple inventory is: ")
print(inventory)

# Print each element in the tuple

print("\nYour items:")
for item in inventory:
    print(item)

input("\n\nPress the enter key to exit.")

# Hero's Inventory 2.0
# Demonstrates tuples
# Create a tuple with some items and display with a for loop

inventory = ("sword",
             "armor",
             "shield",
             "healing potion")

print("Your items: ")

for item in inventory:
    print(item)

# test for membership with in

if "healing potion" in inventory:
    print("You will live to fight another day.")

# display one item through an index

index = int(input("\nEnter the index number for an item in inventory:"))
print("At index", index,"is",inventory[index])

input("\nPress the enter key to continue.")

# display a slice

start = int(input("\nEnter the index number to begin a slice: "))
finish = int(input("Enter the index number to end the slice: "))

print("Inventory[",start,":",finish,"]is",end="")
print(inventory[start:finish])


input("\nPress the enter key to continue.")

# concatenate two tuples

chest = ("gold","gems")
print("You find a chest. It contains: ")
print(chest)

print("You add the contents of the chest to your inventory.")

inventory += chest

print("Your inventory is now: ")
print(inventory)

input("\n\nPress the enter key to continue.")




             
      


