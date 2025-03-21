Num = int(input("Enter the Number : "))
original =str(bin(Num)[2:])
flipped = original.replace("1","x").replace("0","1").replace("x","0")
Decimal = flipped
print(int(Decimal,2))