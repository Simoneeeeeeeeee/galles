#esercizio 1
import random
x=random.randrange(0,50)
y=random.randrange(0,50)
z=random.randrange(0,50)
if x<y and x<z:
    print(x)
    if y<z:
        print(y)
        print(z)
    else:
        print(z)
        print(y)
elif y<z:
    print(y)
    if x<z:
        print(x)
        print(z)
    else:
        print(z)
        print(x)
else:
    print(z)
    if x<y:
        print(x)
        print(y)
    else:
        print(y)
        print(x)
#esercizio 2
auto=['toyota','nissan','ferrari','lamborghini','bmw']
moto=['ktm','tm','ducati','aprilia']
lista = auto + moto
lista.sort()
print(lista)
#esercizio 3
lista=[]
listadispari=[]
for i in range(50):
    lista.append(random.randint(0,1000))
for x in lista:
    if x%2==1:
        listadispari.append(x)
lista=listadispari
print(lista)
#esercizio 4
lista=[]
kenawi=0
for i in range(50):
    lista.append(random.randint(1,100))
for x in lista:
    if x>50 or x<10:
        print(x)
        kenawi=kenawi+1
    print(kenawi)