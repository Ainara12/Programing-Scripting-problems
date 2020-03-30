#This program calculates the successive values of the following
# calculation: Next value by taking the positive integer added by user
# and if it is even divide it by 2, if it is odd, multiply by
#3 and add 1.Program ends if current value is 1. 

#First: I created variable "pnumber" which will be the positive integer entered by the user.

pnumber=int(input("Enter a positive integer here:"))

#Created formula to find out if number entered by user is positive integer ( greater than 0)

while pnumber > 0:
    if pnumber ==1:# then if number greater than 0 and equals 1, program stops with break statement.
        print(pnumber)
        break

    if pnumber % 2 == 0:# if number entered by user is even we divide numbers by 2.
        print(pnumber)
        pnumber = pnumber / 2
    elif pnumber % 2 != 0: #if number entered by user is odd we multiply the values by 3 and add 1. 
        print(pnumber)
        pnumber = pnumber*3+1


#If user enters a not positive integer , the program confirmes this and stops. 
while pnumber < 0:
    print pnumber, "is not a positive integer." 
    break




print ("Thank you so much for using my program")