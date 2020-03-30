# Ainara Ruiz Castillo
#This program calculates the successive values of the following
# calculation: Next value by taking the positive integer added by user
# and if it is even divide it by two, if it is odd, multiply by
#three and add one.Program ends if current value is one. 

pnumber=int(input("Enter a positive integer here:")) #I defined variable 

while pnumber > 0: #defined if number is positive it goes to the second loop
    if pnumber ==1: #here if number meets condition of being 1 the program ends with break statement
        print(pnumber)
        break

    if pnumber % 2 == 0: #on the other hand, if number is even 
        print(pnumber)
        pnumber = pnumber / 2 #we divide the value by 2
    elif pnumber % 2 != 0: #else if value entered is odd
        print(pnumber)
        pnumber = pnumber*3+1 #we proceed to multiply by 2 and add 1 to the result.


#If user enters a not positive integer , the program will confirmed it by printing the indication and stopping. 
while pnumber < 0:
    print pnumber, "is not a positive integer." 
    break




