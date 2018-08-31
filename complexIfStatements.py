#country=input("Please enter your country\n").upper()
#pet=input("Please enter your pet name\n").upper()
##if country=="CANADA" and (pet=="MOOSE" or pet=="BEAVER"):
##    print("That was cool!")

##method 2
#countryCanada=False
#if country=="canada".upper():
#    countryCanada=True
#petName=False 
#if pet=="moose".upper() or pet=="beaver".upper():
#    petName=True
#if countryCanada and petName:
#    #
#    print("I love Canadian pets ")
#men what is happening
#don worry I have got these figured out 
#prompt=input("Please enter the day of the week: ").capitalize()
#Saturday=True
#freshMilk=False
#if Saturday:
#    #Saturday=True
#    if not freshMilk:
#        print("Buy some fresh milk buddy!")
#    print("Wooorei! I love weekends. ")
#else:
#    freshMilk=False
#    print("Wait till Saturday. ")

#Challenge Time!!
country=input("Which Country do you belong to?\n ").capitalize()
orderTotal=float(input("What is your current order Total?\n "))
Canada=False
if country=="Canada":
    Canada=True
    province=input("Which province do you belong to?\n (Please Enter Province in one word) ").capitalize()
    if province=="Alberta":
        #GST refers to General sales tax
        GST=0.05/100
        neworderTotal=(GST+100)/100*orderTotal
        #print(neworderTotal)
        print("You have been taxed General Sales Tax \non your order total and your new order total is ${0:f}".format(neworderTotal))
      #  print("Your tax is ${0:.4f}".format(neworderTotal))
    elif province=="Ontario"or province=="Newbrunswick" or province=="Novascotia":
        #HST refers to Harmonized sales tax
        HST=0.13/100
        neworderTotal=(HST+100)/100*orderTotal
        print("You have been taxed Harmonized Sales Tax\n on your order total and your new order total is ${0:f}".format(neworderTotal))

    else:
        #PST refers to Provincial sales tax
        #GST refers to General sales tax
        PST=0.06
        GST=0.05
        tax=PST+GST
        newPST=tax/100
        neworderTotal=(newPST+100)/100*orderTotal
        print("You have been taxed General Sales Tax and Provincial Sales Tax\n on your order total and your new order total is ${0:f}".format(neworderTotal))
else:
    print("Your have been exempted from paying taxes. Your order total is ${0:f}".format(orderTotal) +" \nDo have a good day.")




