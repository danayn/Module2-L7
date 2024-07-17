#Assignment: Python Exception Handling

'''
1. Exceptional Weather Forecast

Objective: The aim of this assignment is to enhance your understanding of exception handling by creating a weather 
forecast application that gracefully handles unexpected user input and provides user-friendly error messages.

Task 1: Start Begin by asking the user to enter the temperature in Fahrenheit.

Task 2: Temperature Conversion Write a function that converts the Fahrenheit temperature to Celsius. 
Remember that the formula is (Fahrenheit - 32) * 5/9.

Use a try block to catch any potential errors during the conversion process. What happens 
if they type out "thirty" instead of doing 30?

Task 3: User Experience Implement an else block that prints the converted temperature in a user-friendly format. 

Example: "100 degrees Fahrenheit is 37.78 degrees Celsius."

Task 4: Finally Add a finally block that thanks the user for using the weather forecast application, 
ensuring that this message is displayed regardless of whether an exception was caught or not.

'''
#Task 1
try:
      x = int(input("Enter the temperature in Fahrenheit: "))
      y = 0
except ValueError:
      #Code to handle incorrect input type
      print("Please enter a valid integer.")
except Exception as e:
      #Code to handle an unexpected exception
      print(f"An unexpected error occured: {e}")
finally:
        print("Thank you for using this weather forecast application.")

#Task 2 + 3 + 4
def ftoc(x):
    try:
         y = (x - 32) * (5/9)
         return(f"{x} degress Fahrenheit is {y:.2f} degrees Celsius.")
    except ValueError:
        #Code to handle incorrect input type
        print("Please enter a valid integer.")
    except Exception as e:
        #Code to handle an unexpected exception
        print(f"An unexpected error occured: {e}")
    else:
        print(f"{x} degress Fahrenheit is {y} degrees Celsius.")
    

print(ftoc(x))


