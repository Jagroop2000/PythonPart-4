# Scope : What Variables do I have Access to  ?

# 1 - start with local 
# 2 - Parenl LOcal 
# 3 - Global
# 4 built in python

a = 1

def parent():
    a=10
    def confusion():
        return a
    return confusion()

print(parent())
print(a)
