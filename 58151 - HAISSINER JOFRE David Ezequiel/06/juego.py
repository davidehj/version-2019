from generador import generador
buscado=generador(1,10000)
adivinado=False
max=10000
min=1
while adivinado==False:
    print("Ingresame un número papi")
    numero=int(input())
    if numero==buscado:
        adivinado=True
        print("GANASTE LOCO AGUANTE GODOY CRUZ")
    if numero>buscado:
        print("Nah boludo, más chiquito")
    if numero<buscado:
        print("Más grande la puta que te parió")
    if adivinado==False:
        print("Le toca a la computadora")
        npc=generador(min,max)
        if npc==buscado:
            print("Ganó la computadora capo, sos malísimo, el número era"+str(npc))
            adivinado=True
        if npc>buscado:
            print("La computadora eligió el número "+str(npc))
            max=npc
        if npc<buscado:
            print("La computadora eligió el número "+str(npc))
            min=npc
        
