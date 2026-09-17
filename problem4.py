def is_triangle(a,b,c):
  """
  number number number -> boolean
  takes three numbers a,b,c as input and returns True if these numbers can be the side lengths of a triangle and False otherwise

  >>> is_triangle(3,6,9)
      return True
  >>> is_triangle(4,5,8)
      return False
  """
  if a+b==c:
    return True
  else:
    return False
