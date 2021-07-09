try:
    n=int(input("Enter numerator: "))
    d=int(input("Enter denominator: "))

    r=n/d
    print(r)

except ZeroDivisionError:
    print("Not working")

print("Program ends")