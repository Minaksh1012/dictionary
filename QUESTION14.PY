# # Ek program likho jo ki dictionaries ki values ko sort(ascending or descending) kar de.

# # Input :-

a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}

# # Expected result in Ascending Order:

# # {'param':20,'anjili':30,'bijender':45,'roshini':50,'deepak':60}

# # Expected result in Descending Order:

# # {'deepak':60,'roshini':50,'bijender':45,'anjili':30,'param':20}

# h={}
# for i in a:
#     c=a[i]
#     for i in a:
#         b=a[i]
#         if c>b:
#             h[i]=b
# for i in a:
#     c=a[i]
#     for i in a:
#         b=a[i]
#         if c<b:
#             h[i]=b
# print(h)                        

# a=56
# b=5
# print=9
# print


h={}
for i in a:
    c=a[i]
    for i in a:
        b=a[i]
        if c<b:
            h[i]=b
for i in a:
    c=a[i]
    for i in a:
        b=a[i]
        if c>b:
            h[i]=b
print(h)  


# a=2.5
# b=12
# print(a,b)
