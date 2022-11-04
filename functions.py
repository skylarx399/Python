#No arguments inside a function

def say_my_name():
  print('skylarx')
  print('is')
  print('hidden')
say_my_name()

#one arguments inside a function
def say_my_name_2(name):
  print(name)
say_my_name_2('skylarx')

#multiple arguments
def greetings (greet, name):
  print(f'{greet},{name}!')
greetings('hola','Skylarx')

#multiple arguments
def greetings (name,greet='hola'):
  print(f'{greet},{name}!')
greetings('Skylarx')

#named arguments
greetings(greet='Hi',name='skylarx')

#positional arguments
greetings('Skylarx','hello')

def weather_to_emoji(weather):

  if weather == 'rain':
    print('☔')

  elif weather == 'cloudy':
    print('☁')

  elif weather == 'thunderstorm':
    print('🌩')

  else:
    print('😎')

#weather_to_emoji('rain')

def CalculateFoodTotal(Food, tip_percentage):
  tip = Food * (tip_percentage / 100)
  total = Food + tip
  print(f'Food amount $: {Food}' )
  print(f'💲 Tip amount $: {tip}' )
  print('\n')
  print(f'🤓 Total $: {total}' )
  return total

 #print(CalculateFoodTotal(100, 10))
CalculateFoodTotal(Food=100, tip_percentage=20)
