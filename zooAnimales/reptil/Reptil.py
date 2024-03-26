##imports 
from animal import Animal

##clase 
class Reptil (Animal):
    listado = []
    iguanas = 0 
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas,largoCola):
        super.__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil.listado.append(self)

    ##setter y getter
    def setColorEscamas(self, color):
        self._colorEscamas = color

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setLargoCola(self, largo):
        self._largoCola = largo

    def getLargoCola(self):
        return self._largoCola
    
    ##métodos
    def movimiento(self):
        return "reptar"
    
    @classmethod
    def cantidadReptiles(cls):
        return len(cls.listado)
    
    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        cls.__init__(nombre, edad, "humedal", genero, "verde", 3 )
        cls.iguanas+=1

    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        cls.__init__(nombre, edad, "jungla", genero, "blanco", 1 )
        cls.serpientes+=1

