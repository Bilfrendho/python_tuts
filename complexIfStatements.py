country=input("Please enter your country\n").upper()
pet=input("Please enter your pet name\n").upper()
#if country=="CANADA" and (pet=="MOOSE" or pet=="BEAVER"):
#    print("That was cool!")

#method 2
countryCanada=False
if country=="canada".upper():
    countryCanada=True
petName=False 
if pet=="moose".upper() or pet=="beaver".upper():
    petName=True
if countryCanada and petName:
    #
    print("I love Canadian pets ")
    #men what is happening


