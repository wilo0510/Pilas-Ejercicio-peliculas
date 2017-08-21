import os


class Pilas:
    def __init__(self):
        self.pila = []

    def agregar(self, elemento):
        self.pila.append(elemento)

    def sacar(self):
        try:
            return self.pila.pop()
        except IndexError:
            raise ValueError("La pila está vacía")

    def vacia(self):
        return self.pila == []


class Peliculas:
    def __init__(self, pelicula, actor, genero):
        self.pelicula = pelicula
        self.actor = actor
        self.genero = genero


def main():
    pila = Pilas()
    pelicula0 = Peliculas("paquita la del barrio", "paquita", "accion")
    pelicula1 = Peliculas("teemo el demonio", "teemo", "accion")
    pelicula2 = Peliculas("los azules", "pepito", "accion")
    pelicula4 = Peliculas("los morados", "cosita", "accion")
    pelicula3 = Peliculas("los mochos", "nerd", "accion")
    pelicula5 = Peliculas("cosita", "fea", "accion")
    pelicula6 = Peliculas("perro", "gris", "accion")
    pila.agregar(pelicula0)
    pila.agregar(pelicula2)
    pila.agregar(pelicula3)
    pila.agregar(pelicula4)
    pila.agregar(pelicula6)
    pila.agregar(pelicula1)
    pila.agregar(pelicula5)
    print("sistemas de peliculas")
    print("escoja el numero adecuado para buscar la pelicula")
    print("1.nombres")
    print("2.Actor")
    print("3.genero")
    opcion = input()
    if (opcion == "1"):
        print("ingrese el nombre de la pelicula")
        nPelicula = input()
        while pila.vacia() == False:
            obj = pila.sacar()
            if nPelicula==obj.pelicula:
                print("Nombre: " + obj.pelicula + "  Actor: " + obj.actor + "  genero: " + obj.genero)

    elif opcion == "2":
        print("ingrese el nombre del actor")
        nombreActor = input()
        while pila.vacia() == False:
            obj = pila.sacar()
            if nombreActor==obj.actor:

                print("Nombre: " + obj.pelicula + "  Actor: " + obj.actor + "  genero: " + obj.genero)
    elif opcion == "3":
        print("ingrese el genero de la pelicula")
        genero = input()
        while pila.vacia() == False:
            obj = pila.sacar()
            if genero==obj.genero:
                print("Nombre: " + obj.pelicula + "  Actor: " + obj.actor + "  genero: " + obj.genero)




if __name__ == "__main__":
    main()
