def anagrama():
    palabraUno = []
    palabraU = input("Ingrese la primera palabra: ")
    apalabraU = palabraUno.append(palabraU)
    palabraDos = []
    palabraD = input("Ingrese la segunda palabra: ")
    palabraD = palabraDos.append(palabraD)

    if palabraUno == palabraDos:
        print("Esto no es un anagrama")

    elif len(palabraUno) == len(palabraDos):
        comparacion(palabraUno, palabraDos)
        print("Si es un anagrama")
    else:
        print("No es un anagrama")


def comparacion(palabraUno, palabraDos):
    return [x for x in palabraUno if x in palabraDos]

anagrama()