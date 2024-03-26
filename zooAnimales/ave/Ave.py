##imports
from animal import Animal

##clase
class Ave (Animal):
    listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super.__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave.listado.append(self)

    ##setter y getter 
    def setColorPlumas(self, color):
        self._colorPlumas = color

    def getColorPlumas(self):
        return self._colorPlumas
    
    ##métodos
    def movimiento(self):
        return "volar"
    
    @classmethod
    def cantidadAves(cls):
        return len(cls.listado)
    
    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        cls.__init__(nombre, edad, "montañas", genero, "café glorioso")
        cls.halcones += 1

    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        cls.__init__(nombre, edad, "montañas", genero, "blanco y amarillo")
        cls.aguilas += 1

