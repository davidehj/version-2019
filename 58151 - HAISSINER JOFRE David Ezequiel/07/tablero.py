def draw_tablero(tablero):
    print(" "+tablero[0]+" | "+tablero[1]+" | "+tablero[2])
    print("---+---+---")
    print(" "+tablero[3]+" | "+tablero[4]+" | "+tablero[5])
    print("---+---+---")
    print(" "+tablero[6]+" | "+tablero[7]+" | "+tablero[8])
def validate(tablero,posicion):
    return tablero[posicion-1]==" "
def tateti(tablero):
    if tablero[0]!=" " and tablero[0]==tablero[1] and tablero[1]==[2]:
        return True
    if tablero[3]!=" " and tablero[3]==tablero[4] and tablero[4]==[5]:
        return True
    if tablero[6]!=" " and tablero[6]==tablero[7] and tablero[7]==[8]:
        return True
    if tablero[0]!=" " and tablero[0]==tablero[3] and tablero[3]==[6]:
        return True
    if tablero[1]!=" " and tablero[1]==tablero[4] and tablero[4]==[7]:
        return True
    if tablero[2]!=" " and tablero[2]==tablero[5] and tablero[5]==[8]:
        return True
    if tablero[0]!=" " and tablero[0]==tablero[4] and tablero[4]==[8]:
        return True
    if tablero[2]!=" " and tablero[2]==tablero[4] and tablero[4]==[6]:
        return True
    return False
def full(tablero):
    return not " " in tablero