from __future__ import print_function
# Simple Input and Output
print('Maroon', 5)

reply = input('Enter x and y, separated by spaces: ')
pieces = reply.split()
# print(pieces)
x = float(pieces[0])
y = float(pieces[1])
print(x,y, sep=':')


# Files
# r (Reading), w (Writing), a (Appending), rb (Binary), wb (Binary)

# Exception Handling
"""
def sqrt(x):
  if not isinstance(x, (int, float)):
    raise TypeError('x must be numeric')
  elif x < 0:
    raise ValueError('x cannot be negative')
  ...
"""

# Catching an exception
"""
try:
  ratio = x / y
except ZeroDivisionError:
  ...


try:
  fp = open('sample.txt')
except IOError as e:
  print('Unable to open the file: ', e)

Handling more than 1 type of errors

age = -1
while age <= 0:
  try:
    age = int(input('Enter your age in years: '))
    if age <= 0:
      print('Your age must be positive')
  except(ValueError, EOFError):
    print('Invalid response')

"""