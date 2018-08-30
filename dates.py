import datetime
currentDate=datetime.datetime.today()
prompt=input("Kindly enter the deadline date for your project in the format(mm/dd/yyy)\n ")
deadLine=datetime.datetime.strptime(prompt,"%m/%d/%Y")
daysRem1=deadLine-currentDate
#for extra credit lets give them the combination of weeks and days remaining
weeks=daysRem1.days/7
daysRem2=daysRem1.days%7
print("The remaing days to the project deadline is %d " %weeks + "and %d " %daysRem2 +"days\n")
