try:
    number = int(input("Type a number: "))
    1/number
except:
    print("You cannot devide a number by 0.")
else:
    print("There are no errors.")
finally:
    print("This is the end.")