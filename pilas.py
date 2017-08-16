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
    def __init__(self,pelicula,actor,genero):
        self.pelicula=pelicula
        self.actor=actor
        self.genero=genero

def main():
    pila = Pilas()
    pelicula0 = Peliculas("paquita la del barrio", "paquita","accion")
    pelicula1 = Peliculas("teemo el demonio", "teemo","accion")
    pelicula2 = Peliculas("los azules", "pepito","accion")
    pelicula4 = Peliculas("los morados", "cosita","accion")
    pelicula3 = Peliculas("los mochos", "nerd","accion")
    pelicula5 = Peliculas("cosita", "fea","accion")
    pelicula6 = Peliculas("perro", "gris","accion")
    pila.agregar(pelicula0)
    pila.agregar(pelicula2)
    pila.agregar(pelicula3)
    pila.agregar(pelicula4)
    pila.agregar(pelicula6)
    pila.agregar(pelicula1)
    pila.agregar(pelicula5)
    while pila.vacia() == False:
        pelicula = pila.sacar()
        print("Nombre: " + pelicula.pelicula + "  Codigo: " + pelicula.actor + "  Placa: " + pelicula.genero)

if __name__ == "__main__":
    main()