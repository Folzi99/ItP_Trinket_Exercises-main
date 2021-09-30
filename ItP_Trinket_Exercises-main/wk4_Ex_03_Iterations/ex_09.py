#!/bin/python3
value = 0
plier = 0
while value < 10:
  value += 1
  print('line', value, '->',  end='\n')
  while plier < value*9:
      plier += value
      print(plier, end= '')
  print("")
