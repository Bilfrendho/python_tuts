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
country=""
province=""
orderTotal=0
neworderTotal=0
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
        #new things happening
        #print(neworderTotal)
        print("You have been taxed General Sales Tax \non your order total and your new order total is ${0:f}".format(neworderTotal))
        #print("Your tax is ${0:.4f}".format(neworderTotal))
        #This was good Bill. I have been wondering how this code is working
    elif province == "Ontario" or province == \
        "New"+" brunswick".capitalize() or province == "Nova"+" scotia".capitalize():
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




#country = ""
#province = ""
#orderTotal = 0
#totalWithTax = 0
#I am declaring variables to hold the tax values used in the calculations
#That way if a tax rate changes, I only have to change it in one place instead
#of searching through my code to see where I had a specific numeric value and updating it
#GST = .05  
#HST = .13
#PST = .06
#Ask the user what country they are from 
#country = input("What country are you from? " )
#if they are from Canada ask which province...don't forget they may enter Canada as CANADA, Canada, canada, CAnada
#so convert the string to lowercase before you do the comparison
#if country.lower() == "canada" :
#    province = input("Which province are you from? ")
#ask for the order total
#orderTotal = float(input("What is your order total? "))
#Now add the taxes
#first check if they are from canada
#if country.lower() == "canada" :
#    if they are from canada, we have to change the calculation based on the province they specified
#    if province.lower() == "alberta" :
#        orderTotal = orderTotal + orderTotal * GST
#    elif province.lower() == "ontario" or province.lower() == "new brunswick" or province.lower() == "nova scotia" :
#        orderTotal = orderTotal + orderTotal * HST
#    else :
#        orderTotal = orderTotal + orderTotal * PST + orderTotal * GST
#if they are not from Canada there is no tax, so the amount they entered is the total with tax
#and no modification to orderTotal is required
#Now display the total with taxes to the user, don't forget to format the number
#print("Your total including taxes comes to $%.2f " % orderTotal)