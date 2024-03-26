##clase 
class Animal:

    _totalAnimales = 0
    
    ##constructor 
    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None

        Animal._totalAnimales += 1

    ##setter y getter 
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, name):
        self._nombre = name

    def getEdad(self):
        return self._edad
    
    def setEdad(self, edad):
        self._edad = edad
    
    def getHabitat(self):
        return self._habitat
    
    def setHabitat(self, habi):
        self._habitat = habi
    
    def getGenero(self):
        return self._genero
    
    def setGenero(self, gen):
        self._genero = gen

    def getZona(self):
        return self._zona
    
    def setZona(self, zon):
        self._zona = zon

    ##métodos
    def movimiento(self):
        return "desplazarse"
    
    ##total pot tipo

    def __str__(self):
        return "“Mi nombre es",self._nombre,"tengo una edad de", self._edad,"habito en", self._habitat,"y mi genero es",self._genero,"la zona en la que me ubico es", self._zona," en el", self._zona.getZoo()









