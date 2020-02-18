# Ainara Ruiz Castillo
# I am creating a program that confirms wethers is weekday or not. 


import datetime
import calendar


L={0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday",6:"Sunday"}

todaydate = datetime.datetime.today().weekday()

print("Today is", L[todaydate])

if todaydate<5:
    print ( "unfortunately not weekend")

else:
    print ("finally weekend!")
    
