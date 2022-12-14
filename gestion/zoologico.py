class Zoologico:

    def __init__(self,nombre=None,ubicacion=None):
        self._nombre=nombre
        self._ubicacion=ubicacion
        self._zonas=None
    
    def agregarZonas(self,Zona):
        if self._zonas is None:
            self._zonas=[]
        if Zona != None:
            self._zonas.append(Zona)
    def cantidadTotalAnimales(self):
        cantidadAnimales = 0
        for zona in self._zonas:
            cantidadAnimales += zona.cantidadAnimales()
        return cantidadAnimales
    
    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getUbicacion(self):
        return self._Ubicacion
    def setUbicacion(self, ubicacion):
        self._Ubicacion = ubicacion
    
    def getZona(self):
        return self._zonas
    def setZona(self,zonas):
        self._zonas =zonas
