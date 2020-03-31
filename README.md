#**Programming & scripting problems**

##**Purpose of this repository:**

Hi my name is Ainara Ruiz Castillo and this is my Programming & scripting problems repository. 

 This repository includes the weekly tasks we have being asked to complete weekly and the attemps I made in order to solve these. 
 I have also attached any extra files that might be part of the tasks such as "Moby Dick.txt" or "Plotfromweek8task.png".

Before adding the code for every task I briefly comment which one is the purpose of the task and the result we are expecting.
Then I have also included extra comments as clarification in some parts of the code that might be confusing to understand.

Every weekly task/problem is named with the suggested name advised by the lecturer in every task description. 

**Repository content list:**

```
1. BMI.py
2.SecondString.py
3.Collatz.py
4.WeekDay.py
5.Squareroot.py
6.Es.py
7.Moby Dick.txt 
8.Week8task.py
9.Plotfromweek8task.png

```

**Content description**

**1.BMI.py**

This task has the purpose to find out the BMI of the user by taking two inputs : person's height in cm and weight in KG . 
The result will indicate that this person is overweight, normal or underweight.

The parameters to decide this are as follows:

*If person BMI < 18.5 , this person is underweight*  
*If person BMI < 26 , this person has a normal weight*  
*If person BMI >26 , this person is overweight*  

Using the BMI calculating formula , we created a script that takes Weight and Height as inputs , calculate with formula and print message indicating which one is the BMI for the user. 

**References**  
https://stackoverflow.com/questions/20405610/bmi-calculator-in-python/20405792  

**2.SecondString.py**

This task consists in using a sentence entered by the user, the program creates a sentence in which characters shown are every second letter in reverse.
I added the sentence *The quick brown fox jumps over the lazy dog* as an example to use . The result should be:*.o zletrv pu o wr cu h*

**References**  
https://docs.python.org/3/tutorial/datastructures.html

**3.Collatz.py**

In this task we had the goal to create a program which asks the user to enter a positive integer. Then using a *while* loop the program decides if it needs to stop ( in case that the value entered is 1), divided by 2 (if the value is even) or multiply by 3 and add 1 ( if value is odd). I have also added the option that the number entered might not be a positive integer , then the program prints the message confirming the value is not positive and stops.

**References**  
https://realpython.com/python-while-loop/#the-while-loop  
https://stackoverflow.com/questions/14591872/adding-consecutive-integers-in-python-with-a-twist  

**4.Weekday.py**

With this task the goal was to create a program that would confirm if the current day is weekday or weekend.
For this task I imported *datetime* module in order to convert dates in date objects.
The works for this code are well explained within *Weekday.py* but basically we are using a *if* statement to advise different message outputs depending on wether the current day is between 0 ( Monday) and 4 (Friday)or else is greater than 5 which implies it is Saturday(5) or Sunday (6)

**References**  
https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python  
https://www.w3schools.com/python/python_datetime.asp  

**5.Squareroot.py**

In this task I had to write a program that takes  a positive floating-point number entered by the user and outputs then
an approximation of its square root, taking as reference Newton's square root method.
The code is self explanatory and had comments indicating how it works. Basically we create a variable for the user input , then I created a function named "sqrt" as was required by the task with is return as the formula to find the approximate square root. 
At the end the program prints the value entered by user and the square root calculation result.

**References**  
https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d

**6.Es.py**

For this task the goal is to create a program that counts how many times a character shows in a text file. In this case we needed to find how many *e's* in the text file *Moby Dick.txt*.
The method is explained in comments in the code as always, but basically I first opened this text file in read mode and using *count* function found how many *e's* are there. 

**References**  
https://realpython.com/read-write-files-python/    
https://realpython.com/python-strings/  

**7.Week8task.py**

For this task I needed to create a plot of the functions:  f(x)=x ,g(x)=x2 and h(x)=x3 in the range 0-4.
Instructions are in comments within the code but as a summary: First I imported both libraries *matplotlib.pyplot* and *numpy* and create range evenly separated using *np.linspace* , I used object oriented approach to create the plot.
The plot resulted from this program is attached to this repository as *Plotfromweek8task.png*.

**References**  
https://matplotlib.org/tutorials/introductory/pyplot.html  
https://realpython.com/python-matplotlib-guide/#stateful-versus-stateless-approaches  


Thanks so much for reading this document. If you need further information do not hesitate to consult me. 

Ainara Ruiz 
