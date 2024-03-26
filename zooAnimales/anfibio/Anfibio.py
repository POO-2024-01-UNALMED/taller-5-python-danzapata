##imports 
from animal import Animal

##clase 
class Anfibio(Animal):
    listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio.listado.append(self)

    ##setter y getter 
    def setColorPiel(self, color):
        self._colorPiel = color
    
    def getColorPiel(self):
        return self._colorPiel
    
    def setVenenoso(self, venenoso):
        self._venenoso = venenoso

    def isVenenoso(self):
        return self._venenoso
    
    ##métodos
    def movimiento(self):
        return "saltar"
    
    @classmethod
    def cantidadAnfibios(cls):
        return len(cls.listado)
    
    @classmethod
    def crearRana(cls, nombre, edad, genero):
        cls.__init__(nombre, edad, "selva", genero, "rojo", True)
        cls.ranas += 1
    
    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        cls.__init__(nombre, edad, "selva", genero, "negro y amarillo", False)
        cls.salamandras += 1