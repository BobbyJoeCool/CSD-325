# Breutzmann, Robert
# Assignment 1.3
# 99 Bottles of Beer on the Wall

# Ask user for the amount of beer they have, and verify input is valid.
while True:
    try:
        beer = int(input("How Many Bottles of Beer do you have? "))
        if beer < 0:
            print("Error! You cannot have negative beer.\n")
            continue
        break
    except:
        print("Error! Please enter a valid integer.\n")
        continue

print() # Print a blank line to help with spacing

# While loop to print one verse of the song 
while beer >0:
    if beer >1:
        print(f"{beer} bottles of beer on the wall, {beer} bottles of beer!")
    else:
        print(f"1 bottle of beer on the wall, 1 bottle of beer!")
    
    beer -= 1

    if beer >1:
        print(f"Take one down, pass it around, {beer} bottles of beer on the wall!\n")
    elif beer ==1:
        print(f"Take one down, pass it around, 1 bottle of beer on the wall!\n")
    elif beer ==0:
        print(f"Take one down, pass it around, no more bottles of beer on the wall!\n")

print("Time to buy more beer!\n")