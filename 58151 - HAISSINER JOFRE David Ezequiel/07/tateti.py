from tablero import draw_tablero, full, validate, tateti
tablero=[]
draw_tablero([" "," "," "," "," "," "," "," "," "])
for i in range(0,9):
    tablero.append(' ')
while not tateti(tablero) and full(tablero)==False:
    print("Le toca a la X")
    valido=False
    while not valido:
        print("Ingresa posicion, va del 1 al 9")
        posicion =int(input())
        valido=validate(tablero,posicion)
    tablero[posicion-1]="X"
    draw_tablero(tablero)
    gano=tateti(tablero)
    if gano:
        print("Ganaron las X")
    else:
        print("Le toca a la O")
        valido=False
        while not valido:
            print("Ingresa posicion, va del 1 al 9")
            posicion =int(input())
            valido=validate(tablero,posicion)
        tablero[posicion-1]="O"
        draw_tablero(tablero)
        gano=tateti(tablero)
    if gano:
        print("Ganaron las O")