a = 5
b = 23

try:
    print("resource open")
    print(a/b)
    k = int(input("enter a number"))
    print(k)
except ZeroDivisionError as e:
    print("The number cannot be divided by zero", e)
except ValueError as e:
    print("Invalid input", e)
except Exception as e:
    print("something went wrong")

finally:  # finally block is excuted irrespective of the exception
    print("resource closed")