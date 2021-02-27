import re

numero_tarjeta = list(input("Ingresar el número de tarjeta: "))


digito_control = numero_tarjeta.pop()

numero_tarjeta.reverse()

procesar_digitos = []

for index, digito in enumerate (numero_tarjeta):
    if index % 2 == 0:
        doble_digito = int(digito)*2
        if doble_digito > 9:
            doble_digito = doble_digito - 9
        procesar_digitos.append(doble_digito)
    else:
        procesar_digitos.append(int(digito))

total = int(digito_control) + sum(procesar_digitos)

if total % 10 == 0:
    print ("¡Valido!")
    for example in numero_tarjeta:
        regex = r"^[3]"
        regex2 = r"^[4]"
        regex3 = r"^[5]"
    # Match the regex to the string
    if re.match(regex, example):
        # Complete the format method to print out the result
        #x= r"\w+@gmail.com"
        #print("La direccion de correo es valida",(re.findall(patron,x)))
        print("EL número de tarjeta es American Express".format(email_example=example))
    elif re.match(regex2, example):
        print("EL número de tarjeta es Visa".format(email_example=example))
    elif re.match(regex3, example):
        print("EL número de tarjeta es MasterCard".format(email_example=example))
    
else: 
    print("¡Invalido!")
    


