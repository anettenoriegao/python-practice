#split function practice
names = "Antonino, Barbieri, Locatelli"
split_names = names.split()
print(split_names)

#import array
import array

a = array.array("i",[1,2,3,4,5])
print(a)

#more array practice
int_array = array.array('i',[20,30,40,50])
print("Integer Array:", int_array)

#array of floats
float_array = array.array('f',[1.4,2.5,3.7])
print("Float Array:",float_array)

# array of unicode characters
show_array = array.array('u', 'MasterChef')
print("Show Array:", show_array)

# inserting elements - append() and insert()
arr = array.array('i',[1,2,3])
arr.append(4)
arr.insert(1,5)

print(arr)

# deleting elements from an array - remove() and pop()
arr.remove(2)
arr.pop(1)
print(arr)

# loop traversing an array - for
for element in arr:
    print(element)

# while loop with arrays

print(len(arr))
index = 0

while index < len(arr):
    print(arr[index])
    index = index + 1

