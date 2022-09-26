class Zona:

    def __init__(self,nombre=None,zoo=None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = None

    def agregarAnimales(self,animal):
        if self._animales is None:
            self._animales=[]
        if animal!=None:
            self._animales.append(animal)
    def cantidadAnimales(self):
        return len(self._animales)

    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getZoo(self):
        return self._zoo
    def setZoo(self, zoologico):
        self._zoo = zoologico

    def getAnimales(self):
        return self._animales
    def setAnimales(self, animales):
        self._animales = animales