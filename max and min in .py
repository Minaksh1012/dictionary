my_dict = {'x':500, 'y':5874, 'z': 560}

# key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
# key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

# print('Maximum Value: ',my_dict[key_max])
# print('Minimum Value: ',my_dict[key_min])

b=3
for max in my_dict:
    if my_dict[max]>3:
        print(my_dict[max])