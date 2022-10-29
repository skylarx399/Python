# grades

score = float(input('enter total marks: '))
if score >100:
  print('wrong score')
elif score >= 90:
  print('A')
elif score >= 80:
  print('B')
elif score >= 70:
  print('C')
elif score >= 60:
  print('D')
if score > 50 and score <= 100:
  print('E')
  print('passed')
elif score < 50:
  print('Failed')
