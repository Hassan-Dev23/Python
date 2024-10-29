import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()
# Your code here
print("<------------------------->\n")
# Veriable declaration 
name = None
str = "Hassan"
ch = 'h'
interger = 19
boolean = True
floated = 5.734
literelforParagraph = """This is a paragraph.
It spans multiple lines.
Each new line is recognized."""


# Build-in string Methods 

# print(str)
# ustr = str.upper()
# print(ustr)
# lstr = str.lower()
# print(lstr)
# Captilizedstr = lstr.capitalize()

# Mastrig Print statment using different fuction like .formate , f, % 

# print("This is %s and this is %s and this is used for integer %d"
      #  %(Captilizedstr,lstr,interger))
      
# print(f"This is {Captilizedstr} and this is {lstr}")

# print("This is {} and this is {}".format(Captilizedstr,lstr))

# print("this is string with float %.3f"%floated)

# using Three quotes (""" """) to directly print paragraph in python 

# print("""This is a paragraph.
# It spans multiple lines.
# Each new line is recognized.""")




# String functions 

string = "Hassan is a good boy"
string
print(string)
