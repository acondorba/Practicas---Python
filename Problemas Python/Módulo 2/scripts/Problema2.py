print("Problema Encriptación")

def comprobar_positivo(num) :
    if k > 0 :
        return True
    return False
def codigo_ceaser(text, abc) :
    list_texto = list(text.lower())
    encriptado = list()
    for index,valor in enumerate(list_texto) :
        if list_texto[index] == ",":
            encriptado.append(",")
        if list_texto[index] == " " :
            encriptado.append(" ")
        else :
            for ind,val in enumerate(abc) :
                if list_texto[index] == abc[ind] :
                    i = ind
                    indice = (i+k)%26
                    encriptado.append(abc[indice]) 
                    break
    
    return encriptado

abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
bandera = False

while bandera == False :
    while True:
        try:
            k = int(input("Introduza un entero para el cambio de posición: "))
        except :
            print("Ha ocurrido un error, introduce bien el número")
        else:
            break
    bandera = comprobar_positivo(k)
            
texto = input("Introduzca un texto: ")
encriptado = ""
encriptado = "".join(codigo_ceaser(texto, abecedario))
print("Texto encriptado: ",encriptado)



print("Intento 2")
import string
ALFAFETO = string.ascii_lowercase
k = int(input('Introduzca k: '))
plaintext = input('Introduzca texto a cifrar: ')
ciphertext = ''
for l in plaintext:
    
    if l.lower() in ALFAFETO:
        p = ALFAFETO.find(l.lower())
        # algoritmo cesar
        c = (p + k) % 26
        
        if l.isupper():
            ciphertext += ciphertext.join(ALFAFETO[c].upper())
        else:
            ciphertext += ciphertext.join(ALFAFETO[c])
    else:
        ciphertext += ciphertext.join(l)
print("Texto encriptado: ",ciphertext)