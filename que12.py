# Ek dictionary me 1 se 15 tak saare numbers ki keys banaye aur unke square unn keys ki values ho.

# Output :-

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

# n=int(input("enter the number"))
n=10
# d={i:i **2 for i in range(1,n+1)}
# print(d)





a={}
for i in range (1,n+1):
    a[i]=i**2
print(a)    