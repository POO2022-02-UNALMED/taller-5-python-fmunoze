from zooAnimales.animal import Animal

class Anfibio(Animal):

    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self,nombre=None,edad=0,habitat=None,genero=None,colorPiel=None,venenoso=False):
        super().__init__(nombre,edad,habitat,genero,)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
    
    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)
    def movimiento(self):
        return "saltar"
    @classmethod
    def crearRana(cls,nombre,edad,genero):
        return Anfibio(nombre,edad,"selva",genero,"rojo",True)
    @classmethod
    def crearSalamandra(cls,nombre,edad,genero):
        return Anfibio(nombre,edad,"selva",genero,"negro y amarillo",False)

    def getColorPiel(self):
        return self._colorPiel
    def setColorEscamas(self,color):
        self._colorPiel = color
    
    def getVenenoso(self):
        return self._venenoso
    def setVenenoso(self,venenoso):
        self._venenoso = venenoso