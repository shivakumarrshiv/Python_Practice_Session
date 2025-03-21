year = int(input("Enter the Year :"))
leap = False
if year>0:
    if year%4 == 0:
        if year%100 == 0:
            if year%400==0:
                leap =True
        else:
            leap = True
if leap:
    print("It is Leap Year")
else:
    print("No this is not Leap Year")