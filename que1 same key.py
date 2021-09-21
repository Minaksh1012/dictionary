# Write a program such that the below given dictionaries are into a single dictionary and add the values having same key.
# Example :-
# Input :-


dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
for key in dic1:
    if key in dic2:
        dic2.update(dic3)
        dic2[key]=dic1[key]+dic2[key]
    else:
        dic2[key]=dic1[key]    
print(dic2)    


# Output :-

# {1: 10, 2: 60, 3: 30,  5: 50, 6: 60} 


