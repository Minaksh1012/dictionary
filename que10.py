dict =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}

# Output :-

# total count:5


count=0
for i in dict.keys():
    for j in dict[i]:
        count+=1
print(count)       