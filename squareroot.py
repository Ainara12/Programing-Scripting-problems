#Ainara Ruiz Castillo

#I am creating my first function following steps from week 6 tutorials
 #this week task consists of writing a program that consists of taking a positive floating-point number and outputing
#an approximation of its square root.


#First I created variable x which would be any positive floating -point number that user enters
x= float (input ("Please enter a positive floating-point number"))

#Second,  I created a function which I will call "sqrt" which returns the squareroot of the value
#entered by the user

def sqrt (x):
    return x ** 0.5

#As a result of this calculation , the program prints the value entered by user 
# followed by its approximated square root.
print ("The square root of ", x , "is approx" ,sqrt(x))

print ("Thanks for using my program")
 


  








#Using our recommended reading "A Whirlwind Tour of Python" I consulted "Defining and Using Functions" section: