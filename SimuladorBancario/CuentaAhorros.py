__author__ = "Juan José Rueda Viveros"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "juan.ruedav@campusucc.edu.co"

class CuentaAhorros:
    '''#------------------------
    Atributos
    ------------------------#'''

    Saldo = 0 
    InteresMensual = 0

    '''#-----------------------
    Asociacion
    ------------------------#'''

    '''#-----------------------
    Metodos
    ------------------------#'''

    __method__ = "ConsignarValor"
    __parameter__ =  "nuevoValor"
    __returns__ = "Valor"
    __Description__ = "metodo que se ultiliza para consignar el valor deseado por el usuario"
    def ConsignarValor(self, nuevoValor):
        # Aqui va mi codigo
        self.Saldo += nuevoValor


    __method__ = "RetirarValor"
    __parameter__ = "Monto"
    __returns__ = "Valor"
    __Description__ = "metodo que permite retirar el valor que el usuario desee de la cuenta"
    def RetirarValor(self, monto):
        # Aqui va mi codigo 
        self.Saldo -= monto


    __method__ = "DarSaldo"
    __parameter__ = "niguno"
    __returns__ = "Saldo de la cuenta"
    __Description__ = "metodo que retorna el saldo Actual de la cuenta"
    def DarSaldo(self): 
        # Aqui va mi codigo 
        return self.Saldo

    __method__ = "darInteresMensual"
    __parameter__ = ""
    __returns__ = "InteresMensual"
    __Description__ = "metodo que permite consultar el interes de la cuenta"
    def DarInteresMensual(self):
        # Aqui va mi Codigo
        self.DarInteresMensual
    
    __method__ = "actualizarSaldoPorPasoMes"
    __parameter__ = ""
    __returns__ = "Saldo cada mes"
    __Description__ = "metodo que permite actualizar el saldo de la cuenta mes por mes"
    def actualizarSaldoPorPasoMes(self): 
        self.Saldo  