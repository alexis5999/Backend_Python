class Vehiculo:
    def __init__(self, largo, ancho, motor, enMarcha=False):
        self.largo = largo # publico
        self.__ruedas = 4
        self.ancho = ancho
        self.motor = motor
        self.enMarcha = enMarcha
    
    # metodo: cumple la funcionalidad que una funcion pero
    # con diferencia que solo
    # se puede usar dentro de la clase
    def arrancar(self, arrancar):
        self.enMarcha = arrancar
        if (self.enMarcha):
            chequeo = self.__chequeo_interno()
            if (chequeo):
                return 'El coche esta en marcha sin problemas'
            else:
                return 'El coche esta en marcha pero hay un problema'
        else:
            return 'El coche esta parado'
    def __chequeo_interno(self):
        # Encapsulamos este metodo para que solo pueda
        # ser invocado dentro de la clase
        self.gasolina = 15
        self.aceite = 'Ok'
        self.temperatura = 40
        if(self.gasolina > 10 and self.aceite == 'Ok' and self.temperatura < 80):
            return True
        else:
            return False

    def mostrar_ruedas(self):
        return self.__ruedas
objVehiculo =Vehiculo(1.1,2.0,2000)
print(objVehiculo.mostrar_ruedas())
print(objVehiculo.arrancar(False))