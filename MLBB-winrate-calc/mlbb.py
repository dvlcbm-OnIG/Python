#mlbb winrate calculator
'''
print('MLBB Winrate Calculator')
print()

win = int(input('enter number of wins: '))
lose = int(input('enter number of loses: '))

calc = (win/(win + lose)) * 100


print(f'Winrate: {calc}%')


print()
'''

import math
print('MLBB Winrate predict')
print()

'''
tm = total_matches 
cw = current_winrate  
tw = target_winrate
rw = required_wins
'''

tm = int(input('enter total matches: '))
cw = float(input('enter current winrate: ')) /100
tw = float(input('enter target winrate: ')) /100

 
rw = tm * ((tw - cw)/(1- tw))
rw = math.ceil(rw)  

print(f'Winstreak Required: {rw}')


#math.ceil is used for rounding the number UP to the nearest whole integer. e.g, 1.1 to 1.9 is always = 2