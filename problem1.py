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
  if n<=0:
    return 
  while n%2==0:
    n= n//2
  while n%3==0:
    n= n//3
  while n%5==0:
    n= n//5
  return n==1
  
