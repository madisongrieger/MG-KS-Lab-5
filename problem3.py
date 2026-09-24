def roman_to_decimal(string):
  """
 string -> whole number
  takes in a string as a Roman numeral and returns the whole number it corresponds to.

  >>> roman_to_decimal("XIX")
  19
  >>> roman_to_decimal("MCMX")
  1910
  >>> roman_to_decimal("III")
  3
  """
  result=0
I=1
V=5
X=10
L=50
C=100
D=500
M=100
while len(string)>0:
   if string[0:2]== "IV":
   result= result + 4
   string = string[2:]
 elif string[0:2]== "IX":
   result= result + 9
   string = string[2:]
elif string[0:2]== "XL":
   result= result + 40
   string = string[2:]
elif string[0:2]== "XC":
   result= result + 90
   string = string[2:]
elif string[0:2]== "CD":
   result= result + 400
   string = string[2:]
elif string[0:2]== "CM":
   result= result + 900
   string = string[2:]
return result 
