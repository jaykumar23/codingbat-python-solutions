'''
Return True if the string "cat" and "dog" appear the same number of times in the given string.


cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True

'''
def cat_dog(str):
  c = str.count("cat")
  d = str.count("dog")
  if c == d:
    return True
  else:
    return False
