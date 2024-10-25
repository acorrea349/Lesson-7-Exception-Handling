# Task 1: Start Begin by asking the user to enter the temperature in Fahrenheit.

# Task 2: Temperature Conversion Write a function that converts the Fahrenheit temperature to Celsius. Remember that the formula is 
# (Fahrenheit - 32) * 5/9.

# Task 3: User Experience Implement an else block that prints the converted temperature in a user-friendly format. 

# Example: "100 degrees Fahrenheit is 37.78 degrees Celsius."

# Task 4: Finally Add a finally block that thanks the user for using the weather forecast application, ensuring that this message
# is displayed regardless of whether an exception was caught or not.

fahrenheit = input("Please enter the Fahrenheit degree you wish to convert to Celcius: ")


def fahrenheit_to_celsius():
    return (float(fahrenheit) - 32) * 5/9
    


def celsius_result():

    try:   
        user_temp = fahrenheit

    except ValueError:
        print("Error: Please input a temperature using digits.")
    else:
        print(f"{user_temp}° Fahrenheit is {fahrenheit_to_celsius():.0f}° Celsius")

    finally:
        print("Thank you for using the weather forecast app.")

print(celsius_result())
