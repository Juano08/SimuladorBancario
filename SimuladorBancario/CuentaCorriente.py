__author__ = "Juan José Rueda Viveros"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "juan.ruedav@campusucc.edu.co"


class CuentaCorriente:
    #Aqui inicia la declaracion de la clase

    '''#----------------------------------
    Atributos
    ----------------------------------#'''

    __SaldoCuentaCorriente = 0

    '''#----------------------------------
    Asociacion
    ----------------------------------#'''


    #metodos

    __method__ = "DarSaldo"
    __parameter__ = "ninguno"
    __returns__ = "Saldo de la cuenta"
    __Description__ = "Metodo que muestra el saldo de la cuenta"
    def DarSaldo(self):
        return self.__SaldoCuentaCorriente
    
    __method__ = "ConsignarSaldo"
    __parameter__ = "ninguno"
    __returns__ = "ninguno"
    __Description__ = "Metodo que permite consignar un monto a la cuenta corriente"
    def ConsignarSaldo (self, monto):
        # Aqui va mi codigo
        self.__SaldoCuentaCorriente = self.__SaldoCuentaCorriente+monto

    __method__ = "RetirarSaldo"
    __parameter__ = "ninguno"
    __returns__ = "ninguno"
    __Description__ = "Metodo que permite retirar un monto a la cuenta corriente"
    def RetirarSaldo (self, monto):
        # Aqui va mi codigo
        self.__SaldoCuentaCorriente = self.__SaldoCuentaCorriente-monto

    # Tambien se puede usar el codigo del metodo de consignar valor y retirar valor como en la cuenta de ahorros (preferible hacerlo asi porque es la manera corta)