# create initial array
import array

temperature = array.array('f',[72.5, 74.0, 69.8, 70.2, 73.1, 75.6, 71.3])
print(temperature)

# insertion and deletion
updated_temperature = temperature.pop(3)
print(updated_temperature)
temperature.insert(3, 70.0)
print(temperature)
temperature.append(78.0)
print(temperature)

#modifying array with loops
index = 0 
for i in range (len(temperature)):
    temperature[i] += 1.0
print(temperature)

