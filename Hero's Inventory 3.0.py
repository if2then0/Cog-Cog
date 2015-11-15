# Hero's Inventory 3.0
# Demonstrate Lists
# Seth Lombardy 

# Create a list with some items and display with a for loop

inventory = ["Sword","Armor","Shield","Healing Potion"]
print("Your items:")
for item in inventory:
    print(item)

input("\nPress the enter key to continue.")

# get length of a list

print("You have",len(inventory),"items in your possession.")
input("\nPress the enter key to continue.")

# test for membership with in

if "Healing Potion" in inventory:
    print("Your have a Healing Potion. You will live to fight another day.")

input("\nPress the enter key to continue.")

# display one item through an index

index=int(input("\nEnter the index number for an item in inventory: "))
print("At index",index,"is",inventory[index])
input("\nPress any key to continue.")

# display a slice

start=int(input("\nEnter the index number to begin a slice: "))
finish=int(input("Enter the index number to end the slice: "))
print("inventory[",start,":",finish,"]is",end="")
print(inventory[start:finish])
input("\nPress the enter key to continue.")

# concatentate two lists

chest=["Gold","Gems"]
print("You find a chest which contains: ")
print(chest)
print("You add the contents of the chest to your inventory.")
inventory+=chest
print("Your inventory is now: ")
print(inventory)
input("\nPress any key to continue.")

# assign by index

print("You trade your Sword for a Crossbow.")
inventory[0]="Crossbow"
print("Your inventory is now: ")
print(inventory)
input("\nPress any key to continue.")

# assign by slice

print("You use your Gold and Gems to buy an Orb of Future Telling.")
inventory[4:6]=["Orb of Future Telling"]
print("Your inventory is now: ")
print(inventory)
input("\nPress any key to continue.")

# delete an element

print("in a great battle, your shield is destroyed.")
del inventory[2]
print("Your inventory is now: ")
print(inventory)
input("\nPress the enter key to continue.")





