from zooAnimales.animal import Animal

class Reptil(Animal):

    _listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre=None,edad=0,habitat=None,genero=None,colorEscamas=None,largoCola=0):
        super().__init__(nombre,edad,habitat,genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)

    def movimiento(self):
        return "reptar"
    @classmethod
    def crearIguana(cls,nombre,edad,genero):
        return Reptil(nombre,edad,"humedal",genero,"verde",3)
    @classmethod
    def crearSerpiente(cls,nombre,edad,genero):
        return Reptil(nombre,edad,"jungla",genero,"blanco",1)
    @classmethod
    def cantidadReptiles(cls):
        return len(cls.getListado())

    def getColorEscamas(self):
        return self._colorEscamas
    def setColorEscamas(self, color):
        self._colorEscamas = color
    
    def getLargoCola(self):
        return self._largoCola
    def setLargoCole(self, largoCola):
        self._largoCola = largoCola
    
    @classmethod
    def getListado(cls):
        return cls._listado
    @classmethod
    def setListado(cls, listado):
        cls._listado = listado