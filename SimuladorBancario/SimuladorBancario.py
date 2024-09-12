__author__ = "Juan Jose Rueda Viveros"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "juan.ruedav@campusucc.edu.co"

from Fecha import Fecha 
from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente
from CuentaCDT import CuentaCDT

class SimuladorBancario:
    # Aqui inicia la declaracion de la clase

    '''#-------------------------------------
    # Atributos
    -------------------------------------#'''
    
    __cedula = " "
    __nombre = " " 
    __mesActual = 0

    '''#-----------------------------------------
    # Asociaciones
    ------------------------------------------'''
    
    __FechaActual = Fecha()
    __FechaSimulada = Fecha()
    __CuentaAhorros = CuentaAhorros()
    __CuentaCorriente = CuentaCorriente()
    __CuentaCDT = CuentaCDT() 

    #-------------------metodo----------------#

    __method__ = "DepositarCuentaCorriente"
    __parameter__ = "Monto"
    __returns__ = "ninguno"
    __Description__ = "metodo que permite depositar en la cuenta corriente"
    def DespositarCuentaCorriente(self, monto):
        self.__CuentaCorriente.ConsignarSaldo(monto)


    __method__ = "ConsultarSaldoTotal"
    __parameter__ = "Ninguno"
    __returns__ = "Saldo Total de la cuenta"
    __Description__ = "metodo que muestra el saldo total de la cuenta"
    def ConsultarSaldoTotal(self):
        # Aqui inicia mi codigo
        # Forma 1
        # return "El saldo total es: " + self.__CuentaAhorros.DarSaldo() + self.__CuentaCorriente.DarSaldo() + self.__CuentaCDT.DarSaldo()
        
        # forma 2
        # total = self.__CuentaCorriente.DarSaldo()+self.__CuentaAhorros.DarSaldo+ self.__CuentaCDT.DarSaldo()
        # return total 
        
        # Forma 3
        return self.__CuentaAhorros.DarSaldo() + self.__CuentaCorriente.DarSaldo() + self.__CuentaCDT.DarSaldo()
    
    __method__ = "PasarAhorroACorriente"
    __parameter__ = "Ninguno"
    __returns__ = "ninguno"
    __Description__ = "metodo que permite pasar saldo de ahorros a la cuenta corriente"
    def PasarAhorroACorriente(self):
        # Aqui Inicia mi codigo
        saldoAhorros = self.__CuentaAhorros.DarSaldo()
        self.__CuentaAhorros.RetirarValor(saldoAhorros)
        self.__CuentaCorriente.ConsignarSaldo(saldoAhorros)
    
    
    __method__ = "RetirarCorriente"
    __parameter__ = "ninguno"
    __returns__ = "ninguno"
    __Description__ = "Metodo que permite retirar un monto a la cuenta corriente"
    def RetirarCorriente (self, monto):
        # Aqui va mi codigo
        self.__SaldoCuentaCorriente = self.__SaldoCuentaCorriente-monto  



  ###########################
    __method__ = "Ahorrar"
    __parameter__ = ""
    __returns__ = ""
    __Description__ = ""
    def Ahorrar (self, monto):
        self.__CuentaCorriente.RetirarSaldo(monto)
        self.__CuentaAhorros.ConsignarValor(monto)

    __method__ = "DarSaldoCorriente"
    __parameter__ = "ninguno"
    __returns__ = "Saldo de la cuenta"
    __Description__ = "Metodo que muestra el saldo de la cuenta corriente"
    def DarSaldoCorriente(self):
        return self.__CuentaCorriente.DarSaldo()

    __method__ = "RetirarAhorro"
    __parameter__ = "Monto"
    __returns__ = "Retirar dinero cuenta ahorros"
    __Description__ = "metodo que permite retirar el monto que el usuario desee de la cuenta de ahorros"
    def RetirarAhorro(self, monto):
        self.__CuentaAhorros.RetirarValor(monto)

    __method__ = "RetirarTodo"
    __parameter__ = "ninguno"
    __returns__ = "Retirar todo el dinero"
    __Description__ = "metodo que se permite retirar todo el dinero de la cuenta de ahorros y cuenta corriente"
    def RetirarTodo(self):
        SaldoCorriente = self.__CuentaCorriente.DarSaldo()
        SaldoAhorros = self.__CuentaCDT__CuentaAhorrros.DarSaldo()
        self.__CuentaCorriente.RetirarSaldo(SaldoCorriente)
        self.__CuentaAhorros.RetirarValor(SaldoAhorros)
        
    __method__ = "DuplicarAhorro"
    __parameter__ = "ninguno"
    __returns__ = "Duplicar el ahorro"
    __Description__ = "metodo que permite duplicar la cantidad de dinero en la cuenta de ahorros"
    def DuplicarAhorro(self):
        self.__CuentaAhorros.ConsignarValor(self.__CuentaAhorros.DarSaldo())
    