#import random
#hads = random.randint(1, 100)
#print (hads)

#javab = input ()
#while javab != 'd':
    #print (hads)
    #if javab == 'd':
        #print ('Afarin Python Janam!')


import random
a = 1
b = 99
hads = random.randint(a, b)
print (hads)

javab = input ('user idea : ')
while javab != 'd':
    if javab == 'b':
        a = hads
    elif javab == 'k':
        b = hads
    print (hads)
    hads = random.randint(a, b)
    javab = input ('User Idea : ')
print ('Haha, nice game!')