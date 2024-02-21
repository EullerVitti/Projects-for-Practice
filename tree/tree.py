picture = [
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0]
]

for row in picture:
  for item in row:
    if item == 0:
      print(' ',end='')
    else:
      print('*',end='')
  print('') # new line
