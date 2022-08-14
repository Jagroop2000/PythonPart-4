from re import X


def outer():
    x ='Local'
    def inner():
        nonlocal x 
        x ="Non Local"
        print("Inner", x)
    
    inner()
    print("Check Outer In", x)


outer()