phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}


'''
print(type(phonebook))
print('*****  start section 1 - print dictionary ********')
print(phonebook)





print(phonebook['Chris'])
print(phonebook['Chri'])



print('*****  end section 1 ********')
print()

'''

if 'Chris' in phonebook:
    print(phonebook['Chris'])
else:
    print('Key not found')
 


'''

print()
print('*****  start section 2 - search dictionary ********')
print()






print()
print('*****  end section 2 ********')
print()


print()
print('*****  start section 3 - edit/append dictionary ********')
print(phonebook)


phonebook['Joe']= '555-1234'

phonebook['Chris']= '555-3214'


print(phonebook)
print('*****  end section 3 ********')
print()








print()
print('*****  start section 4 - delete/remove from dictionary ********')
print(phonebook)

del phonebook['Chris']
#del phonebook['John']



print(phonebook)
print('*****  end section 4 ********')
print(len(phonebook))






print()
print('*****  start section 5 - iterate through keys ********')
print()

for i in phonebook:
    print(phonebook[i])


print()
print('*****  end section 5 ********')
print()




print()
print('*****  start section 6 - iterate through values  ********')
print()

for v in phonebook.values():
    print(v)



print()
print('*****  end section 6 ********')
print()






print()
print('*****  start section 7 - iterate through both key and value pair********')
print()


for k,v in phonebook.items():
    print("key is: "+ k + " and value is "+ v)

print()
print('*****  end section 7 ********')
print()



print(phonebook.get('John','9999-999'))


for item_tupple in phonebook.items():
    print(item_tupple)


'''


print()
print('*****  start section 8 - using random and converting to list ********')
print()

list_of_keys=list(phonebook)

print(type(list_of_keys))

import random

random_key=random.choice(list_of_keys)

print(random_key)
print(phonebook[random_key])


print()
print('*****  end section 8 ********')
print()



