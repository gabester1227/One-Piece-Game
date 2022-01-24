# Author: Gabriel Schonacher

import time
import sys
import os
from termcolor import cprint

# Clears Console
def clear():
    os.system("clr" if os.name == "nt" else "clear")

# Welcome Room
def welcome(inventory):
    user_choice = None

    # Welcome Screen
    cprint("Welcome to One Piece Adventures!\n")

    while user_choice != "9":
        # Delay Time
        time.sleep(1)

        # Introduction - Welcome Screen
        print("\nYou are in the Grand Line! The Grand Line is a whole new part of   the world where weird islands, kings, and enemies reside! It is    your job to visit each island and defend these islands for the     people on them. First you need to find the special fruit on each island! There is one on each of these islands, so its your job to find them! GO GET EM' PIRATE!\n")

        cprint("Inventory: " + str(inventory), "cyan")

        cprint("\nWhere would you like to go?\n1. Sail North to Cap Des Jumeaux\n2. Sail North-East to Whiskey Peak\n3. Sail East to Little Garden\n4. Sail South-East to Drum Island\n5. Sail South to Alabasta\n6. Sail South-West to Mock Town\n7. Sail West to Sky Piea\n8. Sail North-West to Longring-Longland\n9. Quit\n", "red")

        # Enables user to make a choice
        user_choice = input("Enter your choice: ")
        clear()

        # This is where the code runs to for when the user decieds they want to go somewhere
        if user_choice == "1":
        # Sail North - Cap Des Jumeaux
            island1(inventory)
        elif user_choice == "2":
        # Sail North-East - Whiskey Peak
            island2(inventory)
        elif user_choice == "3":
        # Sail East - Little Garden
            island3(inventory)
        elif user_choice == "4":
        # Sail South-East - Drum Island
            island4(inventory)
        elif user_choice == "5":
        # Sail South - Alabasta
            island5(inventory)
        elif user_choice == "6":
        # Sail South-West - Mock Town
            island6(inventory)
        elif user_choice == "7":
        # Sail West - Sky Piea
            island7(inventory)
        elif user_choice == "8":
        # Sail North-West - Longring Longland
            island8(inventory)
        elif user_choice == "9":
        # QUIT
            sys.exit()
            print("Goodbye! Thanks for playing!")
        else:
            cprint("\nOpps! Looks like your ship hit a bump! Try Again", "blue")

# Island 1 - Cap Des Jumeaux - NORTH
def island1(inventory):
    user_choice = None

    cprint("\nWelcome to Cap Des Jumeaux!\n", "blue")

    # User Choice 
    while user_choice != "7":
        # wait for 2 seconds
        time.sleep(1)

        # Island 1 Description 
        cprint("\nYou sailed to Cap Des Jumeaux! Here on Warship Island lives majestic dragons who are endangered by the Marines who are trying to kill  the dragons for an imortal elixer. Your job is to protect the      dragons from being slain and to protect their rarity! First you    need to find the gum gum fruit to give you the abilites to stretch yourself to defeat these guys with powerful hits!", "yellow")

        cprint("\nInventory: " +str(inventory), "cyan")

        cprint("\nWhat would you like to do?\n1. Battle\n2. Look Around\n3. Sail North-East to Whiskey Peak\n4. Sail North-West to Longring Longland\n5. Sail South to Alabasta\n6. Sail South-West to Mock Town\n7. Quit", "green")

        user_choice = input("Enter your choice: ")
        clear()

        if user_choice == "1" and "Gum Gum Fruit" not in inventory:
            cprint("\nYou lost because you werent strong enough without the gum gum      fruit!", "white")
        elif user_choice == "1" and "Gum Gum Fruit" in inventory:
            print("\nGood job! You beat the Marins from hurting the Dragons!")
        elif user_choice == "2":
            cprint("Good Job! You found and ate the gum gum fruit! The Gum Gum fruit that makes your body elastic! You can stretch things like your arms, super far to get powerful hits!", "yellow")
            inventory.append("Gum Gum Fruit ")
            # NORTH-EAST - Whiskey Peak
        elif user_choice == "3":
            island2(inventory)
            # NORTH-WEST - Longring Longland
        elif user_choice == "4":
            island8(inventory)
            # SOUTH - Alabasta 
        elif user_choice == "5":
            island5(inventory)
            # SOUTH-WEST - Mock Town
        elif user_choice == "6":
            island6(inventory)
            # QUIT
        elif user_choice == "7":
            sys.exit()
            print("Goodbye! Thanks for playing!")
        else:
            cprint("\nOpps! Looks like your ship hit a bump! Try Again", "blue")

# Island 2 - Whiskey Peak - NORTH-EAST
def island2(inventory):
    user_choice = None

    cprint("\nWelcome to Whiskey Peak!\n", "blue")

    # User Choice 
    while user_choice != "7":
        # wait for 2 seconds
        time.sleep(1)

        # Island 2 Description 
        cprint("\nYou sailed to Whiskey Peak! Here on Whiskey Peak is full of bounty hunters! Considering you are a pirate, you have a massive bounty on your head. Your goal is to defend yourself and your crew!", "yellow")

        cprint("\nInventory: " +str(inventory), "cyan")

        cprint("\nWhat would you like to do?\n1. Battle\n2. Look Around\n3. Sail East to Little Garden\n4. Sail North back to Cap Des Jumeaux\n5. Sail West to Sky Piea\n6. Sail South-West to Mock Town\n7. Quit", "green")

        user_choice = input("Enter your choice: ")
        clear()

        if user_choice == "1" and "Bomb Bomb Fruit" not in inventory:
            cprint("\nYou lost because you werent strong enough without the Bomb Bomb      fruit!", "white")
        elif user_choice == "1" and "Bomb Bomb Fruit" in inventory:
            print("\nGood job! You beat all of the bounty hunters who were trying to take your head!")
        elif user_choice == "2":
            inventory.append("Bomb Bomb Fruit")
            cprint("Good Job! You found and ate the Bomb Bomb fruit, which enables you to spit and create exposilions like bullets!", "yellow")
            # EAST - Little Garden
        elif user_choice == "3":
            island3(inventory)
            # NORTH - Cap Des Jumeaux
        elif user_choice == "4":
            island1(inventory)
            # WEST - Sky Piea
        elif user_choice == "5":
            island4(inventory)
            # SOTH-WEST - Mock Town
        elif user_choice == "6":
            island5(inventory)
            # QUIT
        elif user_choice == "7":
            sys.exit()
            print("Goodbye! Thanks for playing!")
        else:
            cprint("\nOpps! Looks like your ship hit a bump! Try Again", "blue")


# Island 3 - Little Garden - EAST
def island3(inventory):
    user_choice = None

    cprint("\nWelcome to Little Garden!\n", "blue")

    # User Choice 
    while user_choice != "7":
        # wait for 2 seconds
        time.sleep(1)

        # Island 3 Description 
        cprint("\nYou sailed to Little Garden! Here on Little Garden lives 2 giants who have 100 million berry bounty on their head! They are dangerous but also extremely strong, they are both 100 years old, so be careful fighting them! ", "yellow")

        cprint("\nInventory: " +str(inventory), "cyan")

        cprint("\nWhat would you like to do?\n1. Battle\n2. Look Around\n3. Sail North back to Whiskey Peak\n4. Sail South-East to Drum Island\n5. Sail West to Sky Piea\n6. Sail North-West to Longring Longland\n7. Quit\n", "green")

        user_choice = input("Enter your choice: ")
        clear()

        if user_choice == "1" and "Bomb Bomb Fruit" not in inventory:
            cprint("\nYou lost because you werent strong enough without the Kilo Kilo     fruit!", "white")
        elif user_choice == "1" and "Kilo Kilo Fruit" in inventory:
            print("\nGood job! You beat both of those AGRESSIVE giants!")
        elif user_choice == "2":
            inventory.append("Kilo Kilo Fruit")
            cprint("Good Job! You found and ate the Kilo Kilo fruit! The Kilo Kilo fruit makes your body as light as a feather where you can defy gravity and float, and then make youself as heavy as 10,000 kilos! You can float in the air and then come down super fast as you increase your weight in your body!", "yellow")
            # NORTH-EAST - Whiskey Peak
        elif user_choice == "3":
            island2(inventory)
            # SOUTH-EAST - Drum Island
        elif user_choice == "4":
            island4(inventory)
            # WEST - Sky Piea
        elif user_choice == "5":
            island7(inventory)
            # NORTH-WEST - Longring Longland
        elif user_choice == "6":
            island8(inventory)
            # QUIT
        elif user_choice == "7":
            sys.exit()
            print("Goodbye! Thanks for playing!")
        else:
            cprint("\nOpps! Looks like your ship hit a bump! Try Again", "blue")

# Island 4 - Drum Island - SOUTH-EAST
def island4(inventory):
    user_choice = None

    cprint("\nWelcome to Drum Island!\n", "blue")

    # User Choice 
    while user_choice != "7":
        # wait for 2 seconds
        time.sleep(1)

        # Island 4 Description 
        cprint("\nYou sailed to Drum Island! Here on Drum Island, it is a winter storm all year round! Your goal is to protect drum island from knights! They have invaded the island in hopes to take it back under an evil kings rule! Do not let this happen!", "yellow")

        cprint("\nInventory: " +str(inventory), "cyan")

        cprint("\nWhat would you like to do?\n1. Battle\n2. Look Around\n3. Sail East back to Little Garden\n4. Sail South to Alabasta\n5. Sail North-East to Longring Longland\n6. Sail North to Cap Des Jumeaux\n7. Quit", "green")

        user_choice = input("Enter your choice: ")

        if user_choice == "1" and "Ice Ice Fruit" not in inventory:
            cprint("\nYou lost because you werent strong enough without the Ice Ice      fruit!", "white")
        elif user_choice == "1" and "Ice Ice Fruit" in inventory:
            print('Good Job! You forze all of those knights who were trying to take over the island!')
        elif user_choice == "2":
            inventory.append("Ice Ice Fruit")
            cprint("Good Job! You found and ate the Ice Ice fruit! This fruit will help you battle off the knights with ice, and freeze them to throw them back on their ship and turn their sails away from the island so that they never come back again!", "yellow")
            # EAST - Little Garden
        elif user_choice == "3":
            island3(inventory)
            # SOUTH - Alabasta
        elif user_choice == "4":
            island5(inventory)
            # NORTH-WEST - Longring Longland
        elif user_choice == "5":
            island8(inventory)
            # NORTH - Cap Des Jumeaux
        elif user_choice == "6":
            island1(inventory)
            # QUIT
        elif user_choice == "7":
            sys.exit()
            print("Goodbye! Thanks for playing!")
        else:
            cprint("\nOpps! Looks like your ship hit a bump! Try Again", "blue")

# Island 5 - Alabsta - SOUTH 
def island5(inventory):
    user_choice = None

    cprint("\nWelcome to Alabasta!\n", "blue")

    # User Choice 
    while user_choice != "7":
        # wait for 2 seconds
        time.sleep(1)

        # Island 5 Description 
        cprint("\nYou sailed to Alabsta! Here on Alabsta reigns king Nefertari Cobra! Your job is to protect the island from being destroyed by a man named Croc! He is trying to destroy Alabasta and make the island his own. Defend the island for Nefertari Cobra", "yellow")

        cprint("\nInventory: " +str(inventory), "cyan")

        cprint("\nWhat would you like to do?\n1. Battle\n2. Look Around\n3. Sail South-East back to Drum Island\n4. Sail South-West to Mock Town\n5. Sail North-East to Whiskey Peak\n6. Sail North to Cap Des Jumeaux\n7. Quit", "green")

        user_choice = input("Enter your choice: ")

        if user_choice == "1" and "Sand Sand Fruit" not in inventory:
            cprint("\nYou lost because you werent strong enough without the Sand Sand      fruit!", "white")
        elif user_choice == "1" and "Ice Ice Fruit" in inventory:
            print("\nGood job! ")
        elif user_choice == "2":
            inventory.append("Sand Sand Fruit")
            cprint("Good Job! You found and ate the Sand Sand fruit! The Sand Sand fruit gievs you the ability to transform your body as sand, and dodge attacks by shifting certain body parts into sand!", "yellow")
            # SOUTH-EAST - Drum Island
        elif user_choice == "3":
            island4(inventory)
            # SOUTH-WEST - Mock Town
        elif user_choice == "4":
            island6(inventory)
            # NORTH-EAST - Whiskey Peak
        elif user_choice == "5":
            island2(inventory)
            # NORTH - Cap Des Jumeaux
        elif user_choice == "6":
            island1(inventory)
            # QUIT
        elif user_choice == "7":
            sys.exit()
            print("Goodbye! Thanks for playing!")
        else:
            cprint("\nOpps! Looks like your ship hit a bump! Try Again", "blue")

# Island 6 - Mock Town - South-East
def island6(inventory):
    user_choice = None

    cprint("\nWelcome to Mock Town!\n", "blue")

    # User Choice 
    while user_choice != "7":
        # wait for 2 seconds
        time.sleep(1)

        # Island 6 Description 
        cprint("\nYou sailed to Mock Town! Here in Mock Town there is a springy man called Belaumy. His legs turn into springs and he can bounce every where really fast. Its your turn to give this guy a smack down, as he is destorying the whole town!", "yellow")

        cprint("\nInventory: " +str(inventory), "cyan")

        cprint("\nWhat would you like to do?\n1. Battle\n2. Look Around\n3. Sail back to the South of Alabasta\n4. Sail West to Sky Piea\n5. Sail North-East to Whiskey Peak\n6. East to Little Garden\n7. Quit", "green")

        user_choice = input("Enter your choice: ")

        if user_choice == "1" and "Smoke Smoke Fruit" not in inventory:
            cprint("\nYou lost because you werent strong enough without the smoke smoke      fruit!", "white")
        if user_choice == "1" and "Smoke Smoke Fruit" in inventory:
            print("\nGood job! You beat Belaumy! You choked him out with you smoke!")
        elif user_choice == "2":
            inventory.append("Smoke Smoke Fruit ")
            cprint("Good Job! You found and ate the Smoke Smoke fruit! The Smoke Smoke fruit enables you to turn into smoke! This gives you the ability to turn your body into smoke whenever you want", "yellow")
            # NORTH-EAST - Whiskey Peak
        elif user_choice == "3":
            island5(inventory)
            # SOUTH - Alabasta
        elif user_choice == "4":
            island7(inventory)
            # SOUTH-EAST - Drum Island
        elif user_choice == "5":
            island2(inventory)
            # EAST - Little Garden
        elif user_choice == "6":
            island3(inventory)
            # QUIT
        elif user_choice == "7":
            sys.exit()
            print("Goodbye! Thanks for playing!")
        else:
            cprint("\nOpps! Looks like your ship hit a bump! Try Again", "blue")

# Island 7 - Sky Piea - WEST
def island7(inventory):
    user_choice = None

    cprint("\nWelcome to Sky Piea!\n", "blue")

    # User Choice 
    while user_choice != "7":
        # wait for 2 seconds
        time.sleep(1)

        # Island 7 Description  
        cprint("\nYou sailed to Sky Piea! Sky Piea is an island in the sky! It has a city of gold, that has man who is trying to steal all the gold! This man goes by the name of Long Lobes. Defend the gold and defeat Long Lobes.\n", "yellow")

        cprint("\nInventory: " +str(inventory), "cyan")

        cprint("\nWhat would you like to do?\n1. Battle\n2. Look Around\n3. Sail back to the South-West of Mock Town\n4. Sail West to Sky Piea\n5. Sail North-East to Whiskey Peak\n6. East to Little Garden\n7. Quit", "green")

        user_choice = input("Enter your choice: ")

        if user_choice == "1" and "Tangle Tangle Fruit" not in inventory:
            cprint("\nYou lost because you werent strong enough without the Tangle Tangle     fruit!", "white")
        elif user_choice == "1" and "Tangle Tangle Fruit" in inventory:
            print("\nGood job! You beat Long Lobes!")
        elif user_choice == "2":
            inventory.append("Tangle Tangle Fruit")
            cprint("Good Job! You found and ate the Tangle Tangle fruit. Use the Tangle Tangle to tie up his long ear lobes, and render him useless for the fight!", "yellow")
            # SOUTH-WEST - Mock Town
        elif user_choice == "3":
            island6(inventory)
            # NORTH-WEST - Longring Longland
        elif user_choice == "4":
            island8(inventory)
            # EAST - Little Garden
        elif user_choice == "5":
            island3(inventory)
            # SOUTH-EAST - Drum Island
        elif user_choice == "6":
            island4(inventory)
            # QUIT
        elif user_choice == "7":
            sys.exit()
            print("Goodbye! Thanks for playing!")
        else:
            cprint("\nOpps! Looks like your ship hit a bump! Try Again", "blue")

# Island 8 - Longring Longland - NORTH-WEST
def island8(inventory):
    user_choice = None

    cprint("\nWelcome to Longring Longland!\n", "blue")

    # User Choice 
    while user_choice != "7":
        # wait for 2 seconds
        time.sleep(1)

        # Island 8 Description 
        cprint("\nYou sailed to Longring Longland, where Davey Back reisdes, where he is trying to take your flag and your crew. Defend the groud from Davey Back.\n", "yellow")

        cprint("\nInventory: " +str(inventory), "cyan")

        cprint("\nWhat would you like to do?\n1. Battle\n2. Look Around\n3. Sail back to the South-West of Sky Piea\n4. Sail West to Cap Des Jumeaux\n5. Sail North-East to Whiskey Peak\n6. East to Little Garden\n7. Quit", "green")

        user_choice = input("Enter your choice: ")

        if user_choice == "1" and "Slow Slow Fruit" in inventory:
            cprint("\nYou lost because you werent strong enough without the Slow Slow      fruit!", "white")
        elif user_choice == "1" and "Slow Slow Fruit" not in inventory:
            print("\nGood job! You beat !")
        elif user_choice == "2":
            inventory.append("Slow Slow Fruit ")
            cprint("Good Job! You found and ate the Slow Slow fruit! Slow down your enemies with the Slow Slow fruit", "yellow")
            # WEST - Sky Piea
        elif user_choice == "3":
            island7(inventory)
            # NORTH - Cap Des Jumeaux
        elif user_choice == "4":
            island1(inventory)
            # NORTH-EAST - Whiskey Peak
        elif user_choice == "5":
            island2(inventory)
            # EAST - Little Garden
        elif user_choice == "6":
            island3(inventory)
            # QUIT
        elif user_choice == "7":
            sys.exit()
            print("Goodbye! Thanks for playing!")
        else:
            cprint("\nOpps! Looks like your ship hit a bump! Try Again", "blue")

# Calls the first island
def main():
    inventory = []
    welcome(inventory)

main()
