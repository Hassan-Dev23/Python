import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()
# Your code here
print("<------------------------->\n")
hassan = "hassan"
Hassan = "Hassan"
# # membesip operator 
# print("e" in hassan)
# # conditional operators in python
# print(hassan>Hassan)
# print(hassan==Hassan)
# cap=0
# low=0
# # arithmatic in for loop 
# for i in hassan:
#     low+=ord(i)

# for i in Hassan:
#     cap+=ord(i)    

# print(cap,low)

for i in range(len(hassan)):
    print(hassan[i])

# operators : arithmatic , assingnment, logical , membership 
if hassan < Hassan :
    print(Hassan)
elif hassan > hassan:
    print(hassan)
else:
    print("ha" * 3)

list= [1,3,4,5,6,6]
ha = list.index(6)
print(ha)


_ha="hab"
print(_ha)
