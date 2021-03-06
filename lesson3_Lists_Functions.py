list_numbers = [1,2,3,4,5]
#1. index() -> finding the index of a value in the list
print('Index of 5 in the list: ', list_numbers.index(5))

#2. append() -> appending / inserting a vaue at the end of the list
list_numbers.append(6)
print('List: ', list_numbers)

#3. insert() -> inserting a value at a particular index
#syntax: list_numbers.insert(index, element)
list_numbers.insert(2, 100)
print('100 inserted at index 2: ', list_numbers);

#3. pop() -> popping the value at the end of the list
popped_value = list_numbers.pop()
print('Popped value: ', popped_value)
print('List after value is popped', list_numbers)

#4. sort() -> sorts in ascending order
list_numbers.sort()
print('Sorted list: ', list_numbers)

#5. reverse() -> sorts in descending order
list_numbers.reverse()
print('Reversed list:', list_numbers)

#6. slice() -> to slice a list to get only a certain portion
#syntax: list_name[start:end]
print('List slice list_numbers[1:3] ', list_numbers[1:3])    #slices from index 1 to index 3. excuding of the last index
print('List slice list_numbers[0:] ', list_numbers[0:])    #slices from index 0 to the end, no limit
print('List slice list_numbers[:-1] ', list_numbers[0:-2])    #slices from the start to index -2

#7. concantenating a list
#syntax -> list1 + list2
list1 = ["Luciana", "Murimi"]
list2 = ["Mary", "Murimi"]

print(list1 + list2)
