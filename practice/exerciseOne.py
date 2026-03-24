def arithmeticProduct(x, y):
    product = x * y
    if product <= 1000:
        return product
    else:
        return x + y

print(arithmeticProduct(10,20))
print(arithmeticProduct(20,40))
print(arithmeticProduct(20,60))
