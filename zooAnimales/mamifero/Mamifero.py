##imports
from animal import Animal

##Clase
class Mamifero(Animal):

    listado = []
    caballos = 0
    leones = 0

    ##constructor
    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje 
        self._patas = patas
        Mamifero.listado.append(self)

    ##setter y getter
    def getPelaje(self):
        return self._pelaje
    
    def setPelaje(self, boo):
        self._pelaje = boo

    def getPatas(self):
        return self._patas
    
    def setPatas(self, pat):
        self._patas = pat

    ##métodos
    @classmethod
    def CantidadMamiferos(cls):
        return len(cls.listado)
    
    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        Mamifero.__init__(nombre, edad, "pradera", genero, True, 4)
        cls.caballos += 1

    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        Mamifero.__init__(nombre, edad, "selva", genero, True, 4)
        cls.leones += 1
    
    

    


    
