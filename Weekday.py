# Ainara Ruiz Castillo
# I am creating a program that confirms wethers is weekday or not. 


import datetime #I imported datetime library in order to work with dates as objects


L={0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday",6:"Sunday"} #then I created this list in which I asigned a number
#to everyday of the week and set variable todaydate to return current date

todaydate = datetime.datetime.today().weekday()

print("Today is", L[todaydate])#then using  if statement along with current day it will print a different message depending

if todaydate<5: #on if the current date is lower than 5 in which case as the message is printed is not weekend
    print ( "unfortunately not weekend")

else:#or else the weekday number is greater than 5 then we have a case of
    print ("finally weekend!")# weekend message being printed. 
    
