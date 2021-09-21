# {'sonu':85,
#     'Kartik':90,
#     'Deepak':96,
#     'Aman':76,
#     'Somesh':60,
#     'Umesh':85,
#     'Amarpal':70,
#     'Roshan':57,
#     'Riyaz':98,
#     'Shabid':56
# } 

a={}
n=int(input("enter the elements:"))
for i in range(n):
    k=input("enter the key:")
    v=input("enter the value:")
    a.update({k:v})
print(a)    