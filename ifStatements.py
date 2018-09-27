##prompt=input ("Kindly enter your favourite football league \n ")
##if prompt.capitalize()=="Epl":
##    print("Bull's eye! ")
##print("No worries!")
##We are going to prompt the user to enter a number and check if it is greator than a certain value
#deposit=float(input("Please enter the deposit value\n "))
#freeToaster=False
##deposit=float(deposit)
#if deposit>=100:
#    freeToaster=True
#    print("You are going to get some bonus and interest ")
#else:
#    print("Have a nice day ")
##print("Have a nice day\n ")

##Challenge for the day
#amount=float(input("Please enter the amount for your total purchase\n "))
#totalAmount=False
#if amount<50:
#    newAmount=amount+10
#    #flag down here(totalAmount)
#    totalAmount=True
##complex code here
##if totalAmount:
#    print("Your total amount shall be $%d " %newAmount)
##if totalAmount==False:
#if not totalAmount:
#    print("Your total amount has been discounted and shall be $%d " %amount)
#print("Thank you for shipping with us. Have a nice day!")
  
#method 2
amount=int(input("kindly input the shipping amount\n"))
if amount<50:
    newAmount=amount+10
    print("Your total amount for shipping is $%d "%newAmount)
else:
    print("Your total amount has been discounted and shall be $%d "%amount)
print("Thank you for shipping with us and do have a nice day.")
    
   