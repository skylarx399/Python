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
