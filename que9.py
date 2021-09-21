a=["M","I","S","S","I","S","S","I","P","P","I"]
# iss word me har letter ki occurrency count karke ek dictionary me store karaye. 
# Jisme letter dictionary ki keys aur occurrency Uss dictionary ki values hongi.

# Example:-

# Output :-

# {M:1,I:4,S:4,P:2}

# a=input("enter the element")
dict={}
for x in a:
    keys=dict.keys()
    if x in keys:
        dict[x]+=1
    else:
        dict[x]=1
print(dict) 



