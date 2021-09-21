Dic= {
    1: 'NAVGURUKUL',
    2: 'IN',  
  	3:{    
        'A' : 'WELCOME',
        'B' : 'To',
        'C' : 'DHARAMSALA'
        }
    }

# Output :-

# Dic= {
#     1: 'NAVGURUKUL',
#     2: 'IN',  
#   	3:
#       { 'B' : 'To',
#         'C' : 'DHARAMSALA'
#        }
#     }

del Dic[3]["A"]
print(Dic,end=" ")
print()