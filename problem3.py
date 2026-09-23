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
 while len(string)>0:
   if string[0:2]== "IV"
   result= result+4 
   string = string[2:]
   
