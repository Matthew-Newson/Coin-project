Name = input("What is your name? ")
Coin = float(input("What is the value of the coin in the bag? (Please use 0.00 to indicate) "))
Weight = float(input("What is the weight of the bag? "))

thisdict = {
    0.01: {
        Bag_weight1: 356.00,
        Coin_weight1: 3.56
    },
    0.02: {
        Bag_weight2: 235.00,
        Coin_weight2: 7.12
    },
    0.05: {
        Bag_weight3: 325.00,
        Coin_weight3: 2.35
    },
    0.10: {
        Bag_weight4: 325.00,
        Coin_weight4: 6.50
    },
    0.20: {
        Bag_weight5: 250.00,
        Coin_weight5: 5.00
    },
    0.50: {
        Bag_weight6: 160.00,
        Coin_weight6: 8.00
    },
    1.00: {
        Bag_weight7: 175.00,
        Coin_weight7: 8.75
    },
    2.00: {
        Bag_weight8: 120.00,
        Coin_weight8: 12.00
    }
}
Current_Coin = thisdict[Coin]
print(Current_Coin)




#if Current_Coin > Weight:
 #   difference = Current_Coin - Weight
  #  print(difference) 
    

#    thisdict = {
 #   0.01 : 356.00,
  #  0.02 : 235.00,
   # 0.05 : 325.00,
    #0.10 : 325.00,
    #0.20 : 250.00,
    #0.50 : 160.00,
    #1.00 : 175.00,
    #2.00 : 120.00
#}
