from time import sleep

Cointypes = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1.00, 2.00] 
COIN_DICTIONARY = {
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

def Calculator(Weight,Real_Coin,Bag_weight):
    if Weight > Bag_weight:
        difference = Weight - Bag_weight
        difference2 = difference / Real_Coin
        print ("You need to Remove " +str (difference2) , " coins from bag") 
    if Weight < Bag_weight:
        difference = Bag_weight - Weight
        difference2 = difference % Bag_weight
        difference3 = difference2 / Real_Coin
        print ("You need to add " +str (difference3) , " coins from bag")

def allvolanteers():
    pass

def accuracy():
    pass

def coincounting():
    Name = input("What is your name? ")
    i = int(input("How many bags do you want to count? ")) 
    count = 0
    while count != i: 
        Coin = float(input("What is the value of the coin in the bag? (Please use 0.00 to indicate) "))
        if Coin not in Cointypes:
            Coin = print("Invalid coin type please re-enter")
            sleep(2)
            continue
        Weight = float(input("What is the weight of the bag? "))
        Real_Coin = COIN_DICTIONARY["Coin Weight"][Coin]
        Bag_weight = COIN_DICTIONARY["Bag weight"][Coin]
        count = count + 1
        Calculator(Weight,Real_Coin,Bag_weight)
        sleep(1)


def main():
    menu()

def menu():
    print("""         ____                                                           __                            
        /\  _`\           __                                           /\ \__  __                     
        \ \ \/\_\    ___ /\_\    ___         ___    ___   __  __    ___\ \ ,_\/\_\    ___      __     
         \ \ \/_/_  / __`\/\ \ /' _ `\      /'___\ / __`\/\ \/\ \ /' _ `\ \ \/\/\ \ /' _ `\  /'_ `\   
          \ \ \L\ \/\ \L\ \ \ \/\ \/\ \    /\ \__//\ \L\ \ \ \_\ \/\ \/\ \ \ \_\ \ \/\ \/\ \/\ \L\ \  
           \ \____/\ \____/\ \_\ \_\ \_\   \ \____\ \____/\ \____/\ \_\ \_\ \__\\ \_\ \_\ \_\ \____ \ 
            \/___/  \/___/  \/_/\/_/\/_/    \/____/\/___/  \/___/  \/_/\/_/\/__/ \/_/\/_/\/_/\/___L\ \
                                                                                           /\____/
                                                                                           \_/__/""")
    print()
    
    Choice = input("""

                        A: Show all volanteers 
                        B: Count Coin!
                        C: Show accuracy of all volanteers
                   
                        Please enter your choice: """)
    
    if Choice == "A" or Choice == "a":
        allvolanteers()
    if Choice == "B" or Choice == "b":
        coincounting()
    if Choice == "C" or Choice == "c":
        accuracy()

menu()
