User = input("Username =")
Pass = input("Password =")
if  User == "admin" and Pass == "admin":
    print("--------------------------")
    print("Welcome To Admin Supermarket")
    print("--------------------------")
    print("Menu")
    print("No.1 : Banana (Price 50)")
    print("No.2 : Cake (Price 70)")
    print("No.3 : Apple (Price 80)")
    print("--------------------------")
    print("Please Select No. of menu")
    x = int(input("No. ="))
    if  x==1:
        NoBanana = int(input("Please input amount of Banana ="))
        print("Total Price :", 50, "x", NoBanana, "=", 50*NoBanana, "THB")
    elif  x==2:
        NoCake = int(input("Please input amount of Cake ="))
        print("Total Price :", 70, "x", NoCake, "=", 70*NoCake, "THB")
    elif  x==3:
        NoApple = int(input("Please input amount of Apple ="))
        print("Total Price :", 80, "x", NoApple, "=", 80*NoApple, "THB")
else:
    print("Incorrect Username or Password")

