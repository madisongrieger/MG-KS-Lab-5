def ugly_number(n):
  """
  positive number -> boolean
  given an integer n, returns True if n is an ugly number and False otherwise
  
  >>> ugly_number(6)
  True
  >>> ugly_number(1)
  True
  >>> ugly_number(14)
  False
  >>> ugly_number(10)
  True
  >>> ugly_number(22)
  False
  """
  if n%2==0:
    return True
  elif n%3==0:
    return True
  elif n%5==0:
    return True
  else:
    return False
  ugly_number(6)
  print True
