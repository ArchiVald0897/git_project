def declination():
    quantity = int(input("Введите цифру \n"))
    remainder = quantity % 100
    if remainder in range(11, 14):
        print(str(quantity) + " питонов")
    elif remainder % 10 == 1:
        print(str(quantity) + " питон")
    elif remainder % 10 == 2 or remainder % 10 == 3 or remainder % 10 == 4:
        print(str(quantity) + " питона")
    else:
        print(str(quantity) + " питонов")