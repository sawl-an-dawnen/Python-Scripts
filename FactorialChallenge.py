def factorial(num):
  total = 1
  if type(num) == int and num >= 0:
    while num > 0:
      total *= num
      num -= 1
  else:
    return None
  return total

#print(factorial(6))
#print(factorial("Fun!"))
#print(factorial(-1))

def rec_factorial(num):
  try:
    if num < 0:
      return None
    return num * rec_factorial(num - 1) if num > 0 else 1
  except TypeError:
    return None

print(rec_factorial(5))
print(rec_factorial(6))
print(rec_factorial("number"))
print(rec_factorial(-3))