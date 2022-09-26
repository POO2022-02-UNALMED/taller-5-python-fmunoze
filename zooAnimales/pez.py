from zooAnimales.animal import Animal

class Pez(Animal):
    _listado=[]
    salmones=0
    bacalaos=0
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas=colorEscamas
        self._cantidadAletas=cantidadAletas
        Pez._listado.append(self)
    
    def movimiento():
        return "nadar"

    
    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        Pez.salmones+=1
        return Pez(nombre, edad, "oceano", genero, "rojo", 6)
        
    @classmethod
    def crearBacalao(cls,nombre, edad, genero):
        Pez.bacalaos+=1
        return Pez(nombre, edad, "oceano", genero, "gris", 6)
    
    @classmethod
    def cantidadPeces(cls):
        return len(Pez._listado)
    
    def getListado(cls):
        return Pez._listado
    
    def setListado(cls, listado):
        Pez._listado= listado
    
    def setColorEscamas(self, color):
        self._colorEscamas= color

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setCantidadAletas(self, aletas):
        self._cantidadAletas= aletas

    def getCantidadAletas(self):
        return self._cantidadAletas