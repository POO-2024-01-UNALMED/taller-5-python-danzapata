##clase Zona 
class Zona:
    ## constructor 
    def __init__(self, nombre, zoo = None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []

    ##setter y getter
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, name):
        self._nombre = name

    def getZoo(self):
        return self._zoo
    
    def setZoo(self, zoo):
        self._zoo = zoo

    ##métodos
    def agregarAnimales(self, *args):
        for i in args:
            self._animales.append(i)
    
    def cantidadAnimales(self):
        return len(self._animales)
    
    
