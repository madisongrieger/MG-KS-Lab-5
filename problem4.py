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
  while n%==3:
    n= n // 3
    if n<=0:
      return false
  return n==1
