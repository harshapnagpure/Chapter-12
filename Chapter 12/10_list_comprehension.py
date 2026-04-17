
# a = [3, 6, 7, 4, 54,34, 32,1 ,2 ,4, 3, 3]
# b =[]
# for item in a:
#     if item%2==0:
#        b.append(item)
# print(b)




# list comprehensions:
# shortcut to write the same:
a = [3, 6, 7, 4, 54,34, 32,1 ,2 ,4, 3, 3]
b =[i for i in a if i%2==0]
print(b)

t = [1, 4, 5, 5, 3, 4 , 4,2]
s = {i for i in t}
print(s)