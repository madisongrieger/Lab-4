def pythagorean_triples(a,b,c):
  """
  number number number -> boolean
  takes three parameters a,b,c and returns True if a^2+b^2=c^2 and False otherwise

  >>> pythagorean_triples(2,4,5):
  False
  >>> pythagorean_triples (2,0,2):
  True
  """
  if (a**2)+(b**2)==(c**2):
    return True
  else:
    return False
