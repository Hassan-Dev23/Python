import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()
# Your code here
print("<------------------------->\n")
# In Python any data structure can hold any datatype_value
# Python can print whole list by its name (without loop like in other languages)

# List in python : Orderd indexed modifiable allow_duplicates resizeable
# Defined -> List_name =[..,..,..,..]
List = [0,1,2,3,4,5,6,7,8,9,10]
# print(List)
# print(List.count(1)) # Count that perticular element in the list
# print(List[::-1])
# print(list(reversed(List)))
DataList = [1,"hassan",True,0.5,'x']
# print(DataList + List)


# Tuple IN Python : like List but can't be modified 
# Definition-> Tuple_name = (..,..,..,..)
Tuple = (1,3,34,2.5,True,"Hassan")
print(Tuple)


# Set in Python : not ordered , not indexed , no duplicates , modifiable , resizeable 
# Definition -> set_name = {..,..,..,..}
# If duplicatd value is initialized in set it will not take it whenever it is used 
Set = {1,3,34,4, 4}

print(Set)

# Dictonary in Python : keys as index , ordered , keys can't be duplicated but values can be,modifiable , resizeable 
# Definition -> Dict-name = { key:value, key:value, key:value }

Dictionary = {"name":"Hassan","age":19,"student":True}
Dictionary["edu"]= 13 # Adding new value
Dictionary["student"] = "ADP CS Semester:2" # modifiying value of specific key
print(Dictionary)
