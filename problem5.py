def wears_jacket(temp, raining):
  """
  number boolean -> boolean
  takes in a number named temp and a boolean value named raining and returns True if she wears a jacket.

  >>> wears_jacket(50, False)
  True
  >>> wears_jacket(70, True)
  True
  >>> wears_jacket(65, False)
  False
  """
if temp <60 or raining:
  return True
else:
  return False
