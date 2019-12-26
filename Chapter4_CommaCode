#Automate the Boring Stuff with Python
#Chapter 4 Practice Project
#Comma Code:
#Say you have a list value like this:
#spam = ['apples', 'bananas', 'tofu', 'cats']
#Write a function that takes a list value as an 
#argument and returns a string with all the items 
#separated by a comma and a space, with and inserted 
#before the last item. For example, passing the previous 
#spam list to the function would return:
# 'apples, bananas, tofu, and cats'. But your function 
#should be able to work with any list value passed to it.

import copy
import random

def convertList(lists):
    
    listA = [str(i) for i in lists]
    listB = copy.copy(listA)
    listB[-1] = 'and ' + listB[-1]
    listFormat =  ', ' 
    listFormat = listFormat.join(listB)
    print("'" + listFormat + "'")

list1 = []
for i in range(10):
    list1.append(random.randint(1,300))  
list2 = ['Bavarian Beaver Cheese', 'Cheddar', 'Bree', 'Gouda']
convertList(list1)
convertList(list2)
