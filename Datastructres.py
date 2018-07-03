
import functools 
#List functions
print(list(filter(lambda x: x < 4, [1,2,3,4,5,4,3,2,1])))
print(functools.reduce(lambda x, y: x *y, [1,2,3,4]))


#Dictonary - Sort of a hashmap in java..
my_dictionary = {'Key': 'Value', 'Key2': 'Value2', 'Key3': 'Value3'}
my_dictionary1 = {x: x + 1 for x in range (10)}

## Printing out the keys
print(my_dictionary.keys())
## Printing out all of the values in the Dictionary
print(my_dictionary.values())

## Adding to the dictionary
my_dictionary[1] = 'Khalid'
my_dictionary[2] = 'Ola'
print(my_dictionary)

##Deleting a specific key from the dictionary.
del my_dictionary[1]
print(my_dictionary)

##Copying the entire dictonary to another dictonary
## Notice! Changes you do in the old dictionary will change the new one.
dictonary = my_dictionary

##Deleting the entire Dictionary
my_dictionary.clear()
print(my_dictionary)


#SETS gives you the opertunity of using union, intersection, difference
# |  unon, ^ intersection, - difference
my_set = set({'one', 'two', 'three', 'one'})
##Printing the enitre my_set. it will automatically delete duplicates
print(my_set)

my_set1 = set(['two', 'three', 'four'])

## gets rid of the duplicates in both of the lists.It will check the lists on eachother this is Union
print(my_set | my_set1)
## you could also do it like this set.union(my_set, my_set1)

##Finds the unique values from both of the list, This is intersection
print(my_set ^ my_set1)
## you could also do it like this set.intersection(my_set, my_set1)

##Finds the unique one against the list, this is difference 
print(my_set1 - my_set)
## you could also do it like this set.difference(my_set, my_set1)
##Adding to the set.
my_set.add('five')

