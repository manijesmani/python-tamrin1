import random
javab = random.randint(1,10)

name = input('What is your name? ')
hads = input('What is your hads? ')
hads = int(hads)

while hads != javab:
    if hads > javab:
        print ('Zeyade!')
    else:
        print('Kame!')
    hads = input('What is your hads? ')
    hads = int(hads)
    
print('wowwwwwww!', name, 'you did it!')