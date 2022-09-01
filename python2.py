alien_0 = {'color': 'red'}
print(f"The alien is {alien_0['color']}.")

alien_0['color']: 'yellow'
print(f"The alien is now {alien_0['color]}.")

alien_1 = {'x_position': 0 ,'y_position': 25,'speed': 'medium'}
print(f"Original position: {alien_1['x_position']}")


if alien_1['speed'] == 'slow':
    x_increment = 1

elif alien_1['speed'] == 'medium':
    x_increment = 2

else:
    x_increment = 3
    
alien_1['x_position'] = alien_1['x_position'] + x_increment

print(f"New position : {alien_1['x_position']}")



