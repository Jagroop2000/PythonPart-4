some_list = ['a','b','c','b','d','m','m']

duplicates = set([ char for char in some_list if some_list.count(char)>1])
print(duplicates)