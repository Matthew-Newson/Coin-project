#ALL IMPORTS
from time import sleep
import os
import sys

#DECLARING CONSTANTS
COINTYPE = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1.00, 2.00] 
COIN_DICTIONARY = {      #Dictionary that uses coin input as a key to get coin weight and bag weight
    "Coin Weight" : {
        0.01 : 3.56,
        0.02 : 7.12,
        0.05 : 2.35,
        0.10 : 6.50,
        0.20 : 5.00,
        0.50 : 8.00,
        1.00 : 8.75,
        2.00 : 12.00
    },
    "Bag weight" : {
        0.01 : 356.00,
        0.02 : 356.00,
        0.05 : 235.00,
        0.10 : 325.00,
        0.20 : 250.00,
        0.50 : 160.00,
        1.00 : 175.00,
        2.00 : 120.00

    },
}

#DEFINING FUNCTIONS
def Calculator(Weight,Real_Coin,Bag_weight,correct):  #Calculates how many coins you need to add and remove from your bag
    if Weight > Bag_weight:
        difference = Weight - Bag_weight
        difference2 = difference / Real_Coin
        print ("You need to Remove " +str (difference2) , " coins from bag")
        sleep(1)
    if Weight < Bag_weight:
        difference = Bag_weight - Weight
        difference2 = difference % Bag_weight
        difference3 = difference2 / Real_Coin
        print ("You need to add " +str (difference3) , " coins from bag")
        sleep(1)
    if Weight == Bag_weight:
        print("Bag weight is correct")
        sleep(1) 
        return True
     

def save_data(Name, count, accuracy_percentage): #Saves data to file
    file.close()
    file = open("Coin_count.txt", "+a") 
    file.write (f"\n{Name} , Total bags counted {count} , Accuracy {accuracy_percentage}") 
    file.close()
    print("Data save")
    menu()

def read_data(Name, count, accuracy_percentage): #Reads the file
    file = open("Coin_count.txt", "+r")
    texts = file.readlines()
    data = -1
    for lines, text in enumerate(texts):
        while data != 0:
            data = text.find(Name)
            print(data)



def adduser(): #Updates file if name is already in file
    pass


def allvolunteers(): #Prints all volunteers saves in the file
    pass

def accuracy(i,correct): #Calculates the accuracy in percentage
    accuracy = correct / i 
    accuracy2 = accuracy *100
    accuracy_percentage = round(accuracy2)
    print(accuracy_percentage) 
    return accuracy_percentage 

def coincounting(): #Main part of the code that counts the coins and asks
    Name = input("What is your name? ")
    i = int(input("How many bags do you want to count? ")) 
    correct = 0
    count = 0
    while count != i:
        try:
            Coin = float(input("What is the value of the coin in the bag? (Please use 0.00 to indicate) "))
        except:
            print("Invalid data entered please retry") 
            continue
        else:
            if Coin not in COINTYPE:
                Coin = print("Invalid coin type please re-enter")
                sleep(1)
                continue
        Weight = float(input("What is the weight of the bag? "))
        Real_Coin = COIN_DICTIONARY["Coin Weight"][Coin]
        Bag_weight = COIN_DICTIONARY["Bag weight"][Coin]
        count += 1
        result = Calculator(Weight,Real_Coin,Bag_weight,correct)
        if result is True:
            correct += 1
    accuracy_percentage = accuracy(i,correct)
    sleep(1)
    read_data(Name, count, accuracy_percentage)
    

def main():
    menu()

def menu():  #Main menu 
    print("""  _____     _        _____               __  _          
 / ___/__  (_)__    / ___/__  __ _____  / /_(_)__  ___ _
/ /__/ _ \/ / _ \  / /__/ _ \/ // / _ \/ __/ / _ \/ _ `/
\___/\___/_/_//_/  \___/\___/\_,_/_//_/\__/_/_//_/\_, / 
                                                 /___/""")
    print()
    
    Choice = input("""
        A: Show all volunteers 
        B: Use already excising volunteers
        C: Show accuracy of all volunteers
        D: Add new volunteer
        E: End program
                   
    Please enter your choice: """)
    
    if Choice.lower() == "a": 
        allvolunteers()
    if Choice.lower() == "b" :
        coincounting()
    if Choice.lower() == "c" :
        accuracy()
    if Choice.lower() == "d" :
        adduser()
    if Choice.lower() == "e" :
        sys.exit()
    
menu()
