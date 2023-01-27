# autogenerador de palabras con un random de 1 a 20 letras
# y un random de 1 a 10^6 palabras
# hay dos tipos de palabras, tipo 1 y tipo 2
# contar cuantas palabras se imprimieron en el archivo

import random
import string

def randomword(length): 
    letters = string.ascii_lowercase 
    return ''.join(random.choice(letters) for i in range(length)) 

# numero de palabras que se imprimen en el archivo
#max = 1000000 # maximo de palabras

# tipo de palabra
def randomtype():
    return random.randint(1,2)

def generar_problema(max):
    path = 'input.txt'
 
    try:
        with open(path, 'r+') as f:
            f.truncate()
    except IOError:
        print('Failure')
    
    file = open(path, "w")
    file.write(str(max) + "\n")
    file.write(str(1) + " " + randomword(random.randint(2,20)) + "\n")

    for i in range(max):     
        file.write(str(randomtype()) + " " + randomword(random.randint(2,20)) + "\n")
    
    file.close()
