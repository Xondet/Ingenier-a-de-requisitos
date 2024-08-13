class Productor:
    
    def __init__(self, pagoPorGalon):
        self.__pagoPorGalon = pagoPorGalon
        
    def getPagoPorGalon(self):
        return self.__pagoPorGalon
    
    def calcularPagoPorDia(self, litrosPorDia):
        numeroGalones = litrosPorDia / 3.785
        pagoPorDia = numeroGalones * self.__pagoPorGalon
        return pagoPorDia
