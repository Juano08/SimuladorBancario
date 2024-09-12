__author__ = "Juan José Rueda Viveros"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "juan.ruedav@campusucc.edu.co"

from Fecha import Fecha

class CuentaCDT:

    '''#----------------------
    Atributos
    -----------------------'''

    __SaldoCuentaCDT = 0

    '''#-------------------
    Asociacion
    --------------------#'''

    FechaActual = Fecha()
    FechaSimulada = Fecha() 

    #metodos
    __method__ = "DarSaldo"
    __parameter__ = "ninguno"
    __returns__ = "Saldo de la cuenta"
    __Description__ = "Metodo que muestra el saldo de la cuenta"
    def DarSaldo(self):
        return self.__SaldoCuentaCDT