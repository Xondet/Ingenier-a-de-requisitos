class Trabajador:
    
    def __init__(self, pagoHora):
        self.__pagoHora = pagoHora
        
    def getPagoHora(self):
        return self.__pagoHora
    
    def calcularSueldo(self, horasTrabajadas):
        pagoDia = horasTrabajadas * self.__pagoHora
        pagoSemanal = pagoDia * 6
        return pagoSemanal