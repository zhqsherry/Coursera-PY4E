largest = None
smallest = None
while True:
    number = input("Enter a number: ")
    if number == "done":
        break
    try:
        num = int(number)
    except:
        print("Invalid input")

    if largest is None:
        largest = num
    elif num > largest:
        largest = num

    if smallest is None:
       smallest = num
    elif num < smallest:
       smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)