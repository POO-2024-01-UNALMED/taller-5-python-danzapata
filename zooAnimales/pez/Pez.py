##imports
from animal import Animal

##clase 
class Pez(Animal):
    listado = []
    bacalaos = 0
    salmones = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez.listado.append(self)

    ##setter y getter 
    def setColorEscamas(self, color):
        self._colorEscamas = color

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setCantidadAletas(self, cantidad):
        self._cantidadAletas = cantidad
    
    def getCantidadAletas(self):
        return self._cantidadAletas
    
    ##métodos
    def movimiento(self):
        return "nadar"
    
    @classmethod
    def cantidadPeces(cls):
        return len(cls.listado)
    
    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        super().__init__(nombre, edad, "oceano", genero, "gris", 6 )
        cls.bacalaos+=1
    
    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        super().__init__(nombre, edad, "oceano", genero, "rojo", 6 )
        cls.salmones+=1


    
