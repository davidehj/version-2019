from generador import generador
adivinado=False
aleatorio=generador(1,20

)

while adivinado==False:
    print("ingrese un num entre 1 y 20")
    numero=int(input())
    if numero==aleatorio:
        print("has adivinao")
        adivinado=True
    if numero<aleatorio:
        print("mas grande pelotudo")
    if numero>aleatorio:
        print("mas chico imbecil")