##Zoologico
class Zoologico:
    ##constructor 
    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []

    ##setter y getter
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, name):
        self._nombre = name

    def getUbicacion(self):
        return self._nombre
    
    def setUbicacion(self, ubi):
        self._ubicacion = ubi

    ##métodos
    def agregarZonas(self, *args):
        for i in args:
            self._zonas.append(i)

    def cantidadTotalAnimales(self):
        contador = 0
        for i in self._zonas:
            contador = contador+i.cantidadAnimales()
        return contador

    
        
