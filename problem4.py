def power_of_three(n):
  """
  postive number -> boolean
  takes an integer and returns True if it is a power of three and False otherwise

  >>> power_of_three(27)
  True
  >>> power_of_three(0)
  False
  >>> power_of_three(-10)
  False
  >>> power_of_three(81)
  True
  >>> power_of_three(33)
  False
  """
 if n<=0:
      return false
   while n % 3 ==0:
     n= n // 3
   return n==1
