#This program calculates the successive values of the following
# calculation: Next value by taking the positive integer added by user
# and if it is even divide it by two, if it is odd, multiply by
#three and add one.Program ends if current value is one. 

pnumber=int(input("Enter a positive integer here:"))

while pnumber > 0:
    if pnumber ==1:
        print(pnumber)
        break

    if pnumber % 2 == 0:
        print(pnumber)
        pnumber = pnumber / 2
    elif pnumber % 2 != 0:
        print(pnumber)
        pnumber = pnumber*3+1


#If user enters a not positive integer , the program confirmes this and stops. 
while pnumber < 0:
    print pnumber, "is not a positive integer." 
    break




