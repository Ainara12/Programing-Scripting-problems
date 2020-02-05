#This program calculates Body Mass Index (BMI) 
# using person's height 
# in centimetres and weight in KG
# If person BMI < 18.5 , this person is underweight
# If person BMI < 26 , this person has a normal weight
# If person BMI >26 , this person is overweight

Weight = float (input ("Enter weight in kg")) 
Height = float (input ("Enter height in cm")) 


BMI  = Weight ** 2/(Height)


print("Your BMI is", BMI ) 


