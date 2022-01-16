def vatCalculate(totalPrice):
    result = totalPrice + (totalPrice*0.07)
    return result

value = int(input("Price :"))
print(vatCalculate(value))


