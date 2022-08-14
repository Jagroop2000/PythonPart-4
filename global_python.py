count = 1

def counter():
    global count
    count+=1
    return count

print(counter())

# Not Recommended to use