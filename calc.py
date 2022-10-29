# Tip Calculator app

print('\n')
food_amounts = float(input('enter the food amount $:🍽 '))
print('\n')
food_amount = int(input('enter the food amount $:🍽 '))
print('\n')
print('---------------------------------------------')
print('\n')
tip_percentage = 20 / 100
print(f'💲 Tip percentage $: {tip_percentage}')
print('\n')
service_tax = 30 / 100
print(f'🤓 Service Tax $: {service_tax}')
print('\n')
print('----------------------------------------------')
print('\n')
tip_amount = food_amounts + food_amount + tip_percentage + service_tax
print('💵 $' + str(tip_amount))
print('\n')
print('----------------------------------------------')
#total = tip_amount
#print('💵 $' + str(total))
#print('----------------------------------------------')
