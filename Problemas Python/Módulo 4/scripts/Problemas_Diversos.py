print('Parte 1')
n = int(input('Introduce un número entero entre 1 y 10: '))
file_name = 'tabla-' + str(n) + '.txt'
f = open(file_name, 'w')
for i in range(1, 11):
    f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')
f.close()
print('---------------------------------------------------------------------')

print('Parte 2')
n = int(input('Introduce un número entero entre 1 y 10: '))
file_name = 'tabla-' + str(n) + '.txt'
try: 
    f = open(file_name, 'r')
except FileNotFoundError:
    print('No existe el fichero con la tabla del', n)
else:
    print(f.read())
print('---------------------------------------------------------------------')

print('Parte 3')
n = int(input('Introduce un número entero entre 1 y 10: '))
m = int(input('Introduce otro número entero entre 1 y 10: '))
file_name = 'tabla-' + str(n) + '.txt'
try: 
    f = open(file_name, 'r')
except FileNotFoundError:
    print('No existe el fichero con la tabla del ', n)

else:
    lines = f.readlines()
    print(lines[m - 1])

print('---------------------------------------------------------------------')

print('Expresiones Regulares')

from modulo import datos
import re

path = './data/re/short_tweets.csv'

s = '@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%'
s
patron = r"@robot\d\D"
print(re.findall(patron, s))

print('---------------------------------------------------------------------')
# Cadena entrada
s = "Unfortunately one of those moments wasn't a giant squid monster. User_mentions:2, likes: 9, number of retweets: 7"
s
patron = r"User_mentions:\d"
patron2= r"likes:\s\d"
patron3= r"number of retweets:\s\d"
print("Los usuarios que sigues este patron son: User_mentions:",(re.findall(patron, s)))
print("El número de likes es:",(re.findall(patron2, s)))
print("El numero de retweets",(re.findall(patron3, s)))

print('---------------------------------------------------------------------')


import re
path = './data/re/short_tweets.csv'
analisis_sentimientos = datos.read_pandas(path,780,782)
regex = r"\w+.txt"  # complete aqui
for tweet in analisis_sentimientos:
    print (re.findall(regex, tweet))
    #print(tweet)
    
    #Encuentre todos los casos
    #print(re.findall(regex, tweet))
    #print (re.findall(regex, tweet))

#regex = r""  # complete aqui
for tweet in analisis_sentimientos:
    print(tweet)
    
    # Encuentre todos los casos
    #print(re.findall(regex, tweet))
print('---------------------------------------------------------------------')


import re
regex = r"\w+[._]\w+[._]\w+@\w+.com"
regex2 = r"\w+@\w+.com"


emails = ['n.john.smith@gmail.com', '87victory@hotmail.com', '!#mary-=@msca.net']
for example in emails:
    # Match the regex to the string
    if re.match(regex, example):
        # Complete the format method to print out the result
        #x= r"\w+@gmail.com"
        #print("La direccion de correo es valida",(re.findall(patron,x)))
        print("The email {email_example} is a valid email".format(email_example=example))
    elif re.match(regex2, example):
        print("The email {email_example} is a valid email".format(email_example=example))
    else:
        print("The email {email_example} is invalid".format(email_example=example))
        