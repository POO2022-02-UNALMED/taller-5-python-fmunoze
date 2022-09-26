from gestion.zona import Zona
from gestion.zoologico import Zoologico

class Animal:

    _totalAnimales = 0

    def __init__(self,nombre=None,edad=0,habitat=None,genero=None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        Animal._totalAnimales+=1

    def movimiento(self):
        return "desplazarse"
    
    @classmethod
    def totalPorTipo(cls):
        str = f'''
        Mamiferos: {Mamifero.cantidadMamiferos()}\n
        Aves: {Ave.cantidadAves()}\n
        Reptiles: {Reptil.cantidadReptiles()}\n
        Peces: {Pez.cantidadPeces()}\n
        Anfibios: {Anfibio.cantidadAnfibios()}
        '''
        return str
    def __str__(self):
        if zona is None or zona==[]:
            str = f'''
            Mi nombre es {self._nombre}, tengo {self._edad}, habito en {self._habitat} y mi genero es {self._genero}
            '''
        else:
            str = f'''
            Mi nombre es {self._nombre}, tengo {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {zona[0]}, en el {zona[0].getZoo()}
            '''
        return str

    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre
    
    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales
    @classmethod
    def setTotalAnimales(cls, totalAnimales):
        cls._totalAnimales = totalAnimales

    def getZona(self):
        return self._zona
    def setZona(self, zona):
        self._zona = zona
    
    def getGenero(self):
        return self._genero
    def setGenero(self,genero):
        self._genero = genero

    def getHabitat(self):
        return self._habitat
    def setHabitat(self,habitat):
        self._habitat = habitat
    
    def getEdad(self):
        return self._edad
    def setEdad(self,edad):
        self._edad = edad