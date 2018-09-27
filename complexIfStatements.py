country=input("Which country are you from?\n").capitalize()
orderTotal=int(input("What is your order total for all your goods?\n"))
if country=="Canada":
    province=input("Which Canadian province do you come from?\n ").capitalize();
    
    if (province=="Alberta"):
        orderTotal=(0.05/100*orderTotal)+orderTotal
        print("You have been taxed General sales Tax of ${0:f}".format(orderTotal))
    elif (province=="Ontario" or province=="New"+" Brunswick".capitalize() or province=="Nova"+" Scotia".capitalize()):
        orderTotal=(0.13/100*orderTotal)+orderTotal
        print("You have been taxed ${0:f}".format(orderTotal)+" Harmonized sales Tax")
    else:
        orderTotal=((0.06/100*orderTotal)+(0.05/100*orderTotal))+orderTotal
        print("You have been taxed ${0:f}".format(orderTotal)+"\nprovincial sales tax and general sales tax")
else:
        print("Your order total is ${0:f}".format(orderTotal))
#else:
#    print("You have been exempted from taxes and your order total is {0:f}".format(orderTotal))

    