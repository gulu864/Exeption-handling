try:
    x=int(input("Enter a number:"))
    y=int(input("Enter a number:"))
    result = x/y
    print(result)

except ValueError:
    print("Please enter a number.")
except ZeroDivisionError:
    print("Please dont divide by 0.")
except NameError as exe:
    print("The error is," , exe, ".")

except:
    print("Some error occcured.")

finally:
    print("Program end.")