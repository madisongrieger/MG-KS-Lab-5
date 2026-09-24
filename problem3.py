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
  >>> roman_to_decimal("CDXLI")
  441
  >>> roman_to_decimal("XDL")
  560
  """
  result=0
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
     elif string[0:1]== "I":
         result= result + 1
         string = string[1:]
     elif string[0:1]== "V":
         result= result + 5
         string = string[1:]
     elif string[0:1]== "X":
         result= result + 10
         string = string[1:]
     elif string[0:1]== "L":
         result= result + 50
         string = string[1:]
     elif string[0:1]== "C":
         result= result + 100
         string = string[1:]
     elif string[0:1]== "D":
         result= result + 500
         string = string[1:]
     elif string[0:1]== "M":
         result= result + 1000
         string = string[1:]
  
  return result 
