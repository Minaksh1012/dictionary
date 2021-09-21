d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
# d = d1.copy()
# d.update(d2)
# print(d)


for key in d1:
    if key in d2:
        d1.update(d2)
    else:
        d2[key]=d1[key]    
print(d2)   