# Replace list items
fruit_list = ['Apple', 'Banana', 'Cherry', 'Orange', 'Grape']

# Меняет местами или изменяет на другие??
# swap
temp_fruit = fruit_list.pop(-1)
fruit_list.insert(0, temp_fruit)
temp_fruit = fruit_list.pop(1)
fruit_list.append(temp_fruit)
print(fruit_list)

# change
veg_list = ['Potato', 'Tomato']
fruit_list.pop(0)
fruit_list.pop(-1)
fruit_list.insert(0, veg_list[0])
fruit_list.append(veg_list[1])
print(fruit_list)
