class Terreno:
    
    def __init__(self, A, B, C):
        self.__A = A
        self.__B = B
        self.__C = C
        
    def calcularAreaTerreno(self):
        areaTriangulo = (self.__B * self.__A) / 2
        areaRectangulo = self.__B * self.__C
        areaTotal = areaTriangulo + areaRectangulo
        
        return areaTotal