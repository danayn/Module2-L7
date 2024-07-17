'''
This is a note for Module 2 of Python Basics. 
This is a Multi-line String comment. 

LESSON 7: Python Exception Handling

'''
#Type of Errors

#Syntax Errors --> are invalidities in the code's structure. 
#In other words, Python syntax errors happen when the Python interpreter is unable to recognize the structure 
#of statements in code. 
#Every language follows certain rules to make sense of what's being told and written.

#Python can tell you where the error is in a Syntax Error through an Error Message.

#-----------------------------------------------------------------------------------------------------

#Exceptions --> Even if a statement or expression is syntactically correct, 
# it may cause an error when an attempt is made to execute it. 
# Errors detected during execution are called exceptions and are not unconditionally fatal

#Python can tell you the type of Exception and a traceback (code where error is) in an Error Message. 

#-----------------------------------------------------------------------------------------------------


#Name Error -- example -- print(age) -- not defined(age)

#Value-Error --> Example -- supposed to enter a number instead of string  or vice versa

#File Not Found Error --> Example -- No such file or directory called exists

#OverFlow Error --> when calculated number is way too big. 

#Type Error --> when mixing types (such as adding string + number) that don't go together

#RunTime Error --> when function calls itself forever. It will cause RunTime error due to recursion (function calling itself) 
# limit. #Recursion Error is subset of Runtime Error. 


#Try and Except block
try:
   #Code that might cause an exception
   #user_input = int(input("Enter a number: "))
   x = 0
except:
   #Code to handle the exception
   print("Oops! That was no valid number. Try again... ")



try: 
   #Code that might cause multiple exceptions
   data = [1, 2, 'a', 4]
   number = int(input("Enter a number: ")) 
   result = 100 / number
except ValueError:
   #Code to handle incorrect input type
   print("Please enter a valid integer.")
except ZeroDivisionError:
   #Code to handle division by zero
   print("Sorry, infinity is not on the menu today. Try a non-zero number. ")
#To catch all exceptions
except Exception as e:
   #Code to handle an unexpected exception ----------------------------------------------------------|
   print(f"An unexpected error occured: {e}")
else:
   print("You have entered a number successfully.")
finally:
   print("This code will run no matter what.")

#Raise an Exception
fuel_level = -1
#if fuel_level < 0:
   #raise ValueError("Fuel level cannot be negative.")

#Custom Exceptions
fuel_level = 10
tank_capacity = 9

class FuelTankOverflowError(Exception):
   """Exception raised when the fuel tank is overfilled."""
   pass

if fuel_level > tank_capacity:
   raise FuelTankOverflowError("Fuel has exceeded the tank capacity")



   
   
