def divisible_by_m(n,m):
  """
  number number-> boolean 
  take as input two numbers n and m and will return True if n is a multiple of m and False otherwise
 
  >>> divisible_by_m(3,2)
  False
  >>> divisible_by_m(0,4)
  True
  >>> divisible_by_m(-6, 2)
  True
  >>> divisible_by_m(5,2)
  False
  >>> divisible_by_m(9,3)
  True
  """
  if n== (n//m * m) + n%m:
    return True
  else: 
   return False 
