import random
def generador(min,max):
    return random.randint(min,max)
    
#if __name__=="__main__":
 #   print(generador(1,20))

def generador_mejor (minimo,maximo,lista):
    encontrado=True
    while encontrado:
        aleatorio=random.randint(minimo,maximo)
        encontrado=aleatorio in lista
        #encontrado=aleatorio in lista es lo mismo que estas 3 lineas de abajo, si aleatorio esta en la lista devuelve un true, sino devuelve un false
        #encontrado=False
        #if aleatorio in lista:
            #encontrado=True
    return aleatorio